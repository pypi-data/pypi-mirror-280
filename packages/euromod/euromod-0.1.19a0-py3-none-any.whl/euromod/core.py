import os
import time
import pandas as pd
import numpy as np
from utils._paths import CWD_PATH, DLL_PATH
from base import SystemElement, Euromod_Element
import clr as clr
import System as SystemCs
from utils.clr_array_convert import asNetArray,asNumpyArray
from utils.utils import is_iterable
clr.AddReference(os.path.join(DLL_PATH, "EM_Executable.dll" ))
from EM_Executable import Control
clr.AddReference(os.path.join(DLL_PATH, "EM_XmlHandler.dll" ))
from EM_XmlHandler import CountryInfoHandler,TAGS, ReadCountryOptions,ModelInfoHandler, ReadModelOptions
from info import Info
from container import Container
from typing import Dict, Tuple, Optional, List


class Model():
    """
    Euromod - a Python library for the microsimulation model EUROMOD.
    ===========================================================================

    **euromod** is a Python package that runs the microsimulation model EUROMOD
    provided by the European Commission - JRC. 
    
    *This package requires the EUROMOD software and model to be installed 
    on your device. For more information, please visit:
        https://euromod-web.jrc.ec.europa.eu/download-euromod

    EUROMOD:
    -------------
    is a tax-benefit microsimulation model for the European Union that enables 
    researchers and policy analysts to calculate, in a comparable manner, 
    the effects of taxes and benefits on household incomes and work incentives 
    for the population of each country and for the EU as a whole.

    Originally maintained, developed and managed by the Institute for Social and 
    Economic Research (ISER) of the University of Essex, since 2021 EUROMOD 
    is maintained, developed and managed by the Joint Research Centre (JRC) 
    of the European Commission, in collaboration with Eurostat 
    and national teams from the EU countries. 
    ===========================================================================
    """
    
    
    def __init__(self, model_path : str, countries = None):
        """
        

        Parameters
        ----------
        model_path : str
            path to the EUROMOD model.
        countries : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """
        self.model_path =  model_path
        self.countries = CountryContainer()
        self._hasMIH = False;
        if countries == None:
            countries = os.listdir(os.path.join(model_path,'XMLParam','Countries'))
            self._load_country(countries)
        else:
            countries_preload = os.listdir(os.path.join(model_path,'XMLParam','Countries'))
            self._load_country(countries_preload)
            for country in countries: #For countries explicitly demanded, load xmlInfoHandler already
                self.countries[country].load()
    def __repr__(self):
        return f"Model located in {self.model_path}"
                
                
    def __getattr__(self,name):
        if not self._hasMIH:
            self._modelInfoHandler = ModelInfoHandler(self.model_path)
            self._hasMIH = True
            
        if name == "extensions":
            self._load_extensions()
            return self.extensions
      
        
    def _load_extensions(self):
        
        self.extensions = Container()
        for el in self._modelInfoHandler.GetModelInfo(ReadModelOptions.EXTENSIONS):
            ext = Extension(el.Value,self)
            self.extensions.add(el.Key,ext)
        
        
    def _load_country(self, countries):        
        """
        Load objects of the TAGS.CONFIG_COUNTRY class.

        Parameters:
        -----------------------------------------------------------------------
            countries   : (str, list of str) 
                        The two-letters country codes (ex: ['IT','LV']).


       
        """

        if type(countries) not in [str, list, set]:
            raise TypeError("Parameter 'countries' must be str, list or set.")
        if type(countries) == str:
            countries = [countries]
            
    	### loop over countries to add the country containers
        for country in countries:            
            ### "Country" class is country specific
            self.countries.add(country,self)

    def __getitem__(self, country):
        return self.countries[country]
    
                


class Country(Euromod_Element):

    def __init__(self,country: str,model: str):
        self.name = country    
        self.model = model
        self._hasCIH = False
        self.systems = None
        self.policies= None
        self.datasets = None
        self.local_extensions = None

        
    def _load(self):
        if not self._hasCIH:
            if not Control.TranslateToEM3(self.model.model_path, self.name, SystemCs.Collections.Generic.List[str]()):
                raise Exception("Country XML EM3 Translation failed. Probably provided a non-euromod project as an input-path.")
            self._countryInfoHandler = CountryInfoHandler(self.model.model_path, self.name)
            self._hasCIH = True;
    
    def __getattribute__(self,name):
        if name == "systems" and self.__dict__["systems"] is None:
            self._load()
            self._load_systems()
            return self.systems
        if name == "policies" and self.__dict__["policies"] is None:
            self._load()
            self._load_policies()
            return self.policies
        if name == "datasets" and self.__dict__["datasets"] is None:
            self._load()
            self._load_datasets()
            return self.datasets
        if name == "local_extensions" and self.__dict__["local_extensions"] is None:
            self._load()
            self._load_extensions()
            return self.local_extensions
        return super().__getattribute__(name)
    
        
    def _load_extensions(self):
        self.local_extensions = Container()
        for el in self._countryInfoHandler.GetTypeInfo(ReadCountryOptions.LOCAL_EXTENSION):
            ext = Extension(el.Value,self)
            self.local_extensions.add(el.Key,ext)
    
    def _load_policies(self):
        self.policies = Container()
        for el in self._countryInfoHandler.GetTypeInfo(ReadCountryOptions.POL):
            pol = Policy(el.Value,self)
            self.policies.add(pol.ID,pol)
        for el in self._countryInfoHandler.GetTypeInfo(ReadCountryOptions.REFPOL):
            ref_pol = ReferencePolicy(el.Value,self)
            self.policies.add(ref_pol.ID,ref_pol)
        self.policies.containerList.sort(key=lambda x: int(self._countryInfoHandler.GetPieceOfInfo(ReadCountryOptions.SYS_POL,self.systems[-1].ID + x.ID)["Order"]))
        
        
    def _load_datasets(self):
        self.datasets = Container()
        for el in self._countryInfoHandler.GetTypeInfo(ReadCountryOptions.DATA):
            db = Dataset(el.Value,self)
            self.datasets.add(db.name,db)
        
    def _load_systems(self):
        self.systems = Container()
        systems = self._countryInfoHandler.GetTypeInfo(ReadCountryOptions.SYS)
        for sys in systems:
            self.systems.add(sys.Value["Name"],System(sys.Value,self))
        
    def load_data(self, ID_DATASET, PATH_DATA = None):
        if PATH_DATA == None:
            PATH_DATA = os.path.join(self.model.model_path, 'Input')
            
        fname = ID_DATASET + ".txt"    
        df = pd.read_csv(os.path.join(PATH_DATA, fname),sep="\t")
        df.attrs[TAGS.CONFIG_ID_DATA] = ID_DATASET
        df.attrs[TAGS.CONFIG_PATH_DATA] = PATH_DATA
        return df
        
          
                        
    def __getitem__(self, system):
        return self.systems[system]
    
    

    def _short_repr(self):
        return f"Country {self.name}"
        

        
        

class CountryContainer(Container):
    def add(self,name,model):
        countryObject = Country(name,model)
        self.containerDict[name] = countryObject
        self.containerList.append(countryObject)

 

class System(Euromod_Element):   
    def __init__(self,*arg):
        super().__init__(*arg)
        self.datasets = None
        self.policies = None
        self.bestmatch_datasets = None
    def __getattribute__(self,name):
        if name == 'policies' and self.__dict__["policies"] is None:
            self._load_policies()
            return self.policies
        if name == 'datasets' and self.__dict__["datasets"] is None:
            self._load_datasets()
            return self.datasets
        if name == 'bestmatch_datasets' and self.__dict__["bestmatch_datasets"] is None:
            self._load_bestmatchdatasets()
            return self.bestmatch_datasets
        
        return super().__getattribute__(name)
    def _load_bestmatchdatasets(self):
        self.bestmatch_datasets = Container()
        for x in self.datasets:
            if x.bestMatch == "yes":
                self.bestmatch_datasets.add(x.name,x)
             
    def _load_datasets(self):
        self.datasets = Container()
        for dataset in self.parent.datasets:
            id = self.ID + dataset.ID
            sysdata = self.parent._countryInfoHandler.GetPieceOfInfo(ReadCountryOptions.SYS_DATA,id)
            if len(sysdata) > 0:
                self.datasets.add(id,DatasetInSystem(sysdata, id, self, dataset))
    def _load_policies(self):
        self.policies = Container()
        for pol in self.parent.policies:
            id = self.ID + pol.ID
            syspol = self.parent._countryInfoHandler.GetPieceOfInfo(ReadCountryOptions.SYS_POL,id)
            self.policies.add(id,PolicyInSystem(syspol, id, self, pol))
    def _get_dataArray(self, df):
        ### check data format
        if type(df) != pd.core.frame.DataFrame:
            raise TypeError("Parameter 'data' must be a pandas.core.frame.DataFrame.")
        ### converting the numpy array to a DotNet/csharp array        
        dataArr=asNetArray(df.to_numpy(np.float64).T)
        return dataArr
        
    def _convert_configsettings(self, configSettings):
        ### check configSettings format
        if type(configSettings) != dict:
            raise TypeError("Parameter 'configSettings' must be dict.")
        ### Creation of csharp dictionary
        configSettingsDict = SystemCs.Collections.Generic.Dictionary[SystemCs.String,SystemCs.String]()
        for key,value in configSettings.items():
            configSettingsDict[SystemCs.String(key) ] = SystemCs.String(value)
        return configSettingsDict
    
    def _get_variables(self, df):
        #### Initialise Csharp object    
        variables = SystemCs.Collections.Generic.List[SystemCs.String]()
        for col in df.columns:
            variables.Add(col)
        return variables
    
    def _get_constantsToOverwrite(self, new_constdict):

         ### check configSettings format    
        if new_constdict == None:
            constantsToOverwrite = new_constdict
        else:
            if type(new_constdict) == dict:
                constantsToOverwrite = SystemCs.Collections.Generic.Dictionary[SystemCs.Tuple[SystemCs.String, SystemCs.String],SystemCs.String]()
                for keys,value in new_constdict.items():
                    if not is_iterable(keys):
                        raise TypeError("Parameter 'constantsToOverwrite' must be a dictionary, with an iterable containing the constant name and groupnumber as key and a string as value (Example: {('$f_h_cpi','2022'):'1000'}).")
                    key1 = keys[0]
                    key2 = keys[1] if keys[1] != "" else -2147483648

                        
                    csharpkey = SystemCs.Tuple[SystemCs.String, SystemCs.String](key1, key2)
                    constantsToOverwrite[csharpkey] = value

            else: 
                raise TypeError("Parameter 'constantsToOverwrite' must be a dictionary (Example: {('$f_h_cpi','2022'):'1000'}).")
        
        return constantsToOverwrite
    

                
    def _get_config_settings(self,dataset):
        configsettings = {}
        configsettings[TAGS.CONFIG_PATH_EUROMODFILES] = self.parent.model.model_path
        configsettings[TAGS.CONFIG_PATH_DATA] = ""
        configsettings[TAGS.CONFIG_PATH_OUTPUT] = ""
        configsettings[TAGS.CONFIG_ID_DATA] = dataset
        configsettings[TAGS.CONFIG_COUNTRY] = self.parent.name
        configsettings[TAGS.CONFIG_ID_SYSTEM] = self.name
        return configsettings
        
        
    def run(self,data: pd.DataFrame,dataset_id: str,constantsToOverwrite: Optional[Dict[Tuple[str, str], str]] = None,verbose: bool = True,outputpath: str = "",  addons: List[Tuple[str, str]] = [],  switches: List[Tuple[str, bool]] = [],nowarnings=False):
        """
        

        Parameters
        ----------
        data : pd.DataFrame
            input dataframe passed to the EUROMOD model.
        ID_DATASET : str
            ID of the dataset.
        constantsToOverwrite : Optional[Dict[Tuple[str, str], str]], optional
            A list of constants to overwrite. Note that the key is a tuple for which the first element is the name of the constant and the second string the groupnumber
            The default is None.
        verbose : bool, optional
            If True then information on the output will be printed. The default is True.
        outputpath : str, optional
            When an output path is provided, there will be anoutput file generated. The default is "".
        addons : List[Tuple[str, str]], optional
            List of addons to be integrated in the spine, where the first element of the tuple is the name of the Addon
            and the second element is the name of the system in the Addon to be integrated. The default is [].
        switches : List[Tuple[str, bool]], optional
            List of Extensions to be switched on or of. The first element of the tuple is the short name of the Addon.
            The second element is a boolean The default is [].

        Raises
        ------
        Exception
            Exception when simulation does not finish succesfully, i.e. without errors.

        Returns
        -------
        sim : TYPE
            simulation object containing the output and error messages

        """
 
        ### initialize the simulation dictionary
        if hasattr(self, 'simulations') is False:
            self.simulations = {}      
     
        
        configSettings = self._get_config_settings(dataset_id)
        if len(dataset_id) == 0:
            if TAGS.CONFIG_ID_DATA in data.attrs.keys():
                configSettings[TAGS.CONFIG_ID_DATA] = data.attrs[TAGS.CONFIG_ID_DATA] 
            else:
                configSettings[TAGS.CONFIG_ID_DATA] = dataset_id
        else:
            configSettings[TAGS.CONFIG_ID_DATA] = dataset_id
        if TAGS.CONFIG_PATH_DATA in data.attrs.keys():
            configSettings[TAGS.CONFIG_PATH_DATA] = data.attrs[TAGS.CONFIG_PATH_DATA]
        else:
            configSettings[TAGS.CONFIG_PATH_DATA] = os.path.join(configSettings[TAGS.CONFIG_PATH_EUROMODFILES], "Input")
            
        configSettings[TAGS.CONFIG_PATH_OUTPUT] = os.path.join(outputpath)
        
        if len(addons) > 0:
            for i,addon in enumerate(addons):
                if not is_iterable(addon):
                    raise(TypeError(str(type(addon)) + " is incorrect type for defining addon"))
                configSettings[TAGS.CONFIG_ADDON + str(i)] = addon[0] + "|" +  addon[1]
        if len(switches) > 0:
            for i,switch in enumerate(switches):
                if not is_iterable(switch):
                    raise(TypeError(str(type(switch)) + " is incorrect type for defining extension switch"))
                status = "on" if switch[1] else "off"
                configSettings[TAGS.CONFIG_EXTENSION_SWITCH + str(i)] = switch[0] + '=' +  status
        
        
        data = data.select_dtypes(['number'])

        ### get Csharp objects
        dataArr = self._get_dataArray(data)
        configSettings_ = self._convert_configsettings(configSettings)
        variables = self._get_variables(data)  
        constantsToOverwrite_ = self._get_constantsToOverwrite(constantsToOverwrite)      

        os.chdir(DLL_PATH)
        ### run system
        out = Control().RunFromPython(configSettings_, dataArr, variables, \
                                      constantsToOverwrite = constantsToOverwrite_,countryInfoHandler = self.parent._countryInfoHandler)
        os.chdir(CWD_PATH)
        sim = Simulation(out, configSettings, constantsToOverwrite) 
        if out.Item1:
            ### load "Simulations" Container
            if verbose:
                print(f"Simulation for system {self.name} with dataset {dataset_id} finished.")
        else:
            return out
            raise Exception(f"Simulation for system {self.name} with dataset {dataset_id} aborted with errors.")
      
        return sim
    
    #def __repr__(self):
     #   return f"System {self.name}"
    def _short_repr(self):
        return f"System {self.name}"
    
class OutputContainer(Container):
    def add(self,name,data):
        self.containerDict[name] = data
        self.containerList.append(data)
    def __repr__(self):
        s= ""
        for i,el in enumerate(self.containerList):
            s += f"{i}: {repr(el)}\n"
        return s
    
        
class PolicyContainer(Container):
    def add(self,id,policy):
        self.containerDict[id] = policy
        self.containerList.append(policy)

class FunctionContainer(Container):     
    def add(self,id,function):
        self.containerDict[id] = function
        self.containerList.append(function)
        

class Simulation:
    def __init__(self, out, configSettings, constantsToOverwrite):
        '''
        Simulations class. 
        
        Attributes:
        -----------------------------------------------------------------------
            configSettings        : (dict)
                                    Keys are : PATH_EUROMODFILES, PATH_DATA,
                                    PATH_OUTPUT, ID_DATASET, ID_SYSTEM.
                                    Values must be str.
            constantsToOverwrite  : (dict)
                                    Keys are tuple of two strings,
                                    Values are str with the new value.
                                    i.e. dict{tuple('constant_name','constant_group') : str}
            name                  : (str)
                                    Name of the simulation
            output                : (dict),
                                    K   
        '''  
        self.outputs = OutputContainer()
        
        if constantsToOverwrite is None:
            constantsToOverwrite = {}

        if (out.get_Item1()):
            dataDict = dict(out.get_Item2())
            variableNameDict = dict(out.get_Item3())
            for key in dataDict.keys():

                clr_arr = dataDict[key]
                temp = asNumpyArray(clr_arr)

                outputvars = list(variableNameDict[key])
                self.outputs.add(key, pd.DataFrame(temp, columns=outputvars))

        self.errors = [x.message for x in out.Item4]
        if len(self.errors) > 0:
            for error in self.errors:
                print(error)

        self.configSettings = configSettings.copy()
        self.constantsToOverwrite = constantsToOverwrite.copy()


    def __repr__(self):
        return f'''
output:               {self.outputs}

'''       




class Dataset(Euromod_Element):
    _objectType = ReadCountryOptions.DATA
    
    def _short_repr(self):
        return f"{self.name}"
    
class Policy(Euromod_Element):
    _objectType = ReadCountryOptions.POL
    _extensionType = ReadCountryOptions.EXTENSION_POL
    def _load_functions(self):
        self.functions = FunctionContainer()
        functions = self.parent._countryInfoHandler.GetPiecesOfInfo(ReadCountryOptions.FUN,TAGS.POL_ID,self.ID)
        for fun in functions:
            self.functions.add(fun["ID"] ,Function(fun,self))
        self.functions.containerList.sort(key=lambda x: int(self.parent._countryInfoHandler.GetPieceOfInfo(ReadCountryOptions.SYS_FUN,self.parent.systems[0].ID + x.ID)["Order"]))
    def _short_repr(self):
        ext = self._get_extension_repr()
        return f"Policy: {self.name}{ext}"
    def __getattribute__(self, name):
        if name == "extensions" and self.__dict__["extensions"] is None:
            self._linkToExtensions()
            return self.extensions
        if name == "functions" and self.__dict__["functions"] is None:
            self._load_functions()
            return self.functions
        return super().__getattribute__(name)

    def __init__(self,*arg):
        super().__init__(*arg)
        self.functions = None
        self.extensions = None
    
    
class ReferencePolicy(Euromod_Element):
    _objectType = ReadCountryOptions.REFPOL
    def __init__(self,info,parent):
        super().__init__(info,parent) #take the parent constructor
        #get name of the reference policy using RefPolID
        self.name = self.parent._countryInfoHandler.GetPieceOfInfo(ReadCountryOptions.POL,self.refPolID)["Name"]
        self.extensions = None


    def _short_repr(self):
        return f"Reference Policy: {self.name}"
    def __getattribute__(self, name):
        if name == "extensions" and self.__dict__["extensions"] is None:
            self._linkToExtensions()
            return self.extensions
        return super().__getattribute__(name)

           

class Function(Euromod_Element):
    _objectType = ReadCountryOptions.FUN
    _extensionType = ReadCountryOptions.EXTENSION_FUN

    def _short_repr(self):
        ext = self._get_extension_repr()
        return f"{self.name}{ext}"
    def _load_parameters(self):
        self.parameters = Container()
        functions = self.parent.parent._countryInfoHandler.GetPiecesOfInfo(ReadCountryOptions.PAR,TAGS.FUN_ID,self.ID)
        for fun in functions:
            self.parameters.add(fun["ID"] ,Parameter(fun,self))
        self.parameters.containerList.sort(key=lambda x: int(self.parent.parent._countryInfoHandler.GetPieceOfInfo(ReadCountryOptions.SYS_PAR,self.parent.parent.systems[0].ID + x.ID)["Order"]))
    
    def __getattribute__(self, name):
        if name == "extensions" and self.__dict__["extensions"] is None:
            self._linkToExtensions()
            return self.extensions
        if name == "parameters" and self.__dict__["parameters"] is None:
            self._load_parameters()
            return self.parameters
        return super().__getattribute__(name)
    def __init__(self,*arg):
        super().__init__(*arg)
        self.parameters = None
        self.extensions = None


class Parameter(Euromod_Element):
    _objectType = ReadCountryOptions.PAR
    _extensionType = ReadCountryOptions.EXTENSION_PAR
    def _short_repr(self):
        ext = self._get_extension_repr()
        return f"Parameter: {self.name}{ext}"
    def __getattr__(self,name):
        if name == "extensions":
            self._linkToExtensions()
            return self.extensions
        raise AttributeError();   
    def __getattribute__(self, name):
        if name == "extensions" and self.__dict__["extensions"] is None:
            self._linkToExtensions()
            return self.extensions

        return super().__getattribute__(name)
    def __init__(self,*arg):
        super().__init__(*arg)
        self.extensions = None


class PolicyInSystem(SystemElement):
    _objectType = ReadCountryOptions.SYS_POL
    def __init__(self,*arg):
        super().__init__(*arg)
        self.functions = None
    def _short_repr(self):
        ext = self._get_extension_repr()
        return f"{self.parentTypeObject.name}: {self.switch}{ext} \t {self.parentTypeObject.comment}"
    
    def __getattribute__(self, name):
        if name == "functions" and self.__dict__["functions"] is None:
            self._load_functions()
            return self.functions
        return super().__getattribute__(name)

        
    def _load_functions(self):
        self.functions = FunctionContainer()
        sys = self.parentSystem
        for fun in self.parentTypeObject.functions:
            id = sys.ID + fun.ID
            sysfun = self.parentSystem.parent._countryInfoHandler.GetPieceOfInfo(ReadCountryOptions.SYS_FUN,id)
            self.functions.add(id,FunctionInSystem(sysfun, id, sys, fun))
class ParameterInSystem(SystemElement):
    _extensionType = ReadCountryOptions.EXTENSION_PAR
    _ctryOption = ReadCountryOptions.SYS_PAR

    def _short_repr(self):
        return f"{self.parentTypeObject.name}: {self.value} \t {self.parentTypeObject.comment}" 
    
class DatasetInSystem(SystemElement):
    _ctryOption = ReadCountryOptions.SYS_DATA
    def _short_repr(self):
        return f"{self.parentTypeObject.name}"
    
class FunctionInSystem(SystemElement):
    _ctryOption = ReadCountryOptions.SYS_FUN 
    def __init__(self,*arg):
        super().__init__(*arg)
        self.parameters = None

    def _short_repr(self):
        return f"{self.parentTypeObject.name}: {self.switch} \t {self.parentTypeObject.comment}" 

    def __getattribute__(self, name):
        if name == "parameters" and self.__dict__["parameters"] is None:
            self._load_parameters()
            return self.parameters
        return super().__getattribute__(name)
    def _load_parameters(self):
       self.parameters = Container()
       sys = self.parentSystem
       for par in self.parentTypeObject.parameters:
           id = sys.ID + par.ID
           syspar = self.parentSystem.parent._countryInfoHandler.GetPieceOfInfo(ReadCountryOptions.SYS_PAR,id)
           self.parameters.add(id,ParameterInSystem(syspar, id, sys, par))

class Extension(Euromod_Element):
    _objectType = ReadModelOptions.EXTENSIONS
    def __repr__(self):
        return f"Extension: {self.name}" 

    def _short_repr(self):
        return f"{self.shortName}" 


    

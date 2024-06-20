class Container:
    """
    This class is a container for objects that allow for indexing and representation in multiple ways:
    via keys that are the name of the objects 
    or via integer indexing as in a list.
    """
    def __init__(self):
        self.containerDict = {}
        self.containerList = []
    def add(self,key,value):
        self.containerDict[key] = value
        self.containerList.append(value)
    def _short_repr(self):
        if len(self) > 10:
            return f"{len(self)} elements"
        elif len(self) == 0:
            return "0 elements"
        else:
            rep = ""
            for i,el in enumerate(self):
                rep += f"{el._short_repr()}"
                if i < len(self)-1:
                    rep += ", "
        return rep
    def __repr__(self):
        s= ""
        for i,el in enumerate(self.containerList):
            s += f"{i}: {el._short_repr()}\n"
        return s
    def __getitem__(self,arg):
        if (type(arg) == int) | (type(arg) == slice):
            return self.containerList[arg]
        if type(arg) == str:
            return self.containerDict[arg]
        
    def __setitem__(self,k,v):
        if (type(k) == int) | (type(k) == slice):
            self.containerList[k] = v
            return
        if type(k) == str:
            self.containerDict[k] = v
            return
        
        raise(TypeError("Type of key is not supported"))
    def __iter__(self):
        return iter(self.containerList)
    def __len__(self):
        return len(self.containerList)
    def keys(self):
        return self.containerDict.keys()
    def items(self):
        return self.containerDict.items()
    def values(self):
        return self.containerDict.values()
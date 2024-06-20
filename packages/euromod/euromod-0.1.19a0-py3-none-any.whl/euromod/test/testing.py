# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:31:25 2024

@author: serruha
"""

## Testing output of different software versions ##
import sys
import time
import os
import pandas as pd
import numpy as np
sys.path.insert(0, r'C:\Users\iribe\EUROMOD_CONNECTOR\connector\Connectors\PythonIntegration\src')
import euromod as em
t = time.time()
model_path= r"C:\Users\iribe\WORK\EUROMOD\EUROMOD_RELEASES_I6.0+"
mod = em.Model(model_path)
outputpathmod = r"C:\Users\iribe\WORK\EUROMOD\EUROMOD_RELEASES_I6.0+\testing"
repository = r"C:\Users\iribe\WORK\EUROMOD\All countries"

mod["BE"]
mod["BE"][-1].policies[0]
mod["BE"][-1].policies[0].functions[0]
mod["BE"][-1].policies[0].functions[0].parameters[0]
mod["BE"].datasets
mod["BE"][-1].datasets
mod["BE"][-1].bestmatch_datasets #gets the bestmatch datasets
mod.extensions
mod["BE"].local_extensions
mod["BE"].policies
mod["BE"].policies[0].functions
mod["BE"].policies[0].functions[0].parameters

for el in [mod["BE"],
mod["BE"][-1].policies[0],
mod["BE"][-1].policies[0].functions[0],
mod["BE"][-1].policies[0].functions[0].parameters[0],
mod["BE"].datasets[0],
mod["BE"][-1].datasets[0],
mod.extensions[0],
mod["BE"].local_extensions[0],
mod["BE"].policies[0],
mod["BE"].policies[0].functions[0],
mod["BE"].policies[0].functions[0].parameters[0]]:
    print(f"Attributes of type {type(el)}")
    print(el.get_properties())
           






print(time.time() - t)


sysToRun = mod["BE"][-1]
dataset = sysToRun.bestmatch_datasets[-1].name
data = pd.read_csv(os.path.join(repository,dataset + ".txt"),sep="\t")
sim = sysToRun.run(data,dataset)
sim.outputs[0].ils_dispy.mean()
sim2 = sysToRun.run(data,dataset)
sim2.outputs[0].ils_dispy.mean()

taxunits = dict()
for pol in mod["BE"][-1].policies:
    for fun in pol.functions:
        for par in fun.parameters:
            if par.name == "TAX_UNIT":
                if not par.value in taxunits:
                    taxunits[par.value] = 1
                else:
                    taxunits[par.value] += 1
            

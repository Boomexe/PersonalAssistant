import os
from os.path import dirname, basename, splitext, join
import fnmatch

import inspect
import importlib.util

found_modules = []

def find_modules():
    for path, directory, files in os.walk(dirname(__file__)):
        for f in fnmatch.filter(files, "*.py"): # can use python .endswith() instead of this library
            if f not in __file__:
                module_name = basename(path)
                found_modules.append((module_name, files, path))

                print(f'Found module: {path}')

def load_module(module_name: str, *args):
    for module in found_modules:
        found_module_name = splitext(module[0])[0]
        
        if found_module_name == module_name:
            spec = importlib.util.spec_from_file_location(found_module_name, join(module[2], module[1][0])) # gets first file in directory, may cause issues? maybe..
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if len(inspect.signature(module.main).parameters) == 0:
                return module.main()
            
            return module.main(args)

# find_modules()
# load_module("jokes")
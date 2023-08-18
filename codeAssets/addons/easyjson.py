from json import load as jsonload, dump as jsondump

# open a json and return a dict
def GetDict(jsonFile:str): return jsonload(open(jsonFile, 'r'))

# write a dict to a json file
def Write(jsonFile:str, dict:dict): jsondump(dict, open(jsonFile,'w'))

# write that makes the json more readable for people
def FormatedWrite(jsonFile:str, dict:dict, indent:int=2): jsondump(dict, open(jsonFile,'w'), indent=indent)
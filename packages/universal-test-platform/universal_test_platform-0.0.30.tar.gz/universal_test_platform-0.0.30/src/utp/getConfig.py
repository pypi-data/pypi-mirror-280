import os
import yaml

def getConfig() -> dict[str, any]:
    with open(os.path.join(getRoot(),'/robot.yaml'), 'r') as f:
      data = yaml.load(f, Loader=yaml.SafeLoader)

    return data
     

def getCondaConfig() -> dict[str, any]:
    with open(os.path.join(getRoot(),'/conda.yaml'), 'r') as f:
      data = yaml.load(f, Loader=yaml.SafeLoader)

    return data
     

def getRoot():
    cwd = os.getcwd()
    
    if (not cwd) or cwd == "/":
        return os.path.abspath(os.curdir)
    
    return cwd
import os
import yaml

def getConfig() -> dict[str, any]:
    with open(getRoot()+'/robot.yaml', 'r') as f:
      data = yaml.load(f, Loader=yaml.SafeLoader)

    return data
     

def getCondaConfig() -> dict[str, any]:
    with open(getRoot()+'/conda.yaml', 'r') as f:
      data = yaml.load(f, Loader=yaml.SafeLoader)

    return data
     

def getRoot():
    cwd = os.getcwd()
    
    if not cwd:
        print(os.path.dirname(os.path.abspath(__file__)))
        return os.path.dirname(os.path.abspath(__file__))
    
    return cwd
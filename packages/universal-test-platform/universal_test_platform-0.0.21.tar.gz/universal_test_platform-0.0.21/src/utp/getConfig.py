import os
import yaml

def getConfig() -> dict[str, any]:
    with open(os.getcwd()+'/robot.yaml', 'r') as f:
      data = yaml.load(f, Loader=yaml.SafeLoader)

    return data
     

def getCondaConfig() -> dict[str, any]:
    with open(os.getcwd()+'/conda.yaml', 'r') as f:
      data = yaml.load(f, Loader=yaml.SafeLoader)

    return data
     
    
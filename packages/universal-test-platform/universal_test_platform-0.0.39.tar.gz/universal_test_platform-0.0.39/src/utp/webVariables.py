import os
from typing import Optional

def webVariables(remote: Optional[bool] = False):
    my_env = os.environ
    my_env['REMOTE'] = str(remote) if remote else ""
    
    return my_env
    
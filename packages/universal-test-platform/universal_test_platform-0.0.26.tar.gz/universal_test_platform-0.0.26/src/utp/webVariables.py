import os

def webVariables(remote: bool | None):
    my_env = os.environ
    my_env['REMOTE'] = str(remote) if remote else ""
    
    return my_env
    
import subprocess
from typing import IO, Optional

def getSubprocessOutput(process: subprocess.Popen[bytes]):

    def log_subprocess_output(pipe: Optional[IO[bytes]]):
        result= ""
        for line in iter(pipe.readline, b''): # b'\n'-separated lines
            a=result + line.decode("utf-8")
            result = a
            
        return result
    
    with process.stdout:
       appiumStatus= log_subprocess_output(process.stdout)
    process.wait() # 0 means success

    return appiumStatus





def readCommand(command):
# Run the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the output and errors
    stdout, stderr = process.communicate()


    return (stdout.decode(),stderr.decode())


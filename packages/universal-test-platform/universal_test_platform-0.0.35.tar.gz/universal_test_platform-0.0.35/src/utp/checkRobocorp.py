from enum import Enum
import os
import platform
import click

class OS(Enum):
    LINUX = "Linux"
    WINDOWS = "Windows"
    DARWIN = "Darwin"

def checkRobocorp():
    #check robocorp installed
    javaStatus = os.popen("rcc --version").read()
    if javaStatus.startswith("v") != True:
        if platform.system() == OS.LINUX:
            os.popen("""curl -o rcc https://downloads.robocorp.com/rcc/ /latest/linux64/rcc ;
                    chmod a+x rcc ;
                    mv rcc /usr/local/bin/ ;
                    """).read()
        elif platform.system() == OS.DARWIN:
            os.popen("""brew update ;
                    brew install robocorp/tools/rcc ;
                    """).read()
        elif platform.system() == OS.WINDOWS:
              click.secho("""
                    Open the command prompt
                    Download: curl -o rcc.exe https://downloads.robocorp.com/rcc/releases/latest/windows64/rcc.exe
                    Add to system path (https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10): Open Start -> Edit the system environment variables
                    Test: rcc
                    """,bg='black', fg='white')
              click.secho("Try again after rcc installed", bg='black', fg='yellow')
              
              exit(1)
        click.secho("rcc installed successfully", bg='black', fg='green')

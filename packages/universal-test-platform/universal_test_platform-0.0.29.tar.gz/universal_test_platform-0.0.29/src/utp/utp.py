import click
import time
import subprocess
from utp.webVariables import webVariables
from utp.syncVersion import syncVersion
from utp.appVariables import appVariables
from utp.checkADB import checkADB
from utp.checkAppium import checkAppium
from utp.checkJava import checkJava
from utp.checkNode import checkNode
from utp.checkRobocorp import checkRobocorp
from utp.checkRobotFramework import checkRobotFramework
from utp.clearArtifact import clearArtifact
from utp.localHub import runLocalHub
from utp.checkport import isPortUsed

syncVersion()

@click.group()
def cli():
    pass

@click.command()
@click.option('--remote', '-remote',  'remote', is_flag=True)
def web(remote):
    """Run test cases locally"""

    #check node installed
    checkNode()

    checkJava()
    
    hubHandler= None

    if not remote:
        hubHandler = runLocalHub()

    checkRobotFramework()

    checkRobocorp()

    clearArtifact()
    
    env = webVariables(remote)

    subprocess.Popen(["rcc", "run", "--task", "Web"],env=env).wait()
    
    if hubHandler is not None:
        hubHandler.kill()
    
        


@click.command()
@click.option('--android_app', '-aa', 'androidApp')
@click.option('--android_platform_version', '-apv', 'androidPlatformVersion')
@click.option('--remote', '-remote',  'remote', is_flag=True)
def app(androidApp, androidPlatformVersion, remote):
    """Run test cases locally"""

    #check node installed
    checkNode()
    
    checkADB()

    appiumHandler = None
    if not remote:
        appiumHandler= checkAppium()
        
    checkRobotFramework()

    checkRobocorp()

    clearArtifact()
    

    env = appVariables(androidApp, androidPlatformVersion, remote)
    
    subprocess.Popen(["rcc", "run", "--task", "App"],env=env).wait()
    if appiumHandler is not None:
        appiumHandler.kill()
    

# @click.command()
# @click.Choice()
cli.add_command(web)
cli.add_command(app)

if __name__ == '__main__':
    cli()
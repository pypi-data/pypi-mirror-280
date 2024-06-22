import subprocess
import os
import time

import click

from utp.checkport import isPortUsed

def runLocalHub():
      localHubIsRunning = isPortUsed(4444)
      if localHubIsRunning == True:
            click.secho("Hub already running", bg='black', fg='yellow')
            return None

            
      click.secho("running Hub Locally")
      handler= subprocess.Popen(["java", "-jar", os.path.dirname(__file__) + "/../setup/selenium-server-4.21.0.jar","standalone"],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)
      time.sleep(10)
      click.secho("Start Hub and Node standalone", bg='black', fg='green')

      return handler
    

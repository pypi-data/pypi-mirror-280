import os
import socket
import requests
from robot.libraries.BuiltIn import BuiltIn
from AppiumLibrary import AppiumLibrary

from utp.getConfig import getConfig

class utp():
    def __init__(self):
        pass
    
    def get_hub_url(self):

        try:
            # Create a socket and connect to an external server to get the local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 53))  # Connect to Google's DNS server
            ip = s.getsockname()[0]
            s.close()
        except Exception as e:
            ip = '127.0.0.1'  # Default to localhost in case of an error
            print(f"Error obtaining IP address: {e}")
        
        return ip

    def open_android_application(self):
        ANDROID_AUTOMATION_NAME = os.environ.get("ANDROID_AUTOMATION_NAME")
        ANDROID_APP = os.environ.get("ANDROID_APP")
        ANDROID_PLATFORM_NAME = os.environ.get("ANDROID_PLATFORM_NAME") 
        ANDROID_PLATFORM_VERSION = os.environ.get("ANDROID_PLATFORM_VERSION")
        REMOTE = True if os.environ.get("REMOTE") else False
        
        if REMOTE:
            ip = getConfig().get("server","").strip()
        else:
            ip = self.get_hub_url()
        
        remote_url = f'http://{ip}:4723/wd/hub'
        
        
        if not (ANDROID_PLATFORM_VERSION and ANDROID_PLATFORM_VERSION.strip()):
            try:
                r = requests.get(url = f'http://{ip}:4723/device-farm/api/device') 
                response = r.json() 
                print("readyDevices",response )
                
                def fullFill(item: dict):
                    if item.get('busy'):
                        return True
                    return False
                    
                readyDevices = filter(fullFill,response)
                ANDROID_PLATFORM_VERSION = readyDevices[0].get("sdk") or '11'
                print("readyDevices",readyDevices )
            except:
                ANDROID_PLATFORM_VERSION = '11'
        
        
        app_url = ANDROID_APP
        appium:AppiumLibrary = BuiltIn().get_library_instance('AppiumLibrary')
        
        appium.open_application(
            remote_url,
            automationName=ANDROID_AUTOMATION_NAME,
            platformName=ANDROID_PLATFORM_NAME,
            platformVersion=ANDROID_PLATFORM_VERSION,
            app=app_url,
            appPackage='com.digikala',
            appWaitActivity='*'
        )
        BuiltIn().sleep('5s')
        
    def get_android_platform_version(self):
        """First part of android platform version"""
        ANDROID_PLATFORM_VERSION = os.environ.get("ANDROID_PLATFORM_VERSION") 
        words = ANDROID_PLATFORM_VERSION.split(".")
        ver = int(words[0])
        
        return ver
        
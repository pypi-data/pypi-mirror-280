import os
import socket
import requests
from robot.libraries.BuiltIn import BuiltIn
from AppiumLibrary import AppiumLibrary
from SeleniumLibrary import SeleniumLibrary

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
            ANDROID_PLATFORM_VERSION = getAnAvailableDeviceSdk()

        if not ANDROID_PLATFORM_VERSION:
            raise Exception("There is no available devices")
        
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
    
    
    def open_chrome(self,url):

        REMOTE = True if os.environ.get("REMOTE") else False
        
        if REMOTE:
            ip = getConfig().get("server","").strip()
        else:
            ip = self.get_hub_url()
        
        remote_url = f'http://{ip}:4444/wd/hub'
        
        
        selenium:SeleniumLibrary = BuiltIn().get_library_instance('SeleniumLibrary')
        
        selenium.open_browser(
            remote_url= remote_url,
            url= url or "https://demo.digikala.com",
            browser= "chrome"
        )
        BuiltIn().sleep('5s')
        
    def get_android_platform_version(self):
        """First part of android platform version"""
        ANDROID_PLATFORM_VERSION = os.environ.get("ANDROID_PLATFORM_VERSION") 
        words = ANDROID_PLATFORM_VERSION.split(".")
        ver = int(words[0])
        
        return ver
    


def getAnAvailableDeviceSdk():
    availableSdk = None
    try:
        r = requests.get(url = f'http://172.20.74.25:4723/device-farm/api/device') 
        response = r.json() 
        
        availableSdks = []
        
        for x in response:
            busy = x['busy']
            userBlocked = x['userBlocked']
            offline = x['offline']
            sessionStartTime = x['sessionStartTime']
            
            if busy == False and userBlocked == False and offline == False and sessionStartTime == 0:
                availableSdks.append(x['sdk'])
        
        if availableSdks.__len__() > 0:
           availableSdk = availableSdks.pop()
    finally:
       return  availableSdk
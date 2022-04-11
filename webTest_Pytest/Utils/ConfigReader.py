import configparser
import os

directory = os.getcwd()

configFilePath=directory+"\\webTest_Pytest\\Resources\\config.properties"
config = configparser.ConfigParser()



class ConfigReader:
    def __init__(self,*args):
        if len(args)>0:
            config.read(args[0])  
        else:
            config.read(configFilePath)

    def get_url(self):
        return config["Application"]["url"]
    
    def get_username(self):
        return config["Application"]["username"]

    def get_password(self):
        return config["Application"]["password"]
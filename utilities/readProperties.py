import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo', 'url')
        return url
    @staticmethod
    def getApplicationEmail():
        email = config.get('commonInfo','email' )
        return email

    @staticmethod
    def getApplicationPWD():
        pwd = config.get('commonInfo', 'password')
        return pwd
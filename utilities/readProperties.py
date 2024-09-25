import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getMobileNumber():
        mobilenumber = config.get("common info", 'mobilenumber')
        return mobilenumber

    @staticmethod
    def getOtp():
        otp = config.get("common info", 'otp')
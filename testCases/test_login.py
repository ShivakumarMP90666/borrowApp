import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    #baseURL = ReadConfig.getApplicationURL()
    #mobilenumber = ReadConfig.getMobileNumber()
    #otp = ReadConfig.getOtp()
    baseURL = "https://borrow-3b1b3.web.app/"
    mobilenumber = "9738928926"
    otp = "123456"
    logger = LogGen.loggen()

    def test_homePage(self, setup):
        self.logger.info("**********Test_001_Login***********")
        self.logger.info("********Verifying Home Page Title**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(10)
        act_title = self.driver.title
        if act_title == "Borrow | Your needs":
            assert True
            self.logger.info("******** Login Page Title is Matched ***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("******** Home Page Title Test is Failed *********")

    def test_loginPage(self, setup):
        self.logger.info("******* Entering Details in Login Page ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setMobileNumber(self.mobilenumber)
        self.lp.clickOnSignIn()
        time.sleep(20)
        self.logger.info("******* Entering OTP ********")
        self.lp.setOtp(self.otp)
        self.lp.clickOnConfirmOtp()
        time.sleep(5)
        title = self.driver.title
        if title == "Borrow | Your needs":
            assert True
            self.logger.info("********* Home Page Title is Matched **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False

# code to add 2 numbers?








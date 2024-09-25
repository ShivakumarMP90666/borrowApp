import time

from pageObjects.LoginPage import LoginPage
from pageObjects.addItemHomePage import addItemHomePage
from utilities.customLogger import LogGen


class Test_004_addItem:
    baseURL = "https://borrow-3b1b3.web.app/"
    mobilenumber = "9738928926"
    otp = "123456"
    firstItemText = "Solomon Northup "
    logger = LogGen.loggen()

    def test_borrowNow(self, setup):
        self.logger.info("************* Test_002_Borrow_Now ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setMobileNumber(self.mobilenumber)
        self.lp.clickOnSignIn()
        time.sleep(30)
        self.lp.setOtp(self.otp)
        self.lp.clickOnConfirmOtp()
        time.sleep(3)
        self.addItem = addItemHomePage(self.driver)
        self.addItem.clickOnSearch()
        time.sleep(2)
        self.addItem.clicckOnAddPlusMark()
        time.sleep(2)
        self.addItem.enterItemName()
        time.sleep(5)
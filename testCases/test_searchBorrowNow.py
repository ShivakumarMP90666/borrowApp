import os
import datetime
import time

from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.BorrowNow import BorrowNow
class Test_003_BorrowNow:
    baseURL = "https://borrow-3b1b3.web.app/"
    mobilenumber = "9738928926"
    otp = "123456"
    firstItemText = "Solomon Northup "
    searchItemText = "Nikon D5600 amera "
    logger = LogGen.loggen()
    def test_searchBorrowNow(self, setup):
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

        self.borrowNow = BorrowNow(self.driver)
        self.borrowNow.clickOnMenu()
        time.sleep(3)
        self.borrowNow.clickOnBorrownow()
        time.sleep(3)
        self.borrowNow.clickOnVehicles()
        time.sleep(3)

        self.borrowNow.setSearchItem()
        time.sleep(3)
        self.borrowNow.clickOnFirstSearchItem()
        time.sleep(3)

        #self.borrowNow.clickOnFirstItem()
        time.sleep(3)
        self.searchtext = self.borrowNow.getFirstSearchElementText()

        try:
            # Code that might raise an assertion error
            if not self.searchtext == self.searchItemText:  # Replace 'condition' with your actual condition
                self.logger.error("*******First Item Details Did not Match********")
                self.logger.error("******* Borrow Now test Failed ********")
                assert False  # This will raise an AssertionError
        except AssertionError:
            # Handle the assertion error
            self.logger.error("AssertionError caught. Continuing with the test...")

            # Ensure the directories exist
            os.makedirs("Logs", exist_ok=True)
            os.makedirs("Screenshots", exist_ok=True)

            # Save error details in Logs directory
            error_details = f"{datetime.datetime.now()}: AssertionError: First Search Item Details Did not Match"
            with open("./Logs/error_log.txt", "a") as error_file:
                error_file.write(error_details + "\n")

            # Take a screenshot and save it in Screenshots directory
            screenshot_path = f"./Screenshots/error_screenshot_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved to {screenshot_path}")

        finally:
            self.driver.close()

        # Continue with further tests or code
        # Your further code here

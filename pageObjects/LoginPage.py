import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage:
    txt_mobileNumber_xpath = "//input[@id='ion-input-0']"
    btn_signIn_xpath = "//ion-button[@id='sign-in']"
    txt_enterOtp_xpath = "//input[@id='ion-input-1']"
    btn_confirmOtp_xpath = "//ion-button[contains(text(), 'Confirm OTP')]"
    HomePageTitle = "Borrow | Your needs"

    def __init__(self, driver):
        self.driver = driver

    def setMobileNumber(self, mobilenumber):
        #self.driver.find_element(By.XPATH, self.txt_mobileNumber_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_mobileNumber_xpath).send_keys(mobilenumber)

    def clickOnSignIn(self):
        self.driver.find_element(By.XPATH, self.btn_signIn_xpath).click()
        time.sleep(5)

    def setOtp(self, otp):
        self.driver.find_element(By.XPATH, self.txt_enterOtp_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_enterOtp_xpath).send_keys(otp)

    def clickOnConfirmOtp(self):
        self.driver.find_element(By.XPATH, self.btn_confirmOtp_xpath).click()






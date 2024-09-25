from selenium import webdriver
from selenium.webdriver.common.by import By


class addItemHomePage:
    btn_search_xpath = "//ion-button[@class='sc-ion-buttons-md ion-color ion-color-primary md button button-clear in-toolbar in-toolbar-color in-buttons button-has-icon-only ion-activatable ion-focusable hydrated']"
    btn_addPlus_xpath = "//ion-fab-button[@class='md ion-activatable ion-focusable hydrated']"
    txt_name_xpath = "//label[@for='ion-input-0']//div[@class='native-wrapper sc-ion-input-md sc-ion-input-md-s']"
    itemname = "Volley Ball"

    def __init__(self, driver):
        self.driver = driver

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def clicckOnAddPlusMark(self):
        self.driver.find_element(By.XPATH, self.btn_addPlus_xpath).click()

    def enterItemName(self):
        self.driver.find_element(By.XPATH, self.txt_name_xpath).send_keys(self.itemname)

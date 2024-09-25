from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class BorrowNow:
    btn_menu_xpath = "//ion-buttons[@class='buttons-first-slot sc-ion-buttons-md-h sc-ion-buttons-md-s md hydrated']"
    btm_borrowNow_xpath = "//ion-label[text()='Borrow Now']"
    btn_vehicles_xpath = "//div[@class='scroll-horizontal']//div[1]//div[1]//ion-avatar[1]"
    btn_firstItem = "(//ion-col[@class='scroll-item md hydrated'])[34]//ion-card"
    txt_itemName_xpath = "//h1[@class='itemName']"
    searchItemText = "Nikon D5600 camera "
    txt_search_xpath = "//input[@placeholder='Search']"
    btn_firstSearchElement_xpath = "(//ion-card[@class='md hydrated'])[35]"
    txt_firstSearchElement_xpath = "//h1[normalize-space()='Nikon D5600 camera']"
    def __init__(self, driver):
        self.driver = driver

    def clickOnMenu(self):
        self.driver.find_element(By.XPATH, self.btn_menu_xpath).click()

    def clickOnBorrowNow(self):
        self.driver.find_element(By.XPATH, self.btm_borrowNow_xpath).click()

    def clickOnVehicles(self):
        self.driver.find_element(By.XPATH, self.btn_vehicles_xpath).click()

    def clickOnFirstItem(self):
        self.driver.find_element(By.XPATH, self.btn_firstItem).click()

    def  getFirstItemText(self):
        self.text = self.driver.find_element(By.XPATH, self.btn_firstItem).text
        return self.text

    def clickOnBorrownow(self):
        element = self.driver.find_element(By.XPATH, self.btm_borrowNow_xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def setSearchItem(self):
        self.element = self.driver.find_element(By.XPATH, self.txt_search_xpath)
        self.element.send_keys("Nikon")
        self.element.send_keys(Keys.ENTER)

    def clickOnFirstSearchItem(self):
        self.driver.find_element(By.XPATH, self.btn_firstSearchElement_xpath).click()

    def getFirstSearchElementText(self):
        self.searchText = self.driver.find_element(By.XPATH, self.txt_firstSearchElement_xpath).text
        return self.searchText


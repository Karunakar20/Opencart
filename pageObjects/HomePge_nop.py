from selenium.webdriver.common.by import By


class Homepage():
    lnk_register_xpath = "//a[normalize-space()='Register']"
    lnk_login_xpath = "//a[normalize-space()='Log in']"


    def __init__(self,driver):
        self.driver = driver


    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.lnk_register_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.lnk_login_xpath).click()
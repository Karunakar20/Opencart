from selenium.webdriver.common.by import By


class Login:
    txt_email_xpath="//input[@id='Email']"
    txt_pwd_xpath ="//input[@id='Password']"
    btn_login_xpath ="//button[normalize-space()='Log in']"
    var_btn_xpath = "//a[normalize-space()='Log out']"

    def __init__(self,driver):
        self.driver = driver

    def sendEmai(self,email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)
    def sendPwd(self,pwd):
        self.driver.find_element(By.XPATH, self.txt_pwd_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def textVer(self):
        try:
            return self.driver.find_element(By.XPATH, self.var_btn_xpath).is_displayed()
        except:
            return False
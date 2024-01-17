from selenium.webdriver.common.by import By


class Register():
    rad_gender_xpath = "//*[@id='gender']/span[1]/label"
    txtbox_firstName_xpath = "//input[@id='FirstName']"
    txtbox_lastName_xpath = "//input[@id='LastName']"
    txtbox_email_xpath = "//input[@id='Email']"
    txtbox_pwd_xpath = "//input[@id='Password']"
    txtbox_conpwd_xpath = "//input[@id='ConfirmPassword']"
    btn_register_xpath = "//button[@id='register-button']"
    confirmtext_xpath = "//div[@class='result']"

    def __init__(self, driver):
        self.driver = driver


    def setGender(self):
        self.driver.find_element(By.XPATH, self.rad_gender_xpath).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txtbox_firstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH, self.txtbox_lastName_xpath).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH, self.txtbox_pwd_xpath).send_keys(pwd)

    def setConfirPassword(self,cpwd):
        self.driver.find_element(By.XPATH, self.txtbox_conpwd_xpath).send_keys(cpwd)

    def setContinue(self):
        self.driver.find_element(By.XPATH, self.btn_register_xpath).click()

    def setConfirmtext(self):
        try:
            return self.driver.find_element(By.XPATH, self.confirmtext_xpath).text
        except:
            None


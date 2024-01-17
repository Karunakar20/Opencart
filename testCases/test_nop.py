import time
from datetime import datetime

import pytest

from pageObjects.HomePge_nop import Homepage
from pageObjects.Register_nop import Register
from utilities import randomString
import os
from utilities.readProperties import ReadConfig



class TestRegister:

    url = ReadConfig.getApplicationURL()


    @pytest.mark.regression
    def test_register(self,setup):
        self.driver = setup
        self.driver.get(self.url)



        self.driver.maximize_window()

        self.home = Homepage(self.driver)
        self.home.clickRegister()

        self.reg = Register(self.driver)
        self.reg.setGender()
        self.reg.setFirstName("Karunakar")
        self.reg.setLastName("Chavadam")
        self.email_ran=randomString.random_string_generator()+"@gmail.com"
        self.reg.setEmail(self.email_ran)
        # time.sleep(5)
        self.reg.setPassword("12345678")
        self.reg.setConfirPassword("123456789")
        self.reg.setContinue()
        self.message=self.reg.setConfirmtext()


        if self.message == "Your registration completed":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+"_test_register.png")
            assert False



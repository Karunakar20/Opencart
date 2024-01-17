import os
import time
from datetime import datetime

import pytest

from utilities.readProperties import ReadConfig
from pageObjects.HomePge_nop import Homepage
from pageObjects.LoginPage_nop import Login


class Test_Login:
    url = ReadConfig.getApplicationURL()
    email = ReadConfig.getApplicationEmail()
    pwd = ReadConfig.getApplicationPWD()


    @pytest.mark.sanity
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.hp = Homepage(self.driver)
        self.hp.clickLogin()

        self.login = Login(self.driver)
        self.login.sendEmai(self.email)
        self.login.sendPwd(self.pwd)
        self.login.clickLogin()
        self.btn_dis = self.login.textVer()

        if self.btn_dis == True:
            assert True
        else:
            assert False




import webbrowser
import pytest

from TestCases.conftest import setup
from PageObjects.LoginPage import Login
from Utillities.ReadProperties import ReadConfig
from  Utillities.CustomLogger import LogGen
class TestLogin001():
    url = ReadConfig.getUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_Login(self,setup):
        TestLogin001.logger.info("****************** Test Login 001 *********************")
        TestLogin001.logger.info("*************** Test Login ***************")

        self.driver = setup
        self.driver.get(TestLogin001.url)
        self.driver.maximize_window()

        lg = Login(self.driver)
        lg.setUserName(TestLogin001.username)
        lg.setPassword(TestLogin001.password)
        lg.clickOnLogin()

        if lg.checkProduct() == True:
            TestLogin001.logger.info("****************** Login Successful 001 ********************")
        else:
            self.driver.save_screenshot("D:\\Project\\SeleniumHandsonProject\\Screenshots\\LoginTestFailed.png")
            TestLogin001.logger.error("******************** Login Failed 001 *************************")

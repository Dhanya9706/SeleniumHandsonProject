import time
import webbrowser
import pytest

from TestCases.conftest import setup
from PageObjects.LoginPage import Login
from Utillities.ReadProperties import ReadConfig
from  Utillities.CustomLogger import LogGen
from Utillities.XlUtills import ExcelUtills

class TestLogin001():
    url = ReadConfig.getUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    path = "D:\Project\SeleniumHandsonProject\TestData\TestLogin.xlsx"

    @pytest.mark.regression
    def test_Login(self,setup):
        TestLogin001.logger.info("****************** Test Login 001 *********************")
        TestLogin001.logger.info("*************** Test Login ***************")
        self.driver = setup

        self.rows = ExcelUtills.getRowCount(TestLogin001.path,'Input')
        for r in range(2,self.rows+1):
            self.driver.get(TestLogin001.url)
            self.driver.maximize_window()
            lg = Login(self.driver)
            lg.setUserName(ExcelUtills.readData(TestLogin001.path,'Input',r,1))
            lg.setPassword(ExcelUtills.readData(TestLogin001.path,'Input',r,2))
            lg.clickOnLogin()
            time.sleep(5)
            if lg.checkProduct() == True and ExcelUtills.readData(TestLogin001.path,'Input',r,3) == 'Pass':
                ExcelUtills.writeData(TestLogin001.path,'Input',r,4,'Pass')
                ExcelUtills.fillGreenColour(TestLogin001.path, 'Input', r, 4)
                TestLogin001.logger.info("****************** Login Successful ********************")
            else:
                ExcelUtills.writeData(TestLogin001.path, 'Input', r, 4, 'Fail')
                ExcelUtills.fillRedColour(TestLogin001.path, 'Input', r, 4)
                self.driver.save_screenshot("D:\\Project\\SeleniumHandsonProject\\Screenshots\\LoginTestFailed.png")
                TestLogin001.logger.error("******************** Login Failed *************************")
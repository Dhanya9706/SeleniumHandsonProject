from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:

    textbox_username_id = 'user-name'
    textbox_password_id = 'password'
    button_login_id = 'login-button'
    title_product_xpath = '//*[@id="header_container"]/div[2]/span'

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,Login.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,Login.textbox_password_id).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element(By.ID,Login.button_login_id).click()

    def checkProduct(self):
        try:
            if self.driver.find_element(By.XPATH,Login.title_product_xpath).is_displayed():
                return True
        except:
            return False
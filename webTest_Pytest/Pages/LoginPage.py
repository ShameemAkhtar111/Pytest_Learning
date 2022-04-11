from selenium.webdriver.common.by import By


from framework.ElementFunctions import ElementFunctions
from Utils.ConfigReader import ConfigReader as reader

USERNAME = (By.ID,"txtUsername")
PASSWORD = (By.ID,"txtPassword")
LOGIN_BTN = (By.ID,"btnLogin")

class LoginPage(ElementFunctions):

    def __init__(self, driver):
        super().__init__(driver)
    
    def launch_orangehrm(self):
        self.driver.get(reader().get_url())

    def enter_username(self,usrname):
        self.set_text(USERNAME,usrname)
    
    def enter_password(self,pwd):
        self.set_text(PASSWORD,pwd)
    
    def login(self,usr_nm,passwrd):
        self.enter_username(usr_nm)
        self.enter_password(passwrd)
        self.click_element(LOGIN_BTN)


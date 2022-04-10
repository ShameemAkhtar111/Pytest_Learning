import sys
sys.path.append("D:\\Shameem\\SeleniumPython\\Pytest_Learning")
sys.path.append("D:\\Shameem\\SeleniumPython\\Pytest_Learning\\webTest_Pytest")

from Pages.LoginPage import LoginPage

from framework.TestSetup import Base
from Utils.ConfigReader import ConfigReader as reader



class Test_Login(Base):

    def test_login_to_orangehrm(self):
        self.loginPage = LoginPage(self.driver)
        # self.loginPage.launch_orangehrm()
        self.loginPage.login(reader.get_username(),reader.get_password())
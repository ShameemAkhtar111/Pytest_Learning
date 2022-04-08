from time import sleep
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver2")
class BaseTest:
    pass

class Test_Iengage(BaseTest):
    @pytest.mark.parametrize(
                            "username,password",
                            [('78877','Apr@cfg1')]
                            )
    def test_iengage_login(self,username,password):
        self.driver.get("https://iengage.coforge.com")
        assert self.driver.title == "Login", "Page not loaded successfully"
        self.driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
        assert self.driver.find_element(By.XPATH,"(//h1[contains(text(),'Engage with the Emerging')])[2]").text == "Engage with the Emerging", "Not found 'Engage with the Emerging'"
        self.driver.find_element(By.ID,"txtEmpCode").send_keys(username)
        self.driver.find_element(By.ID,"txtPassword").send_keys(password)
        self.driver.find_element(By.ID,"imgBtnOK").click()
        sleep(2)

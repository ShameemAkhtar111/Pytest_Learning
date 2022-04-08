from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


@pytest.fixture(params=["chrome","edge"],scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param == "edge":
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    # request.cls.driver declares class level variable named "driver"
    request.cls.driver = web_driver

    yield
    web_driver.quit()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("https://www.google.co.in")
        assert self.driver.title == "Google"
    

    def test_fb_title(self):
        self.driver.get("https://facebook.com")
        assert self.driver.title == "Facebook – log in or sign up"
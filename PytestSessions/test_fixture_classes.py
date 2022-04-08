from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


@pytest.fixture(scope="class")
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    # request.cls.driver declares class level variable named "driver"
    request.cls.driver = ch_driver

    yield
    ch_driver.quit()

@pytest.fixture(scope="class")
def init_edge_driver(request):
    edge_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    request.cls.driver = edge_driver

    yield
    edge_driver.quit()

@pytest.mark.usefixtures("init_chrome_driver")
# above statement is using class level fixture
class Base:
    pass

# Test_Google_Chrome is extended from Base class
class Test_Google_Chrome(Base):

    def test_google_title(self):
        # since request.cls.driver is declared in class level fixture, variable 'driver' can be used directly
        self.driver.get("https://www.google.co.in")
        assert self.driver.title == "Google"

@pytest.mark.usefixtures("init_edge_driver")
class Base_ff:
    pass

class Test_Google_Edge(Base_ff):

    def test_google_title(self):
        self.driver.get("https://www.google.co.in")
        assert self.driver.title == "Google"
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

@pytest.fixture(scope="class")
def init_driver2(request):
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    web_driver.maximize_window()
    web_driver.implicitly_wait(20)
    # request.cls.driver declares class level variable named "driver"
    request.cls.driver = web_driver

    yield
    web_driver.quit()
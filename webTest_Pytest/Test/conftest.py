import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def init_driver(request):
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    web_driver.maximize_window()
    web_driver.implicitly_wait(20)
    request.cls.driver = web_driver

    yield
    web_driver.quit()
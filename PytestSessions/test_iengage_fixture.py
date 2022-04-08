from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import  pytest

driver = None

@pytest.fixture(scope="module")
def init_driver():
    print("----------------setup----------------------------")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    driver.get("https://iengage.coforge.com/")

# yield is for teardown
    yield
    print("----------------teardown----------------------------")
    driver.quit()

    
@pytest.mark.usefixtures("init_driver")
# either use the above line or pass fixture name as a parameter in the test function example "def test_iengage(init_driver):"
def test_iengage():
    assert driver.title == "Login", "Page not loaded successfully"
    driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
    assert driver.find_element(By.XPATH,"(//h1[contains(text(),'Engage with the Emerging')])[2]").text == "Engage with the Emerging", "Not found 'Engage with the Emerging'"

@pytest.mark.usefixtures("init_driver")
def test_iengage_url():
    assert driver.current_url == "https://iengage.coforge.com/ess1/Authentication/LoginAuth.aspx?_a=AB7DE28B-872B-4B3F-B2A0-C9F5E7E52A99"
    
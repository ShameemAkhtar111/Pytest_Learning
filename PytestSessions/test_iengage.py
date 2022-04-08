from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    driver.get("https://iengage.coforge.com/")

def teardown_module(module):
    driver.quit()

def test_iengage():
    assert driver.title == "Login", "Page not loaded successfully"
    driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
    assert driver.find_element(By.XPATH,"(//h1[contains(text(),'Engage with the Emerging')])[2]").text == "Engage with the Emerging", "Not found 'Engage with the Emerging'"
   
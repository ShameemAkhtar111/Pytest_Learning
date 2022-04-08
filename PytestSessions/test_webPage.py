from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_iengage():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    driver.get("https://iengage.coforge.com/")
    assert driver.title == "Login", "Page not loaded successfully"
    driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
    assert driver.find_element(By.XPATH,"(//h1[contains(text(),'Engage with the Emerging')])[2]").text == "Engage with the Emerging", "Not found 'Engage with the Emerging'"
    # driver.find_element("//input[@id='btnLogin']").click()
    driver.quit()

def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    driver.get("https://www.google.co.in/")
    assert driver.title=="Google"
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    driver.get("https://www.facebook.com/")
    assert driver.title=="Facebook – log in or sign up"
    driver.quit()
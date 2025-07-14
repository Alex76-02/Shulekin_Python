from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().
                                                  install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

input_username = driver.find_element(By.CSS_SELECTOR, "#username")
input_password = driver.find_element(By.CSS_SELECTOR, "#password")
input_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
input_username.send_keys("tomsmith")
input_password.send_keys("SuperSecretPassword!")
input_button.click()
message = driver.find_element(By.CSS_SELECTOR, '[data-alert=""]')
print_message = message.text.strip("×")
print(print_message)
sleep(5)
driver.quit()

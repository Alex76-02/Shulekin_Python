from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/")
driver.get("https://vk.com/")
#driver.set_window_size(640, 460)
driver.maximize_window()
sleep(10)
driver.minimize_window()
sleep(10)
driver.fullscreen_window()
sleep(10)
driver.save_screenshot("./ya.png")
#for x in range(1, 10):
#	driver.back()
#	driver.forward()
#driver.refresh()    

sleep(20) #установили «засыпание» браузера на 50 секунд
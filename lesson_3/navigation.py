import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://yandex.ru")

time.sleep(10)

driver.back()

time.sleep(3)

driver.forward()

time.sleep(3)

driver.refresh()

time.sleep(3)
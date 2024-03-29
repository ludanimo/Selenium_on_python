import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")

ELEMENT = driver.find_element("class name", "wikipedia-icon")
print("Иконка Wikipedia:", ELEMENT)

ELEMENT_2 = driver.find_element("id", "Wikipedia1_wikipedia-search-input")
print("Поле ввода Wikipedia:", ELEMENT_2)

ELEMENT_3 = driver.find_element("class name", "wikipedia-search-button")
print("Кнопка поиска Wikipedia:", ELEMENT_3)

ELEMENT_4 = driver.find_element("id", "name")
print("Поле ввода Name:", ELEMENT_4)

time.sleep(3)
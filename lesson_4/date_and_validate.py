import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# driver.get("https://www.wikipedia.org/")
#
# # PAGE_URL = driver.current_url
# # print("URL страницы", PAGE_URL)
# # assert PAGE_URL == "https://www.wikipedia.org/", "Ошибка в URL"
# #
# # PAGE_TITLE = driver.title
# # print("Текущий заголовок:", PAGE_TITLE)
# # assert PAGE_TITLE == "Wikipedia", "Некорректный заголовок страницы"
#
# PAGE_SOURCE = driver.page_source
# print(PAGE_SOURCE)

driver.get("https://dzen.ru/")

PAGE_TITLE = driver.title
print("Текущий заголовок:", PAGE_TITLE)

driver.get("https://www.youtube.com/")

PAGE_TITLE_2 = driver.title
print("Текущий заголовок:", PAGE_TITLE_2)

driver.back()

PAGE_TITLE_3 = driver.title
assert PAGE_TITLE_3 == "Дзен", "Некорректный заголовок страницы"

driver.refresh()

PAGE_URL = driver.current_url
print("URL страницы:", PAGE_URL)

driver.forward()

PAGE_FORWARD = driver.current_url
assert PAGE_FORWARD == "https://www.youtube.com/", "Не тот URL"


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import requests
import pickle
options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
port = 8888
driver = webdriver.Chrome(executable_path='chromedriver',options=options, port=port)

for cookie in pickle.load(open(f"cookies.pkl", "rb")):
    driver.add_cookie(cookie)
sleep(2)


driver.get(f'https://www.instagram.com/mn_tezy/followers/')
sleep(4)
driver.refresh()
sleep(4)
print(driver.page_source)

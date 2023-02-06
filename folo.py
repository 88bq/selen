from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import requests
import telebot
import pickle
bot = telebot.TeleBot('1601467114:AAEQhSKTf8pSbSBFcSkG-KzDPlYZONee0X8')


options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
port = 8888
driver4 = webdriver.Chrome(executable_path='chromedriver', port=port)
driver4.get(f'https://www.instagram.com/888.zip/following/')
sleep(4)

for cookie in pickle.load(open(f"p_cr_.pkl", "rb")):
    driver4.add_cookie(cookie)
sleep(2)
driver4.get(f'https://www.instagram.com/888.zip/following/')
sleep(5)
ii = 0
x = bot.send_message('1382680308', f'Time  => Start')
while True:
    i = 1
    while i < 12:
        u = driver4.find_element_by_xpath(f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div[3]/button')
        if 'Following' in u.text or 'Folgend' in u.text:
            u.click()
            sleep(3)
            driver4.find_element_by_xpath(
                '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]').click()
            bot.edit_message_text(f'UNfollo => {i} //  {ii}', '1382680308', x.message_id)
        else:
            u.click()
            bot.edit_message_text(f'follo => {i} //  {ii}', '1382680308', x.message_id)
        sleep(35)
        i += 1
    ii += 1
    if ii == 4:
        ii = 0
        s = 0

        while s < 50 * 60:

            bot.edit_message_text(f'Time => {s}', '1382680308', x.message_id)
            s += 1


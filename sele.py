from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests

options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
port = 8888 # or any other available port



#driver3 = webdriver.Chrome(executable_path="driver/chromedriver.exe")
user = 'zxcv.kis'
pas = 'ahmedcan3'
user1 = []
check1 = ['magedbmw29']

def check(use):
    url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
    #user1 = open('kok.txt', 'r').read().split('\n')

    data = {
        'email':f'{use}@gmail.com',
        'username': 'jkjrjgkkdgd',
            'first_name':'koky',
    'opt_into_one_tap':'false',
    }
    head = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '55',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'datr=5WvSYy7FPvL1yCXXUNnrIUR7; csrftoken=eniA5Uj1P2k1kMzrfuSTZjkTzthjJD8I; mid=Y9Jr8wALAAF8wJLzi7GSWgm1PCal; ig_did=6E2F1F10-2048-4C38-ACF3-3F8301A2D440; ig_nrcb=1',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'viewport-width': '479',
        'x-asbd-id': '198387',
        'x-csrftoken': 'eniA5Uj1P2k1kMzrfuSTZjkTzthjJD8I',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1006866983',
        'x-requested-with': 'XMLHttpRequest',
    }
    q = requests.post(url, data=data, headers=head).json()['errors']

    try:
        z = q['email']
        print(use)
        open('gmail.txt', 'a', encoding='utf-8').write(use + '@gmail.com' + '\n')

    except:
        pass

def users(x):

    #x = open('kok.txt', 'r', encoding='utf-8').read()
    use = x.split("'s profile picture")
    for i in use:
        user1.append( i.split('img alt="')[-1])


driver4 = webdriver.Chrome(executable_path='chromedriver',options=options, port=port)


def login(user, pas):
    driver4.get("https://www.instagram.com/accounts/login/")
    sleep(3)
    username_input = driver4.find_element_by_name("username")
    password_input = driver4.find_element_by_name("password")
    username_input.send_keys(user)
    password_input.send_keys(pas)
    password_input.submit()
    sleep(8)
    print('[+] Done Login')
    read_aloud('Done Login ')


def get_user(u, t):
    r = -3
    #u = open('user3.txt', 'r').read().split('\n')[r]
    driver4.get(f'https://www.instagram.com/{u}/followers/')
    sleep(4)
    a = 0
    while a < t/12:
        try:

            following_panel = driver4.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
            ht = driver4.execute_script(""" 
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight; """, following_panel)
            sleep(2)
        except:
            pass
        a += 1

    try:

        x = driver4.page_source
        #user = str(x).split('aria-disabled="false"')
        i = 1
        while True:
            user11 = x.split('img alt="')[i].split("'s profile")[0]
            users(user11)
            i += 1
    except:
        pass


def gml():
    
    driver = webdriver.Chrome(executable_path='chromedriver',options=options, port=port)
    
    print('Search about gmail ...')

    driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp')
    for i in user1:
        if 'profile picture' in i or '_' in i or ' ' in i or len(i) < 5:
            pass
        else:
            driver.find_element_by_css_selector('#username').click()
            driver.find_element_by_css_selector('#username').send_keys(i)
            driver.find_element_by_css_selector('#firstName').click()
            sleep(3)
            u = driver.find_element_by_css_selector('#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.akwVEf.OcVpRe > div.d2CFce.cDSmF.OcVpRe > div > div.LXRPh').text
            sleep(1)
            print(u)
            if 'اسم المستخدم هذا مستخدم بالفعل. جرّب اسم مستخدم آخر' in u:
                pass
            else:
                check(i)

            driver.refresh()

    driver.delete_all_cookies()


login('zxcv.kis', 'ahmedcan3')

while True:
    try:
        
        u = input('User Target =>')
        no = input('No. of Followers => ')
        get_user(u, int(no))
        gml()
    except:
        pass

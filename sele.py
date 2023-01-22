from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# Start a web driver (e.g. Chrome) and log in to Instagram
users = []
driver = webdriver.Chrome('driver/chromedriver.exe')
driver.get("https://www.instagram.com/accounts/login/")
sleep(3)
username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")
username_input.send_keys("zxcv.kis")
password_input.send_keys("ahmedcan3")
password_input.submit()
sleep(8)
print('[+] Done Login')
# Go to the target user's profile
driver.get("https://www.instagram.com/mn_tezy/")
sleep(10)
# Click on the following button
following_button = driver.find_element_by_xpath('//a[@href="/mn_tezy/followers/"]')
following_button.click()
sleep(4)
try:
    popup = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
    a = 0
    try:
        while a < 3:
            sleep(3)
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
            a += 1
        x = driver.page_source
        user = str(x).split('aria-disabled="false"')
        i = 4
        open('user1.txt', 'w').write('')
        while True:
            z = user[i].split('href="/')[1]
            z = z[:z.find('/')]
            open('user1.txt', 'a', encoding='utf-8').write(z + '\n')

            img = x.split('img alt="')
            hh = 0
            for h in img:
                if z in h:
                    try:
                        driver.find_element_by_xpath(f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{hh - 10}]/div[1]/div/div').click()
                        sleep(15)
                        driver.find_element_by_class_name(
                            '_abl-')

                        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[3]/div/div/div[2]/span/button').click()
                        sleep(1)
                        print(f'[+] Done Like => {z}')
                        driver.back()
                        sleep(5)
                    except:
                        pass

                else:
                    pass
                hh += 1
            i += 1

    except:
        pass
except:
    pass
# Wait for the following modal to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']")))

# Scrape the users the target user is following
following_list = driver.find_elements_by_css_selector("#mount_0_0_r0 > div > div > div > div:nth-child(4) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1)")
following = [user.text for user in following_list]
print(following)

# Close the web driver
driver.close()

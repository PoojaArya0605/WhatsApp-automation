from selenium import webdriver
import time,sys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC




def new_chat(user_name):
    new_chat=chrome_browser.find_element_by_xpath('//div[@class="_3qx7_"]')
    new_chat.click()

    new_user=chrome_browser.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    new_user.send_keys(user_name)
    time.sleep(6)
    try:
        user=chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException as se:
        print(se)
        print("given user {} not found!".format(user_name))
    except Exception as e:
        chrome_browser.close()
        print(e)
        sys.exit()

chrome_browser=webdriver.Chrome()
chrome_browser.get('https://web.whatsapp.com/')

        

time.sleep(15)

print("Scanning is complete!")
WebDriverWait(chrome_browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "_3qx7_")))
user_name_list=['Hema 1111','Whatsapp bot', 'Ketan', 'Bharti']
for user_name in user_name_list:
    try:
        user=chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        new_chat(user_name)
        
    message_box=chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
    message_box.send_keys("Hey, I am your whatsapp bot..")

    message_box=chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
    message_box.click()
                              





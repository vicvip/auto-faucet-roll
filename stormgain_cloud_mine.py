from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
from io import BytesIO
import uuid
import re
import pytesseract
import random
import time
from datetime import datetime
from PIL import ImageOps

chrome_options = Options()
driver = webdriver.Chrome()

#Login to Stormgain
driver.get("https://app.stormgain.com/#modal_login")


def cloud_mine(driver):
    driver.get("https://app.stormgain.com/crypto-miner/")
    time.sleep(30)
    driver.switch_to.default_content()
    driver.switch_to.frame(0)
    time.sleep(3)
    try:
        btn = driver.find_element_by_css_selector("body > div:nth-child(3) > div:nth-child(2) > div > button")
        print(btn)
        btn.click()
    except:
        btn = driver.find_element_by_css_selector("body > div:nth-child(4) > div:nth-child(2) > div > button")
        print(btn)
        btn.click()


def auto_roll(i=0, driver=driver):
    random_sec = random.randint(3650,4000)
    time.sleep(random_sec)
    nw = datetime.now()
    driver.refresh()
    i = i + 1
    print(f'Refreshing page at {nw}, i is at {i}')
    if i == 4:
        print(f'Cloud mining at {nw}')
        cloud_mine(driver)
        i = 0
    auto_roll(i=i, driver=driver)


def quick_roll(driver=driver):
    random_sec = random.randint(1,2)
    time.sleep(random_sec)
    nw = datetime.now()
    driver.refresh()
    print(f'Cloud mining at {nw}')
    cloud_mine(driver)

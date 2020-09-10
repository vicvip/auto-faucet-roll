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
driver.get("https://app.stormgain.com/#modal_login")

#Login to Stormgain


def cloud_mine():
    driver.switch_to.default_content()
    driver.switch_to.frame(0)
    time.sleep(3)
    driver.find_element_by_css_selector("body > div:nth-child(3) > div:nth-child(2) > div > button").click()

def auto_roll(i=0, driver=driver):
    random_sec = random.randint(3650,4000)
    time.sleep(random_sec)
    nw = datetime.now()
    driver.refresh()
    print(f'Refreshing page at {nw}')
    if i == 3:
        print(f'Cloud mining at {nw}')
        cloud_mine()
        i = 0
    auto_roll(i=i, driver=driver)

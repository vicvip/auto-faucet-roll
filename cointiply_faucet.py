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
chrome_options.add_extension(r'D:\Crypto Related\auto-faucet-roll\chromeaudiocapture.crx')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://cointiply.com/home?intent=faucet")

#login....

driver.get("https://cointiply.com/home?intent=faucet")
time.sleep(3)

driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button').click()
time.sleep(3)

def cointiply_faucet(i=0):
    if i == 0:
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button').click()
    if i == 20:
        return
    time.sleep(5)
    png = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[1]/div[1]').screenshot_as_png
    border = (0, 20, 0, 0)
    im = Image.open(BytesIO(png)).convert('LA')
    guid = uuid.uuid4().hex
    ImageOps.crop(im, border).save(f'D:\Crypto Related\Cointiply\{guid}.png')
    time.sleep(2)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    captcha = pytesseract.image_to_string(f'D:\Crypto Related\Cointiply\{guid}.png')
    captcha = captcha.replace('\n\x0c', '')
    captcha = captcha.replace('\n', ' ')
    captcha = captcha.replace('|', '')
    regex = r'[^\w\- \'\,\.\?\!]'
    abnormality_found = 0
    for abnormality in re.findall(regex, captcha):
        abnormality_found = abnormality_found + 1
    if len(captcha) < 6 or abnormality_found > 0:
        driver.find_element_by_xpath('//*[@id="adcopy-link-refresh"]').click()
        print(f'Abnormality or length not satisfied! "{captcha.strip()}" cant solve {guid}.')
        i = i + 1
        cointiply_faucet(i)
        return
    else:
        try:
            input = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input')
            input.send_keys(captcha.strip())
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button').click()
        except:
            print(f'Cant find the input box! Skipping "{captcha.strip()}" for {guid}. Lets try again...')
            driver.find_element_by_xpath('//*[@id="adcopy-link-refresh"]').click()
            i = i + 1
            cointiply_faucet(i)
            return
    time.sleep(25)
    try:
        success = driver.find_element_by_xpath("//div[contains(., 'Claim Again In')]")
    except:
        print(f'Damn it! "{captcha.strip()}" wasnt accepted for {guid}. Retrying...')
        driver.find_element_by_xpath('//*[@id="adcopy-link-refresh"]').click()
        i = i + 1
        cointiply_faucet(i)
        return
    print(f'Claim success! "{captcha.strip()}" was accepted for {guid}.')


def auto_roll():
    random_sec = random.randint(3650,4000)
    time.sleep(random_sec)
    nw = datetime.now()
    if nw.hour <= 5:
        driver.refresh()
        print(f'Skipping Roll since time is at {nw}')
    else:
        print(f'Rolling Cointiply! at {nw}')
        cointiply_faucet(0)
    driver.minimize_window()
    auto_roll()
    

def auto_roll2(driver):
    random_sec = random.randint(3650,4000)
    time.sleep(random_sec)
    nw = datetime.now()
    if nw.hour <= 5:
        driver.refresh()
        print(f'Skipping Roll since time is at {nw}')
    else:
        print(f'Rolling Cointiply! at {nw}')
        driver.refresh()
        time.sleep(3)
        driver.maximize_window()
        cointiply_faucet(0)
        driver.minimize_window()
    auto_roll2(driver)
    

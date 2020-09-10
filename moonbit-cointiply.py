from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image, ImageEnhance, ImageOps
from io import BytesIO
import uuid
import re
import pytesseract
import random
import time
from datetime import datetime
from PIL import ImageOps
import pyperclip
import os
import speech_recognition as sr
import subprocess

chrome_options = Options()
chrome_options.add_extension(r'D:\Crypto Related\auto-faucet-roll\chromeaudiocapture.crx')
chrome_options.add_extension(r'D:\Crypto Related\auto-faucet-roll\ublock.crx')

#Navigate to Moonbit manually, change Chrome Record Audio Ext to save in .WAV format
driver_m_1 = webdriver.Chrome(options=chrome_options)
driver_c = webdriver.Chrome()
driver_c.get("https://cointiply.com/home?intent=faucet")


def cointiply_faucet(i=0):
    if i == 0:
        driver_c.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button').click()
    if i == 20:
        return
    time.sleep(5)
    png = driver_c.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[1]/div[1]').screenshot_as_png
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
        driver_c.find_element_by_xpath('//*[@id="adcopy-link-refresh"]').click()
        print(f'Abnormality or length not satisfied! "{captcha.strip()}" cant solve {guid}.')
        i = i + 1
        cointiply_faucet(i)
        return
    else:
        try:
            input = driver_c.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input')
            input.send_keys(captcha.strip())
            time.sleep(1)
            driver_c.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button').click()
        except:
            print(f'Cant find the input box! Skipping "{captcha.strip()}" for {guid}. Lets try again...')
            driver_c.find_element_by_xpath('//*[@id="adcopy-link-refresh"]').click()
            i = i + 1
            cointiply_faucet(i)
            return
    time.sleep(25)
    try:
        success = driver_c.find_element_by_xpath("//div[contains(., 'Claim Again In')]")
    except:
        print(f'Damn it! "{captcha.strip()}" wasnt accepted for {guid}. Retrying...')
        driver_c.find_element_by_xpath('//*[@id="adcopy-link-refresh"]').click()
        i = i + 1
        cointiply_faucet(i)
        return
    print(f'Claim success! "{captcha.strip()}" was accepted for {guid}.')


def a():
    r = sr.Recognizer()
    with sr.AudioFile(r'D:\Crypto Related\placeholder\test.wav') as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)
            pyperclip.copy(text)
        except:
            print('Sorry.. run again...')
            pyperclip.copy('not sure what this is')


def b(driver):
    png = driver.find_element_by_xpath('/html/body').screenshot_as_png
    border = (650, 0, 1000, 800)
    im = Image.open(BytesIO(png)).convert('LA')
    im = ImageOps.crop(im, border)
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(2).save(r'D:\Crypto Related\placeholder\examine.png')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    examine = pytesseract.image_to_string(r'D:\Crypto Related\placeholder\examine.png')
    should_repeat = 'tiple correct' in examine or 'correct' in examine
    return should_repeat


def moon_roll(driver):
    driver.switch_to.window(driver.window_handles[-1])
    subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\claim-to-audio.ahk'])
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])
    subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\play-and-save-audio-init.ahk'])
    time.sleep(15)
    print('to audio done')
    a()
    driver.switch_to.window(driver.window_handles[-1])
    subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\paste-and-verify-init.ahk'])
    time.sleep(6)
    print('pasting values')
    should_repeat = b(driver)
    if should_repeat:
        repeat_madness(driver)
        return
    else:
        driver.switch_to.window(driver.window_handles[-1])
        subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\claim-and-close.ahk'])
        time.sleep(10)
        print(f'Rewards claimed wth single recaptcha!')
        return


def repeat_madness(driver):
    print('madness start')
    driver.switch_to.window(driver.window_handles[-1])
    subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\play-and-save-audio-rpt.ahk'])
    time.sleep(15)
    a()
    driver.switch_to.window(driver.window_handles[-1])
    subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\paste-and-verify-rpt.ahk'])
    time.sleep(6)
    repeat = b(driver)
    if repeat:
        repeat_madness(driver)
        return
    else:
        driver.switch_to.window(driver.window_handles[-1])
        subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\claim-and-close.ahk'])
        time.sleep(10)
        print(f'Rewards claimed wth multiple recaptcha!')
        return


def auto_roll(i=0, j=0, driver_c=driver_c, driver_m_1=driver_m_1):
    random_sec = random.randint(1000,1100)
    time.sleep(random_sec)
    nw = datetime.now()
    if j >= 3 and nw.hour >= 3:
        print(f'Rolling Cointiply! at {nw}')
        driver_c.refresh()
        time.sleep(3)
        driver_c.maximize_window()
        cointiply_faucet(0)
        driver_c.minimize_window()
        time.sleep(3)
        j = 0
    if i == 7:
        driver_m_1.refresh()
        time.sleep(5)
        i = 0
    if nw.hour == 25:
        print(f'Skipping Roll since time is at {nw}')
    else:
        driver_m_1.maximize_window()
        print(f'Rolling Moon BTC at {nw}')
        moon_roll(driver_m_1)
        i = i + 1
        j = j + 1
        print(f'i is {i}')
        print(f'j is {j}')
    auto_roll(i=i, j=j, driver_c=driver_c, driver_m_1=driver_m_1)



def auto_roll2(i=0, driver_m_1=driver_m_1):
    random_sec = random.randint(1000,1100)
    time.sleep(random_sec)
    nw = datetime.now()
    if i == 10:
        driver_m_1.refresh()
        time.sleep(5)
        i = 0
    print(f'Roll at {nw}')
    moon_roll(driver_m_1)
    i = i + 1
    auto_roll2(i=i, driver_m_1=driver_m_1)



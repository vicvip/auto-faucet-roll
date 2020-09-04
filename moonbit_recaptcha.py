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
driver = webdriver.Chrome(options=chrome_options)


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


def b():
    png = driver.find_element_by_xpath('/html/body').screenshot_as_png
    border = (650, 0, 1000, 800)
    im = Image.open(BytesIO(png)).convert('LA')
    im = ImageOps.crop(im, border)
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(2).save(r'D:\Crypto Related\placeholder\examine.png')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    examine = pytesseract.image_to_string(r'D:\Crypto Related\placeholder\examine.png')
    should_repeat = 'tiple correct' in examine
    return should_repeat




def repeat_madness():
    print('madness start')
    os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\play-and-save-recording2-attempt2.mrf"')
    time.sleep(22)
    a()
    os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\paste-and-verify-attempt2.mrf"')
    time.sleep(6)
    repeat = b()
    if repeat:
        repeat_madness()
        return
    else:
        os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\claim-and-close.mrf"')
        time.sleep(10)
        os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\close-remaining-tab.mrf"')


def roll():
    os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\claim-captcha-audio2.mrf"')
    time.sleep(8)
    os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\play-and-save-recording2.mrf"')
    time.sleep(29)
    print('to audio done')
    a()
    os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\paste-and-verify.mrf"')
    time.sleep(6)
    print('pasting values')
    should_repeat = repeat_madness()
    if should_repeat:
        repeat_madness()
        return
    else:
        os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\claim-and-close.mrf"')
        time.sleep(10)
        os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\close-remaining-tab.mrf"')




def read_recording():
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

def detect_multiple_req():
    png = driver.find_element_by_xpath('/html/body').screenshot_as_png
    border = (650, 0, 1000, 800)
    im = Image.open(BytesIO(png)).convert('LA')
    im = ImageOps.crop(im, border)
    contrast = ImageEnhance.Contrast(im)
    contrast.enhance(2).save(r'D:\Crypto Related\placeholder\examine.png')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    examine = pytesseract.image_to_string(r'D:\Crypto Related\placeholder\examine.png')
    should_repeat = 'Multiple correct solutions required' in examine
    return should_repeat

contrast = ImageEnhance.Contrast(im)
contrast.enhance(2).save(r'D:\Crypto Related\placeholder\examine.png')


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


def b():
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


def roll2():
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
    should_repeat = b()
    if should_repeat:
        repeat_madness2()
        return
    else:
        driver.switch_to.window(driver.window_handles[-1])
        subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\claim-and-close.ahk'])
        time.sleep(10)
        print(f'Rewards claimed wth single recaptcha!')
        return


def repeat_madness2():
    print('madness start')
    driver.switch_to.window(driver.window_handles[-1])
    subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\play-and-save-audio-rpt.ahk'])
    time.sleep(15)
    a()
    driver.switch_to.window(driver.window_handles[-1])
    subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\paste-and-verify-rpt.ahk'])
    time.sleep(6)
    repeat = b()
    if repeat:
        repeat_madness2()
        return
    else:
        driver.switch_to.window(driver.window_handles[-1])
        subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\claim-and-close.ahk'])
        time.sleep(10)
        print(f'Rewards claimed wth multiple recaptcha!')
        return


def auto_roll():
    random_sec = random.randint(900,1200)
    time.sleep(random_sec)
    nw = datetime.now()
    if nw.hour <= 5 or nw.hour >= 23:
        print(f'Rolling Moon BitCoin! at {nw}')
        roll2()
    else:
        print(f'Skipping Roll to prioritise other faucet since time is at {nw}')
    auto_roll()


def auto_roll2(i=0):
    random_sec = random.randint(900,1000)
    time.sleep(random_sec)
    nw = datetime.now()
    if i == 10:
        driver.refresh()
        time.sleep(5)
        i = 0
    if nw.hour <= 5:
        print(f'Skipping Roll since time is at {nw}')
    else:
        print(f'Roll at {nw}')
        roll2()
        i = i + 1
    auto_roll2(i)

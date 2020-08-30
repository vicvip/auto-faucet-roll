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


chrome_options = Options()
chrome_options.add_extension(r'D:\Crypto Related\auto-faucet-roll\chromeaudiocapture.crx')
chrome_options.add_extension(r'D:\Crypto Related\auto-faucet-roll\ublock.crx')

#Navigate to Moonbit manually, change Chrome Record Audio Ext to save in .WAV format
driver = webdriver.Chrome(options=chrome_options)



def repeat_madness():
    print('madness start')
    os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\play-and-save-recording2-attempt2.mrf"')
    time.sleep(22)
    a()
    os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\paste-and-verify-attempt2.mrf"')
    time.sleep(6)
    return b()


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
    else:
        os.system(r'C:\"Program Files (x86)\MacroRecorder\MacroRecorder.exe" -play="D:\Crypto Related\auto-faucet-roll\claim-and-close.mrf"')




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



play_rec = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/button')
/html/body/div[1]/div[1]/div[3]/div[2]/div/input

play_rec = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/input')

//
/html/body/div/div/div[3]/div/button
/html/body/div/div/div[3]/div/button


Next = driver.find_element_by_xpath("//button[@class='rc-button-default goog-inline-block']")

/html/body/div/div/div[1]
Next = driver.find_element_by_xpath("/html/body/div/div/div[1]")

png = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[1]/div[1]').screenshot_as_png

zxc = driver.find_element_by_xpath('/html/body').screenshot_as_png



moonbitcash

{"request":{"adBlocked":false,"captchaResponse":"03AGdBq25g_kt6TyCcW5-9tcMGDVV3DKVydibtGbjpJRXjqjnY_5EtbmIVL10_Ozdf3mD8RuuXyLOZd7qQH5l_y7_QpzD_HhtoQ8htYKDcflbGMMswMUawN00S6WebH20LgTI88yt9k2KAFxDKvKoP141bNiE8yOUFCdslOd4-vTKDmNCM8-pHRe26Jf2IW7SaFqyDybA2nh9wnXVF-61Zoa_S--7JXFB76PA6afSqfamZz53h1uoW9XoJeAcK8k1E6kXxs9gCWJdT_-pfGkeuAYc1bDXa7tH2EEzYeoB0hzj7UZrQoJAuzNNfg_Lwjo-nXYU206t4L97AOEteC-fEm3ZJcHwlLgjD-eenR65l51WZgUXpipPyQ0Q5jbmKXRAldQEmDNht-q3ScP0Cj95bTtTsycxWm1_uOg","instantClaim":true,"fp":"f5e921a1769bbbe804c2d9048f0d18fd","version":"20DFB2F85845BE85B3823E4F11380E8E27B3657B28D2720484FFF9D89706D0A6"}}
{"request":{"adBlocked":false,"captchaResponse":"03AGdBq24BG022hISpQI08kZ5lvyIoqCjNkMNCI9QNjQoJgFc_swbNKJWi-LRpya6qbZqx_jEYHB0IZDxdLJQJUuskCefo01MgzsWNMauCFTYIGJy7K1LcdF-m_wRsXryddMP-GgZVOREtbsA1DGILTEDFn68revZ2gB2zpAP-sXJ3iMgvZjzSxDJ7Bf8KqbeQ6RpNZFHqnstp_tULY3anaEbaF4vmsnOhzg3kXn4_QAZZRtnK_QcA1ugnDzS-edFIZYzg9DqgeA4InZftVF9JW4oXTIr0xo8_KRTprD5bQw9-oXhICrh1ult-61muIgk3QzSJZPVXxX_qQ72QTRxgMdXTD-dfJusKADBFY8ft_UFUx8AVbainMVGh6bHhjaT2wnR0C5Qt0B-6uU5JPqD5OuLUygFutx8rvw","instantClaim":true,"fp":"f5e921a1769bbbe804c2d9048f0d18fd","version":"20DFB2F85845BE85B3823E4F11380E8E27B3657B28D2720484FFF9D89706D0A6"}}


curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://rest-api.io/items

curl -i -X POST
-H ':authority: moonbitcoin.cash'
-H ':method: POST'
-H ':path: /api/faucet/service.svc/FaucetClaim'
-H ':scheme: https'
-H 'accept: application/json, text/javascript, */*; q=0.01'
-H 'accept-encoding: gzip, deflate, br'
-H 'accept-language: en-US,en;q=0.9'
-H 'content-length: 609'
-H 'content-type: application/json; charset=UTF-8'
-H 'cookie: __cfduid=dd6970fe111161f99eac076f1d93d93cc1598683500; sm_dapi_session=1; pops=LPUTimestamp=8/29/2020; session=2256118E64D985273FBC804D185C6E468AA90203F93C5EE97603B54FFA4940B621ABD62ABF9546C37DB23C40B0FCE18A53E768B1D20ECA81911B9014548BB63BF3E484B5C6E146EA06DB410596530345F597A2592AC511EC037EEDE407448F5F8DF9A389DB9CA74479AAA8DCB0B34180'
-H 'origin: https://moonbitcoin.cash'
-H 'referer: https://moonbitcoin.cash/faucet'
-H 'sec-fetch-dest: empty'
-H 'sec-fetch-mode: cors'
-H 'sec-fetch-site: same-origin'
-H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
-H 'x-requested-with: XMLHttpRequest'
-d '{"request":{"adBlocked":false,"captchaResponse":"03AGdBq25g_kt6TyCcW5-9tcMGDVV3DKVydibtGbjpJRXjqjnY_4EtbmIVL10_Ozdf3mD8RuuXyLOZd7qQH5l_y7_QpzD_HhtoQ8htYKDcflbGMMswMUawN00S6WebH20LgTI88yt9k2KAFxDKvKoP141bNiE8yOUFCdslOd4-vTKDmNCM8-pHRe26Jf2IW7SaFqyDybA2nh9wnXVF-61Zoa_S--7JXFB76PA6afSqfamZz53h1uoW9XoJeAcK8k1E6kXxs9gCWJdT_-pfGkeuAYc1bDXa7tH2EEzYeoB0hzj7UZrQoJAuzNNfg_Lwjo-nXYU206t4L97AOEteC-fEm3ZJcHwlLgjD-eenR65l51WZgUXpipPyQ0Q5jbmKXRAldQEmDNht-q3ScP0Cj95bTtTsycxWm1_uOg","instantClaim":true,"fp":"f5e921a1769bbbe804c2d9048f0d18fd","version":"20DFB2F85845BE85B3823E4F11380E8E27B3657B28D2720484FFF9D89706D0A6"}}'
https://moonbitcoin.cash/api/faucet/service.svc/FaucetClaim


curl -i -X POST -H ':authority: moonbitcoin.cash' -H ':method: POST' -H ':path: /api/faucet/service.svc/FaucetClaim' -H ':scheme: https' -H 'accept: application/json, text/javascript, */*; q=0.01' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9' -H 'content-length: 609' -H 'content-type: application/json; charset=UTF-8' -H 'cookie: __cfduid=dd6970fe111161f99eac076f1d93d93cc1598683500; sm_dapi_session=1; pops=LPUTimestamp=8/29/2020; session=2256118E64D985273FBC804D185C6E468AA90203F93C5EE97603B54FFA4940B621ABD62ABF9546C37DB23C40B0FCE18A53E768B1D20ECA81911B9014548BB63BF3E484B5C6E146EA06DB410596530345F597A2592AC511EC037EEDE407448F5F8DF9A389DB9CA74479AAA8DCB0B34180' -H 'origin: https://moonbitcoin.cash' -H 'referer: https://moonbitcoin.cash/faucet' -H 'sec-fetch-dest: empty' -H 'sec-fetch-mode: cors' -H 'sec-fetch-site: same-origin' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36' -H 'x-requested-with: XMLHttpRequest' -d '{"request":{"adBlocked":false,"captchaResponse":"03AGdBq25g_kt6TyCcW5-9tcMGDVV3DKVydibtGbjpJRXjqjnY_4EtbmIVL10_Ozdf3mD8RuuXyLOZd7qQH5l_y7_QpzD_HhtoQ8htYKDcflbGMMswMUawN00S6WebH20LgTI88yt9k2KAFxDKvKoP141bNiE8yOUFCdslOd4-vTKDmNCM8-pHRe26Jf2IW7SaFqyDybA2nh9wnXVF-61Zoa_S--7JXFB76PA6afSqfamZz53h1uoW9XoJeAcK8k1E6kXxs9gCWJdT_-pfGkeuAYc1bDXa7tH2EEzYeoB0hzj7UZrQoJAuzNNfg_Lwjo-nXYU206t4L97AOEteC-fEm3ZJcHwlLgjD-eenR65l51WZgUXpipPyQ0Q5jbmKXRAldQEmDNht-q3ScP0Cj95bTtTsycxWm1_uOg","instantClaim":true,"fp":"f5e921a1769bbbe804c2d9048f0d18fd","version":"20DFB2F85845BE85B3823E4F11380E8E27B3657B28D2720484FFF9D89706D0A6"}}' https://moonbitcoin.cash/api/faucet/service.svc/FaucetClaim


fetch('https://moonbitcoin.cash/api/faucet/service.svc/FaucetClaim', {
  method: 'POST',
  body: JSON.stringify({"request":{"adBlocked":false,"captchaResponse":"03AGdBq24BG022hISpQI08kZ5lvyIoqCjNkMNCI9QNjQoJgFc_swbNKJWi-LRpya6qbZqx_jEYHB0IZDxdLJQJUuskCefo01MgzsWNMauCFTYIGJy7K1LcdF-m_wRsZryddMP-GgZVOREtbsA1DGILTEDFn68revZ2gB2zpAP-sXJ3iMgvZjzSxDJ7Bf8KqbeQ6RpNZFHqnstp_tULY3anaEbaF4vmsnOhzg3kXn4_QAZZRtnK_QcA1ugnDzS-edFIZYzg9DqgeA4InZftVF9JW4oXTIr0xo8_KRTprD5bQw9-oXhICrh1ult-61muIgk3QzSJZPVXxX_qQ72QTRxgMdXTD-dfJusKADBFY8ft_UFUx8AVbainMVGh6bHhjaT2wnR0C5Qt0B-6uU5JPqD5OuLUygFutx8rvw","instantClaim":true,"fp":"f5e921a1769bbbe804c2d9048f0d18fd","version":"20DFB2F85845BE85B3823E4F11380E8E27B3657B28D2720484FFF9D89706D0A6"}}),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
    ':authority': 'moonbitcoin.cash',
    ':method': 'POST',
    ':path': '/api/faucet/service.svc/FaucetClaim',
    ':scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '609',
    'content-type': 'application/json; charset=UTF-8',
    'cookie': '__cfduid=dd6970fe111161f99eac076f1d93d93cc1598683500; sm_dapi_session=1; pops=LPUTimestamp=8/29/2020; session=2256118E64D985273FBC804D185C6E468AA90203F93C5EE97603B54FFA4940B621ABD62ABF9546C37DB23C40B0FCE18A53E768B1D20ECA81911B9014548BB63BF3E484B5C6E146EA06DB410596530345F597A2592AC511EC037EEDE407448F5F8DF9A389DB9CA74479AAA8DCB0B34180',
    'origin': 'https://moonbitcoin.cash',
    'referer': 'https://moonbitcoin.cash/faucet',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
})
.then(res => res.json())
.then(console.log)


fetch('https://moonbitcoin.cash/api/faucet/service.svc/FaucetClaim', {
  method: 'POST',
  body: JSON.stringify({"request":{"adBlocked":false,"captchaResponse":"03AGdBq24BG022hISpQI08kZ5lvyIoqCjNkMNCI9QNjQoJgFc_swbNKJWi-LRpya6qbZqx_jEYHB0IZDxdLJQJUuskCefo01MgzsWNMauCFTYIGJy7K1LcdF-m_wRsZryddMP-GgZVOREtbsA1DGILTEDFn68revZ2gB2zpAP-sXJ3iMgvZjzSxDJ7Bf8KqbeQ6RpNZFHqnstp_tULY3anaEbaF4vmsnOhzg3kXn4_QAZZRtnK_QcA1ugnDzS-edFIZYzg9DqgeA4InZftVF9JW4oXTIr0xo8_KRTprD5bQw9-oXhICrh1ult-61muIgk3QzSJZPVXxX_qQ72QTRxgMdXTD-dfJusKADBFY8ft_UFUx8AVbainMVGh6bHhjaT2wnR0C5Qt0B-6uU5JPqD5OuLUygFutx8rvw","instantClaim":true,"fp":"f5e921a1769bbbe804c2d9048f0d18fd","version":"20DFB2F85845BE85B3823E4F11380E8E27B3657B28D2720484FFF9D89706D0A6"}}),
  headers: {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '609',
    'content-type': 'application/json; charset=UTF-8',
    'cookie': '__cfduid=dd6970fe111161f99eac076f1d93d93cc1598683500; sm_dapi_session=1; pops=LPUTimestamp=8/29/2020; session=2256118E64D985273FBC804D185C6E468AA90203F93C5EE97603B54FFA4940B621ABD62ABF9546C37DB23C40B0FCE18A53E768B1D20ECA81911B9014548BB63BF3E484B5C6E146EA06DB410596530345F597A2592AC511EC037EEDE407448F5F8DF9A389DB9CA74479AAA8DCB0B34180',
    'origin': 'https://moonbitcoin.cash',
    'referer': 'https://moonbitcoin.cash/faucet',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
})
.then(res => res.json())
.then(console.log)
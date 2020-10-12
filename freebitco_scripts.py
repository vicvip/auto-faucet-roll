import win32com.client as comclt
import random
import time
from datetime import datetime
import subprocess

def run_firefox_console():
    subprocess.call([r'C:\Program Files\AutoHotkey\AutoHotkey.exe', r'D:\Crypto Related\auto-faucet-roll\freebitco-activate-roll.ahk'])

def auto_roll():
    random_sec = random.randint(3650,4000)
    time.sleep(random_sec)
    nw = datetime.now()
    if nw.hour <= 5:
        print(f'Skipping Roll since time is at {nw}')
    else:
        print(f'Roll at {nw}')
        run_firefox_console()
    auto_roll()


def auto_roll_max():
    random_sec = random.randint(3650,4000)
    time.sleep(random_sec)
    nw = datetime.now()
    print(f'24hour Rolling at {nw}')
    run_firefox_console()
    auto_roll_max()


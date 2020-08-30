import win32com.client as comclt
import random
import time
from datetime import datetime

def run_firefox_console():
    wsh = comclt.Dispatch("WScript.Shell")
    wsh.AppActivate('Developer Tools')
    wsh.SendKeys('{UP}{ENTER}')

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

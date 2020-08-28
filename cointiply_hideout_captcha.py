import win32com.client as comclt
import random
import time
from datetime import datetime

def hideout():
   wsh = comclt.Dispatch("WScript.Shell")
   random_sec = random.randint(900,1000)
   time.sleep(random_sec)
   nw = datetime.now()
   if(wsh.AppActivate('Hideout.co - Video Interrupted')):
      time.sleep(1)
      wsh.SendKeys('{TAB}')
      time.sleep(1)
      wsh.SendKeys('{ENTER}')
      time.sleep(5)
      wsh.SendKeys('{TAB}{TAB}{TAB}')
      time.sleep(0.5)
      wsh.SendKeys('{ENTER}')
      print(f'Attempt to refresh Captcha at {nw}')
   else:
      print(f'No "Are you still there" crap at {nw}')
   hideout()
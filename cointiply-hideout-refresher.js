// ==UserScript==
// @name     Captcha Hideout TV
// @version  1
// @grant    none
// @match       *://hideout.co/*
// @require https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js 
// ==/UserScript==

// GreaseMonkey script to check "Are you still watching?"
function checkCaptcha() {
    setInterval(function(){
      document.getElementById('stillWatching').click()
    }, (900 * 1000));
}

checkCaptcha();
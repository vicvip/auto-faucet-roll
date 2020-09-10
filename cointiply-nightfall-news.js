// ==UserScript==
// @name        NightFall News
// @description Basic Google Hello
// @match       *://nightfallnews.com/*
// @version     1
// @grant       none
// @require https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js 
// ==/UserScript==

// GreaseMonkey script to run Nighfall News offer
$(document).ready(function() { //When document has loaded

  setTimeout(function() {
    var nextBtn = document.getElementById('nextButton');
    var finishNotification = document.getElementsByClassName('card-title text-center');
    if (finishNotification[0].textContent === "Great job, your quiz was successful! ") {
    	window.location.href = "https://nightfallnews.com?ref_id=83b1cbb5&extra_data=&banner_id=9"; //Make sure to change this everytime
    }
    
    if(nextBtn === null) {
    	document.getElementsByClassName('ob-widget-section ob-first')[0].click()
    } else {
    	document.getElementById('nextButton').click();
    }
    console.log("TADA!")
    
  //Code to run After timeout elapses

  }, Math.floor(Math.random() * 8000) + 2000); //Two seconds will elapse and Code will execute.

}); 


$(document).ready(function() { //When document has loaded
	setTimeout(function() {
    location.reload();

  }, Math.floor(Math.random() * 5000) + 35000); //Two seconds will elapse and Code will execute.

}); 


// var i = 0;
// var timer = setInterval(function() {
//   console.log(++i);
//   if (i === 50) clearInterval(timer);
//   document.querySelector("#StakeButtons > div > button:nth-child(2)").click();
// }, 30 * 1000);
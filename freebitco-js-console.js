// Freebitco.in blocks Tampermonkey/Greasemonkey extension. Therefore it's better to run this in a JS console (Firefox) recursively
function autoRoll(){
	document.getElementById('free_play_form_button').click();
	closeModal();
}

function closeModal() {
  setTimeout(function(){
	console.log('close')
		  document.getElementsByClassName('close-reveal-modal')[0].click();
  }, (7 * 1000));
}

autoRoll()
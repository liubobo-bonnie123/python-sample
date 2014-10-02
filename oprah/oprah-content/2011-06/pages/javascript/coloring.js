var canvas, context, reference, brush, curSize;
var started = false;
var sizeScrollerStart = 153;
var outlineImage = new Image();
var userDrawing = new Image();
var canvasWidth = 847;
var canvasHeight = 768;

///// Loads the selected image as the "foreground" of the coloring page.

function loadPage() {
	reference = document.getElementById('referenceImage');

	switch(parseInt(window.name))
	{
		case 1:
			reference.src = "images/coloring/BertandErnieBakers-SW_c01_Bert.png";
			break;
		case 2:
			reference.src = "images/coloring/BertandErnieBakers-SW_c02_Cookie.png";
			break;
		case 3:
			reference.src = "images/coloring/SesameStreet123-9781403753731-SW_c01_Elmo.png";
			break;
		case 4:
			reference.src = "images/coloring/SesameStreet123-9781403753731-SW_c02_Oscar.png";
			break;
		case 5:
			reference.src = "images/coloring/TheFirehouse-9781403789372-SW_c01_BigBird.png";
			break;
		case 6:
			reference.src = "images/coloring/TheFirehouse-9781403789372-SW_c02_Elmo.png";
			break;
	}
	$("#referenceImage").css("background", "url("+reference.src+") no-repeat top left");
} 

///// Changes the color paint currently being used. Called when a map area in the pallette
///// is clicked.

function changeColor(number) {
	if(context)
	{
		switch (number){
			case 1: 
				context.strokeStyle = 'rgb(255,0,0)';
			break;
			case 2: 
				context.strokeStyle = 'rgb(255,100,0)';
			break;
			case 3:
				context.strokeStyle = 'rgb(255,212,0)';
			break;
			case 4:
				context.strokeStyle = 'rgb(0,184,0)';
			break;
			case 5:
				context.strokeStyle = 'rgb(11,84,184)';
			break;
			case 6:
				context.strokeStyle = 'rgb(194,87,233)';
			break;
			case 7:
				context.strokeStyle = 'rgb(0,0,0)';
			break;
			case 8:
				context.strokeStyle = 'rgb(255,255,255)';
			break;
			case 9:
				context.strokeStyle = 'rgb(255,104,168)';
			break;
			case 10:
				context.strokeStyle = 'rgb(255,168,0)';
			break;
			case 11:
				context.strokeStyle = 'rgb(0,103,92)';
			break;
			case 12:
				context.strokeStyle = 'rgb(71,222,254)';
			break;
			case 13:
				context.strokeStyle = 'rgb(69,21,237)';
			break;
			case 14:
				context.strokeStyle = 'rgb(255,195,188)';
			break;
			case 15:
				context.strokeStyle = 'rgb(98,40,0)';
			break;
			case 16:
				context.strokeStyle = 'rgb(70,70,70)';
			break;
			default :
				context.strokeStyle = '#000'; 
		}
	}
}

///// Hide or display popups or otherwise navigate away from the current page
///// when buttons are clicked. (Save, Help, Home, Pages)

var toMainPage = "";

function closeActivitiesView() {
	window.location.href = "home.html";
}

function gotoMainPage() {
	window.location.href = "mainpage.html";
}

function saveImage() {
	outlineImage.src = reference.src;
	context.drawImage(outlineImage, 0, 0);
	userDrawing = canvas.toDataURL();
	showSavePopup(true);
}

function showSavePopup(show) {
	document.getElementById("savableImage").src = userDrawing;
	document.getElementById("save-popup").style.display = (show == true) 
		? "" : "none";
}

function leaveColoring(destination) {
	toMainPage = destination;
	hideLeavePopup(event, false, false);
}

function hideLeavePopup(ev, hide, leave) {
	document.getElementById("leave-popup").style.display = (hide == true) 
		? "none" : "";
	if(leave) {
		if(toMainPage == "main") closeActivitiesView();
		else if(toMainPage == "selection") gotoMainPage();
	}
}	

function showHelp(event, show){
	event.preventDefault();
	event.stopPropagation();
	document.getElementById("help-popup").style.display = (show == true) ? "" : "none";
}

///// Functions for displaying the appropriate cursor to user function.

function showPointerCursor() {
	document.body.style.cursor = 'pointer';
}

function showDefaultCursor() {
	document.body.style.cursor = 'default';
}

function showCrayanCursor() {
	document.body.style.cursor = 'url(images/coloring/crayon_cursor.gif), crosshair';
}

///// Initalization function.

if(window.addEventListener) {
	window.addEventListener('load', function () {
		function init () {
			document.onselectstart = function () { return false; };

			canvas = document.getElementById('drawplane');
			context = canvas.getContext('2d');

			canvas.style.width = canvasWidth + "px";
			canvas.style.Height = canvasHeight + "px";
			context.fillStyle = '#ffffff';					
			context.fillRect(0, 0, canvasWidth, canvasHeight);

			// Find and bind events to the reference/bg image.
			reference = document.getElementById('referenceImage');

			reference.addEventListener('mousedown', touchStart, false);
			reference.addEventListener('mousemove', touchMove, false);
			reference.addEventListener('mouseup', touchEnd, false);

			// Find, set styles, and bind events to the brush selector.
			brush = document.getElementById('brush');
			brush.style.top = sizeScrollerStart+"px";
			
			context.lineWidth = 65;
			curSize = context.lineWidth;
			
			context.lineCap = "round";
			context.lineJoin = "round";

			brush.addEventListener('mousedown', setMouseDown, false);
			brush.addEventListener('mouseup', setMouseUp, false);
			brush.addEventListener('mousemove', moveBrush, false);
		}


		///// Do the drawing!

		function touchStart (event) {
			started = true;
			context.beginPath();
			context.moveTo(event.layerX, event.layerY);
		}

		function touchMove (event) {
			event.preventDefault();
			event.stopPropagation();
			if(started == false) { return; }

			context.lineTo(event.layerX, event.layerY);
			context.stroke();
		}


		///// Keeps track of what kind of gesture is being made, whether the mouse button
		///// is down or not (are we drawing?).

		var mouseIsDown = false;

		function touchEnd(event) { started = false; }
		
		function setMouseDown() { mouseIsDown = true; }

		function setMouseUp() { mouseIsDown = false; }

		
		///// Changing the brush size.
	  
		function moveBrush(event) {
			if (mouseIsDown == true) {
				var tempy = event.pageY - document.getElementById('content').offsetTop;
				brush.style.zIndex = "4";
									
				if(tempy < 153) tempy = 153;
				else if(tempy > 611) tempy = 611;
			
				tempy -= 229; // half the width of the slider button (get middle)
				
				brush.style.top = (tempy) + "px";

				context.lineWidth = Math.floor(10+(86-(tempy - 76)/3));
				curSize = context.lineWidth;
			}
		}
		
		init();
		
	}, false);
}
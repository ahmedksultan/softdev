// Ahmed K. J. H. Sultan and Kazi A. Jamal -- oldfirefoxdata
// SoftDev pd9
// K08-- What is it saving the screen from ?
// 2020-02-13

//model for HTML5 canvas-based animation

//access canvas and buttons via DOM
var c = document.getElementById('playground');
var dotButton = document.getElementById('circle');
var dvdlogoButton = document.getElementById('dvdlogo');
var stopButton = document.getElementById('stop');

//prepare to interact with canvas in 2D
var ctx = c.getContext('2d');

//set fill color to celine
ctx.fillStyle = '#00ffff';

var dotrequestID;
var dvdrequestID;

var clear = function (e) {
     e.preventDefault();
     ctx.clearRect(0, 0, 500, 500);
};

var radius = 0;
var growing = true;

var drawDot = function () {
     window.cancelAnimationFrame(dotrequestID);

     ctx.clearRect(0, 0, c.width, c.height);

     if (growing) {
          radius += 1;
     } else {
          radius -= 1;
     }

     if (radius == c.width / 2) growing = false;
     else if (radius == 0) {
          growing = true;
     }

     //draw the dot
     ctx.beginPath();
     ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 * Math.PI);
     ctx.stroke();
     ctx.fill();

     //console.log(dotrequestID);
     dotrequestID = window.requestAnimationFrame(drawDot);
};

var xpos = c.width / 2;
var ypos = c.height / 2;
var xchange = 2;
var ychange = 3;
// set up image
const dvdimg = new Image();
dvdimg.src = 'logo_dvd.jpg';
// resize image in same 3:2 aspect ratio
imgwidth = 150;
imgheight = 100;

var dvdLogo = function () {
     window.cancelAnimationFrame(dvdrequestID);

     ctx.clearRect(0, 0, c.width, c.height);

     ctx.drawImage(dvdimg, xpos, ypos, imgwidth, imgheight);

     // check if logo should bounce off left or right of canvas
     if (xpos + xchange >= c.width - imgwidth / 2 || xpos + xchange <= imgwidth / -2) {
          xchange *= -1;
     }
     // check if logo should bounce off top or bottom of canvas
     if (ypos + ychange >= c.height - imgheight / 2 || ypos + ychange <= imgheight / -2) {
          ychange *= -1;
     }

     xpos += xchange;
     ypos += ychange;

     //console.log(dvdrequestID);
     dvdrequestID = window.requestAnimationFrame(dvdLogo);
};

var stopIt = function () {
     console.log(dotrequestID);
     window.cancelAnimationFrame(dotrequestID);
     console.log(dvdrequestID);
     window.cancelAnimationFrame(dvdrequestID);
};

dotButton.addEventListener('click', drawDot);
stopButton.addEventListener('click', stopIt);
dvdlogoButton.addEventListener('click', dvdLogo);
// Ahmed Sultan and Vishwaa Sofat -- MUNy Problems
// SoftDev pd9
// K12 - DotConn 2: Electric Boogaloo
// 2020-03-29

const container = document.getElementById("container");
const clear = document.getElementById("clear");
const xmlns = "http://www.w3.org/2000/svg";

var lastX = 0;
var lastY = 0;

var drawLine = false;

var clearcont = function (event) {
     console.log("CLEARING CLEARING CLEARING");
     /* was originally going to just paint container white,
     but found this answer on StackOverflow we really liked and
     want to keep in our records for future use */
     while (container.lastChild) {
          container.removeChild(container.lastChild);
     }
     drawLine = false;
     console.log("...COMPLETED!")
}

var draw = function (event) {
     const mouseX = event.offsetX;
     const mouseY = event.offsetY;
     console.log("drawing dot at " + mouseX + ", " + mouseY);
     // creating the dot
     const dot = document.createElementNS(xmlns, "circle");
     // assigning dot attributes
     dot.setAttribute("r", 5);
     dot.setAttribute("fill", "black");
     dot.setAttribute("cx", mouseX);
     dot.setAttribute("cy", mouseY);
     // appending dot to svg container
     container.appendChild(dot);

     // drawing the line
     if (drawLine) {
          const line = document.createElementNS(xmlns, "line");
          // assigning line attributes
          line.setAttribute("stroke", "black")
          line.setAttribute("x1", mouseX);
          line.setAttribute("y1", mouseY);
          line.setAttribute("x2", lastX);
          line.setAttribute("y2", lastY);
          // appending line to svg container
          container.appendChild(line);
     }

     drawLine = true;

     // setting these coords to last coords
     lastX = mouseX;
     lastY = mouseY;
     console.log("...completed!")
}

// adding event listeners
container.addEventListener("mousedown", draw);
clear.addEventListener("click", clearcont); 
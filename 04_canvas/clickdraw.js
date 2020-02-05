var mode = "dot"

var c = document.getElementById("slate")
var ctx = c.getContext("2d")

function clear() {
     ctx.clearRect(0, 0, 300, 300);
}

function dotmode() {
     mode = "dot"
}

function rectmode() {
     mode = "rect"
}

function draw(e) {
     console.log(e)
     if(mode==="dot"){
          var circle = new Path2D();
          circle.moveTo(e.offsetX, e.offsetY);
          circle.arc(e.offsetX, e.offsetY, 2, 0, 2 * Math.PI);
          ctx.fill(circle);
          console.log("dot")
     }
}

var clearbutton = document.getElementById("clear")
clearbutton.addEventListener('click',clear);

var dotbutton = document.getElementById("dot")
dotbutton.addEventListener('click', dotmode);

var rectbutton = document.getElementById("rect")
rectbutton.addEventListener('click', rectmode);

c.addEventListener('click', draw)
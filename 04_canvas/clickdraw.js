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
          ctx.arc(e.offsetX,e.offsetY,2,0,360)
     }
}

var clearbutton = document.getElementById("clear")
clearbutton.addEventListener('click',clear);

var dotbutton = document.getElementById("dot")
dotbutton.addEventListener('click', dotmode);

var rectbutton = document.getElementById("rect")
rectbutton.addEventListener('click', rectmode);

c.addEventListener('click',draw)
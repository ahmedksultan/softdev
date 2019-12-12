// factorial 
var fact = function (n) {
     while (n > 0) {
          return n * fact(n - 1);
     }
     return 1;
}

/*
console.log("HELLO!");
console.log(fact(0));
console.log(fact(1));
console.log(fact(2));
console.log(fact(3));
console.log(fact(4));
console.log(fact(5));
*/


// fibonacci
var fibonacci = function (n) {
     if (n == 0) {
          return 0;
     }
     if (n == 1) {
          return 1;
     }
     return fibonacci(n - 1) + fibonacci(n - 2);
}

/*
console.log(fibonacci(0));
console.log(fibonacci(1));
console.log(fibonacci(2));
console.log(fibonacci(3));
console.log(fibonacci(4));
console.log(fibonacci(5));
*/

var gcd = function (a, b) {
     if (b > a) {
          return gcd(b, a);
     }
     else if (a % b == 0) {
          return b;
     }
     return gcd(b, a % b);
}

/*
console.log(gcd(15, 5));
console.log(gcd(16, 5));
console.log(gcd(18, 4));
console.log(gcd(20, 3));
console.log(gcd(100, 15));
*/

students = ["joe", "bean", "alfred", "albert", "alexander", "alexandra", "alexei"];

var randomStudent = function (list) {
     n = Math.floor(Math.random() * list.length);
     return list[n];
}

/*
console.log(randomStudent(students));
console.log(randomStudent(students));
console.log(randomStudent(students));
console.log(randomStudent(students));
console.log(randomStudent(students));
console.log(randomStudent(students));
console.log(randomStudent(students));
console.log(randomStudent(students));
console.log(randomStudent(students));
console.log(randomStudent(students));
console.log(randomStudent(students));
*/

/*

var factorial = document.getElementById("factorial");
factorial.addEventListener("click", function () {
     console.log(fact(5));
});

var fib = document.getElementById("fibonacci");
fib.addEventListener("click", function () {
     console.log(fibonacci(5));
});

var gcdiv = document.getElementById("gcd");
gcdiv.addEventListener("click", function () {
     console.log(gcd(15, 3));
});

var randStud = document.getElementById("randomStudent");
randStud.addEventListener("click", function () {
     console.log(randomStudent(students));
});

*/

var f = document.getElementById("factorial");
f.addEventListener("click", function () {
     document.getElementById("1").innerHTML = fact(5);
     console.log(fact(5));
});
var fib = document.getElementById("fibonacci");
fib.addEventListener("click", function () {
     document.getElementById("2").innerHTML = fibonacci(5);
     console.log(fibonacci(5));
});
var g = document.getElementById("gcd");
g.addEventListener("click", function () {
     document.getElementById("3").innerHTML = gcd(24, 20);
     console.log(gcd(24, 20));
});
var ranStu = document.getElementById("randomStudent");
ranStu.addEventListener("click", function () {
     document.getElementById("4").innerHTML = randomStudent(students);
     console.log(randomStudent(students));
});

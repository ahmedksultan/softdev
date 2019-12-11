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

document.getElementById("fibonacci").addEventListener("click", console.log("hello!"));

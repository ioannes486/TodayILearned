// 변수선언
const a = 5;
const b = 2; // 불변변수 - const
let myName = "Jin"; // 가변변수 - let
// const는 바뀔 수  없다.

console.log(a + b);
console.log(a * b);
console.log(a / b);

// 변수 할당
myName = "Kwanghwan";

// boolean
const amIFat = null;
let something;
console.log(something, amIFat);

// array
const daysOfWeek = [1, 2, "hello", "my", "name", "jin"];
console.log(daysOfWeek);
daysOfWeek.push("function");
console.log(daysOfWeek);

//Objects(딕셔너리)

//
const player = {
  name: "nico",
  points: 10,
  fat: true,
};
console.log(player);
console.log(player.name); // 오브젝트 인덱싱
player.fat = false;
console.log(player);
player.lastName = "potato";
console.log(player);

// 사용자 정의 함수
function sayHello(nameOfPerson, age) {
  console.log("hello my name is " + nameOfPerson + "and I am " + age);
}

sayHello("nico", 10);
sayHello("dal", 23);
sayHello("lynn", 21);

function plus(a, b) {
  console.log(a + b);
}

plus(8, 60);
//오브젝트와 사용자 정의 함수
//js에서는 클래스를 정의하는 대신 아래와 같이 오브젝트 안에 넣어서 함수를 사용한다.
const player = {
  name: "nico",
  sayHello: function (otherPersonsName) {
    console.log("hello " + otherPersonsName + " nice to meet you");
  },
};
console.log(player.name);
player.sayHello("lynn");

const calculator = {
  plus: function (a, b) {
    return a + b + "hello";
  },
  minus: function (a, b) {
    return a - b;
  },
  times: function (a, b) {
    return a * b;
  },
  divide: function (a, b) {
    return a / b;
  },
  power: function (a, b) {
    return a ** b;
  },
};
const krAge = calculator.plus(1, 2);
console.log(krAge);

const age = parseInt(prompt("how are you"));

// 조건문
if (isNaN(age)) {
  console.log("please write a number");
} else {
  console.log("thank you for writing your age");
}

console.log(age);
parseInt("15");
console.log(typeof "25", typeof parseInt("15"));

console.log(title);

title.innerText = "title3";
title.style.color = "blue";

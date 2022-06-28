// Q1. 기본적인 구구단을 Node Js로 숫자를 입력받아서 함수 구현하기
let num = 2;

let gugu = (number) => {
  for (i = 1; i < 10; i++) {
    console.log(`${num}  *  ${i} = ${num * i}`);
  }
};

gugu(num);

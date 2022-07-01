// Q1. 기본적인 구구단을 Node Js로 숫자를 입력받아서 함수 구현하기

// 초기 코드
// let num = 2;

// let gugu = (number) => {
//   for (i = 1; i < 10; i++) {
//     console.log(`${num}  *  ${i} = ${num * i}`);
//   }
// };

// gugu(num);


'use strict';

(function () {
    const getGugu = () => {
        const num = 2;
        const gugu = [1, 2, 3, 4, 5, 6, 7, 8, 9];

        return gugu.map((value) => `${num} * ${value} = ${num * value}`);
    };

    console.log(getGugu());
}) ();

// 1. map, filter, reduce 고차함수 구현하기
// 2. 함수의 합성
// 3. 커링을 이용해서 로직을 더 간단하게 나타내기
// 4. 지연평가
// 5. Sql Injection Prevention 미들웨어 구현하기

const arr = [1, 2, 3, 4, 5];

// 1. 거르는건 -> filter 함수

const sum = arr
  .filter((item) => item % 2 === 1)
  .map((value) => value * 2)
  .reduce((prev, curr) => prev + curr);

const map = (func, arr) => {
  const result = [];

  for (const el of arr) {
    result.push(func(el));
  }

  return result;
};

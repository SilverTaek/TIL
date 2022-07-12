### 미들웨어

콜백함수를 여러개 배열 형태로 등록할 수 있다.

import express from 'express';
const app = express();

app.get(
'/',
(req, res, next) => {
console.log('first');
next('route'); // 다음 미들웨어로 넘어감
},
(req, res, next) => {
console.log('first2');
}
);

어플리케이션 마지막에는 에러 처리하는 것을 담아줘야한다.

app.use((error, req, res, next) => {
console.log(error);
res.status(500).send('Sorry, try later!)
})
app.listen(8080);

app.all() => 경로에 한해서만
app.use() => 어떤 경로를 하더라도 항상 use가 호출이 됨

### 에러처리

1. 클라이언트에게 충분한 에러에 대한 내용을 전달
2. 시스템 내부적으로 큰 문제가 발생하더라도 서버가 죽지않도록 하는 것

동기적 에러처리라면 try catch 로 감싸서 해줌

비동기적이라면 에러가 던져졌을 때 콜백함수로 전달이 되기 때문에 에러를 처리하기 위해선 콜백함수 안에서 처리해주기

async await -> catch로만 잡을 수 있음

### 비동기 에러 처리 방법

async-errors 라이브러리

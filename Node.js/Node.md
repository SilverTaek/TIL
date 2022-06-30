# What is Node.js?
* Node.js is an open-source
* cross-platform
* JavaScript runtime environment

## Event loof
이벤트 루프는 가능하다면 언제나 시스템 커널에 작업을 떠넘겨서 Node.js가 NonBlocking I/O 작업을 수행하도록 해줍니다.

이벤트 루프는 메인스레드 겸 싱글스레드로서, 비즈니스 로직을 수행한다.
또한, 수행 도중에 블로킹 IO작업을 만나면 커널 비동기 또는 자신의 워커쓰레드풀에게 넘겨주는 역할까지 한다.

### Event loof 내부 동작 과정

이벤트루프는 몇 개의 단계로 구성되어 있으며 각각의 단계는 FIFO 큐를 가지고 있다.

* timers : 이 단계는 setTimeout()과 setInterval()로 스케줄링한 콜백을 실행합니다.
* pending callbacks: 다음 루프 반복으로 연기된 I/O 콜백들을 실행합니다.
* idle, prepare: 내부용으로만 사용합니다.
* poll: 새로운 I/O 이벤트를 가져옵니다. I/O와 연관된 콜백(클로즈 콜백, 타이머로 스케줄링된 콜백, setImmediate()를 제외한 거의 모든 콜백)을 실행합니다. 적절한 시기에 node는 여기서 블록 합니다.
* check: setImmediate() 콜백은 여기서 호출됩니다.
* close callbacks: 일부 close 콜백들, 예를 들어 socket.on('close', ...).

## V8 엔진
JIT 컴파일 방식을 사용하여 자바스크립트를 인터프리트하지 않고 즉시 기계어로 컴파일 합니다.

* 인라인 캐싱
* 최적화 컴파일러
* 메모리 관리, GC

## libuv

NodeJs는 기본적으로 libuv위에서 동작한다.
Node 인스턴스가 뜰 때, libuv에는 워커 쓰레드풀(default 4개)이 생성된다.
블로킹 작업(api콜, DB Read/Write 등)이 들어오면 이벤트루프가 uv_io에게 내려준다.
libuv는 커널단에서 어떤 비동기 작업들을 지원해주는지 알고 있기 때문에, 그런 종류의 작업들을 받으면, 커널의 비동기함수들을 호출한다.
작업이 완료되면 시스템콜을 libuv에게 던져준다.
libuv 내에 있는 이벤트루프에게 콜백으로서 등록된다.
libuv의 워커쓰레드는 커널이 지원안하는 작업들을 수행한다.

## Callback function
콜백 함수는 다른 함수에 인수로 전달된 함수이며 외부 함수 내부에서 호출되어 일종의 루틴이나 작업을 완료한다.

```
function greeting(name) {
  alert('Hello ' + name);
}

function processUserInput(callback) {
  var name = prompt('Please enter your name.');
  callback(name);
}

processUserInput(greeting);
```

## Promise
비동기 작업의 단위
```
const promise = new Promise((resolve, reject) => {
    // 비동기 작업
})
```

`excutor` 라는 이름의 함수를 인자로 받는다.

resolve를 호출하게 된다면 비동기 작업이 성공했다라는 뜻이다.
reject를 호출하게 된다면 비동기 작업이 실패했다라는 뜻이다.

new Promise(...) 하는 순간 여기에 할당된 비동기 작업이 바로 시작된다.

promise가 끝나고 난 다음의 동작을 설정할 수 있는데 then / catch 메소드이다.

promise는 세 가지 상태를 가진다.
(pending, fulfilled, rejected)

promise는 비동기 작업을 생성/시작하는 부분(new Promise(...))과 작업 이후의 동작 지정 부분(then, catch)을 분리함으로써 기존의 러프한 비동기 작업보다 유연한 설계를 가능토록 한다.

## Async
async function 선언은 AsyncFunction 객체를 반환하는 하나의 비동기 함수를 정의한다.

async 함수는 항상 promise를 반환한다.

## await

await[[Promist 객체]] 형태로 사용한다.

await은 Promise가 완료될 때까지 기다린다.

await은 Promise가 resolve한 값을 내놓는다.

Promise에서 reject가 발생하면 예외가 발생한다.

await을 async 에서만 사용할 수 있는 이유?
=> 비동기로 시작한 작업의 특징은, 그로부터 파생된 모든 작업 또한 비동기 작업으로 간주할 수 있다.

Q) 그렇다면 비동기를 적용해놓고 다른 job이 없다면 이것은 성능 낭비인가? 낭비라면 다시 동기로 바꿔줘야하나?

## 동시성 & 병렬성

* 동시성 : 동시성은 동시에 여러 작업을 실행하는 것을 의미하지만 반드시 동시에 실행할 필요는 없다.
* 병렬성 : 동시에 실행되는 둘 이상의 작업을 지원할 수 있는 시스템



참조문서
* https://github.com/nodejs/node
* https://nodejs.org/ko/docs/guides/event-loop-timers-and-nexttick/

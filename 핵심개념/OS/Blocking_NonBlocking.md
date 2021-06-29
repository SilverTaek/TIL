# Blocking vs Non-Blocking
## Blocking 
자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 다른 작업이 끝날 때까지 `기다렸다`가 자신의 작업을 시작하는 것

## Non-Blocking
다른 주체의 작업에 `관련없이` 자신의 작업을 하는 것


정리 : 다른 주체가 작업할 때 자신의 `제어권`이 있는지 없는지로 볼 수 있다.

# Synchronous(동기) vs Asynchronous(비동기)
## Synchronous
작업을 동시에 수행하거나, 동시에 끝나거나, 끝나는 동시에 시작함을 의미

## Asynchronous
시작, 종료가 일치하지 않으며, 끝나는 동시에 시작을 하지 않음을 의미

# 조합 4가지 경우

![image](https://user-images.githubusercontent.com/43171179/123688776-64ea5800-d88d-11eb-902b-5b2be43b3759.png)

## Synchronous Blocking I/O
![image](https://user-images.githubusercontent.com/43171179/123688334-d544a980-d88c-11eb-84a4-a5fe74bc5749.png)
예시 : 상사는 기다리라고함 관심을 가지며 기다리다가 결과를 주면 바로 처리 ex) 입출력
## Synchronous Non-Blocking I/O
![image](https://user-images.githubusercontent.com/43171179/123688418-eb526a00-d88c-11eb-8c79-b1f2fe5ab98f.png)
예시 : 다른 작업이 있어도 자신의 제어권을 가지고 일을 함 중간중간마다 물어봄
## Asynchronous Non-Blocking I/O (AIO)
![image](https://user-images.githubusercontent.com/43171179/123688513-0cb35600-d88d-11eb-981a-ab0d0545affa.png)
다른 작업이 시작되어도 자신이 하던 작업을 멈추지 않음 자신의 일이 끝나야 그때서야 처리
## Asynchronous Blocking 
Asynchronous Blocking 조합은 비효율적이라 직접적으로 사용하는 모델은 없다. 하지만 Asynchronous Non-Blocking 모델 중에서 Blocking 으로 동작하는 작업이 있는 경우 의도와 다르게 Asynchronous Blocking으로 동작할 때가 있다고 한다.

대표적인 예로는 Node.js와 MySQL을 함께 사용하는 경우이다. Node.js는 비동기로 작업하려 하지만 MySQL 드라이버가 Blocking 방식으로 동작하므로 어쩔 수 없이 Asynchronous Blocking 방식으로 동작하게 된다.

결과를 바로 처리하지 않아도 됨

# 정리
Synchronous VS Asynchronous
두 가지 이상의 대상(메서드, 작업, 처리 등)과 이를 처리하는 시간으로 구분한다.
Synchronous: 호출된 함수의 리턴하는 시간과 결과를 반환하는 시간이 일치하는 경우
Asynchronous: 호출된 함수의 리턴하는 시간과 결과를 반환하는 시간이 일치하지 않는 경우
Blocking VS Non-Blocking
호출되는 대상이 직접 제어할 수 없는 경우 이를 구분할 수 있다.
Blocking: 직접 제어할 수 없는 대상의 작업이 끝날 때까지 기다려야 하는 경우
Non-Blocking: 직접 제어할 수 없는 대상의 작업이 완료되기 전에 제어권을 넘겨주는 경우

참고 문헌 
https://velog.io/@codemcd/Sync-VS-Async-Blocking-VS-Non-Blocking-sak6d01fhx
https://www.youtube.com/watch?v=oEIoqGd-Sns
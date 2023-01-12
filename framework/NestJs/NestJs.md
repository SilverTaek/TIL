### Controllers

- 어플리케이션을 향한 요청을 받는 첫번째 스텝

- 요청을 하는 주체

### Providers

- provider는 디펜던시로 주입될 수 있다.

- 컨트롤러는 HTTP 요청을 핸들링하고 더 복잡한 일들을 provider에게 위임해야 한다.

- provider는 그저 js의 클래스일 뿐이다.

### modules

- 같은 도메인에 속한 것들을 응집화 할 수 있도록 도와줌

- 앱의 사이즈가 커질수록, 경계를 설정해서 복잡도를 매니징할 수 있다.

provide에는 token이 들어간다.

## DI

1. Controller 인스턴스화 할 때, dependency를 살펴본다.
2. 토큰은 Service 클래스를 리턴
3. 싱글톤 스코프로 Service를 인스턴스화 한다.
4. 메모리 내에 캐시를 하고 재사용가능 하도록 만든다.
5. bottom up 으로 dependency가 정확한 순서로 관리

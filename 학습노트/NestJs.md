# Nest Js

Nest (NestJS)는 효율적이고 확장 가능한 Node.js 서버 측 애플리케이션을 구축하기 위한 프레임 워크이다.

프로그레시브 JavaScript를 사용하고 TypeScript로 빌드되고 완벽하게 지원하며 OOP / FP / FRP 요소를 사용할수있게 해준다.

## 철학

Nest는 개발자와 팀이 고도로 테스트 가능하고 확장 가능하며 느슨하게 결합되고, 유지 관리가 쉬운 애플리케이션을 만들 수 있는 즉시 사용 가능한 애플리케이션 아키텍처를 제공한다.

설치

```
npm i -g @nestjs/cli
```

프로젝트 설치

nest new ./

request -> module -> cotroller -> service

## 모듈

AppModule

모듈은 기본적으로 싱글톤

프로바이더

종속성으로 주입할 수 있다.

서비스

injectable 데코레이터로 감싸져서 모듈에 제공

주입하여 앱 전체에서 사용할 수 있다.

서비스에서 주로 해주는게 맞다

private 를 써주면 property로 선언이 된다.

원래는

```
todoService: TodoService;

constructor(todoService: TodoService) {
    this.todoService = todoService;
}
```

```

constructor(private todoService: TodoService) {}
```

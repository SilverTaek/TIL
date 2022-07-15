# Nest Js

Nest (NestJS)는 효율적이고 확장 가능한 Node.js 서버 측 애플리케이션을 구축하기 위한 프레임 워크이다.

프로그레시브 JavaScript를 사용하고 TypeScript로 빌드되고 완벽하게 지원하며 OOP / FP / FRP 요소를 사용할수있게 해준다.

## 철학

Nest는 개발자와 팀이 고도로 테스트 가능하고 확장 가능하며 느슨하게 결합되고, 유지 관리가 쉬운 애플리케이션을 만들 수 있는 즉시 사용 가능한 애플리케이션 아키텍처를 제공한다.

설치

```
npm i -g @nestjs/cli
```

프로젝트 초기화

```
nest new ./
```

### 부가적으로 해야 할 일

- 환경 변수 설정
- 유효성 검증
- 인증
- 로깅
- 헬스체크
- CQRS
- 클린 아키텍처
- 유닛 테스트

### 노드의 특징

싱글 스레드 Nonblocking/io
이벤트 루프

### 타입스크립트

### 컨트롤러

nest g resource [name]
와일드카드 사용 \* 별표 문자를 사용하면 문자열 가운데 어떤 문자가 와도 상관없이 라우팅 패스를 구성하겠다는 뜻

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

### dto

class vs interface

클래스는 인터페이스와 다르게 런타임에서 작동하기 때문에 파이프 같은 기능을 이용할 때 더 유용하다.

### pipes

transformer
validator

### 커스텀 파이프 구현 방법

### typeorm

node js 에서 실행되고 typeScript로 작성된 객체 관계형

@nestjs/typeorm

mysql 모듈
npm install --save @nestjs/typeorm typeorm mysql2

### entity

### 삭제

remove vs delete
remove : 무조건 존재하는 아이템을 지워야함 아니면 에러남
delete : 만약 아이템이 존재하면 지우고 존재하지 않으면 영향이 없다. => 작업을 한번만 사용

따라서 delete를 사용

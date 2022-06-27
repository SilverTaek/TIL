# NestJs 프로젝트

## 구조

### app.controller.spec.ts

app.controller.ts 파일을 테스트하기 위한 파일

`app.controller.ts` : 하나의 라우트가 있는 기본 컨트롤러
`app.controller.spec.ts` : 컨트롤러를 위한 유닛 테스트
`app.module.ts` : 애플리케이션의 루트 모듈
`app.service.ts` : 단일 메소드를 사용하는 기본 서비스
`main.ts` : 핵심기능 NestFactory를 사용하여 Nest 애플리케이션 인스턴스를 생성하는 애플리케이션의 엔트리 파일

@Get() => 데코레이터 패턴 즉, 함수나 메소드에 첨가를 해주는 것

service에서 리턴 된 값이 module 로 들어가고 Factory를 통해 알아서 자동으로 클라이언트가 해당하는 라우터에 들어가서 받을 수 있게 설정

### package.json

## dependencies

- @nestjs/common
- @nestjs/core
- @nestjs/platform-express
  => nestjs 자체적으로 동작하는 라이브러리
  `reflect-metadata` : 데코레이터 패턴을 사용할 수 있는 패키지
  `rimraf` : 윈도우에서도 rm - rf 명령어를 사용할 수 있게 해줄 수 있는 명령어
  `rxjs` : 비동기 이벤트 기반 프로그램을 작성하기 위한 라이브러리

## Controller

들어오는 요청을 처리 하고 클라이언트에 응답을 반환 하는 역할을 한다.
기본 컨트롤러를 만들기 위해 클래스와 데코레이터를 사용 합니다. 데코레이터는 클래스를 필수 메타데이터와 연결하고 Nest가 라우팅 맵을 생성할 수 있도록 한다.

## providers

service, repository, factory, component 등 기본 Nest 클래스의 대부분은 providers로 취급 될 수 있다. 주요 아이디어는 중속성을 주입할 수 있다는 것이다.

### app.module.ts

providers에 등록을 해줘야 의존성 주입이 가능함

```
export class AppController {
constructor(private readonly appService: AppService) {
this.appService = appService
}
}

// 의존성 주입
```

의존성 주입할 때는 각각의 module에서 exports에 추가하는 형태로 사용해야 단일 책임 원칙을 위반하지 않고 사용할 수 있다.

## MiddleWare

Express의 middleware와 동일하다.
(각각의 대해 순서가 있다.)
@Injectable() => DI가 가능하다는 것

## Exception

throw new HttpException

### filter 활용하기

### pipes

ParseIntPipe를 활용하여 타입을 지정해줄 수 있다. 또한, 타입에러가 발생할 경우 예외를 발생시켜준다.

pipe 패턴을 활용하여 유지보수성을 높힐 수 있다.

### Intercepter

AOP기술에서 영감을 받은 기술

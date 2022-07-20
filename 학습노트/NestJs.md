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

### 코드 리뷰

any 타입?
Exception

- nestjs exception filter (사용자 에러 find)
- validate
- server error
  try catch
  TypeORM 옵션들에 대해 살펴보기

### AOP & 데코레이터

================================================================================================================================

- DI / IOC

SOLID원칙의 D에 해당하는 의존성 역전 원칙을 구현하기 위해서는 IoC 컨테이너라는 기술이 필요하다.
프로파이더를 다른 컴포넌트에 주입할 때 사용했던 기술
IOC의 도움으로 객체의 라이프 사이클에 신경쓰지 않아도 된다. 이는 곧 가비지 컬렉터가 알아서 관리해주기 때문에 신경쓰지 않아도 된다. 이로 인해서 코드가 간결해지고 이해하기 쉬워지게 되는 것도 큰 장점이다.

DI는 이렇게 IoC컨테이너가 직접 객체의 생명주기를 관리하는 방식이다.

```
export interface Person {
  getName: () => string;
}

@Injectable()
export class Dexter implements Person {
  getName() {
    return 'Dexter';
  }
}

@Injectable()
export class Jane implements Person {
  getName() {
    return 'Jane';
  }
}

class MyApp {
    private person: Person;
    constructor() {
        this.person = new Dexter();
    }
}


```

```
class MyApp {
    constructor(@Inject('Person') private p: Person) { }
}
```

```
@Module({
  controllers: [UsersController],
  providers: [
    UsersService,
    {
      provide: 'Person',
      useClass: Dexter
    }
  ]
})
...
```

- 프로바이더(provider)
  컨트롤러는 요청과 응답을 가공하고 처리하는 역할을 맡는다.
  하지만 서버가 제공하는 핵심기능은 전달받은 데이터를 어떻게 비즈니스 로직으로 해결하는가?
  즉, 비즈니스 로직을 수행하는 역할을 하는 것이 프로바이더이다. 소프트웨어 구조상 분리해 두는 것이 단일 책임 원칙(SRP)
  프로바이더의 핵심은 의존성을 주입할 수 있다는 것

의존성을 주입하기 위한 라이브러리가 많이 있지만 Nest가 이를 제공 의존성 주입은 OOP에서 많이 활용하고 있는 기법 관심사를 분리할 수 있다.

`Injectable()` 데코레이터를 사용하여 다른 어떤 Nest 컴포넌트에서도 주입할 수 있는 프로바이더가 된다.

별도의 스코프를 지정해 주지 않으면 일반적으로 싱글톤 인스턴스가 생성된다.

속성 기반 프로바이더

```
export class BaseService {
  @Inject(ServiceA) private readonly serviceA: ServiceA;
    ...

    doSomeFuncFromA(): string {
    return this.serviceA.getHello();
  }
}
```

상속관계에 있지 않는 경우 생성자 기반 주입 추천

- 데코레이터 AOP 알아보기
- 인터셉터
- 필터
- Pipe
- 에러 핸들링은 그래서 어느 시점에 하는게 좋은가? (Class-validator는 어느 시점에 하는가?)
- Nest에서 트랜잭션 처리는 어떻게 하는가?
- GraphQL 스키마 코드 비교
- 프론트와 그래서 어떻게 통신하는지?
- 아키텍처(각각의 아키텍처와 SOLID 5원칙에 따른 장단점 비교)
- 테스트(강의 후 어떤 가치관으로 테스트를 해야하고 그에 대한 예제)
- 이전에 키워드 주신 기반으로 다시 발표

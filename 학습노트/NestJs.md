### Nest.js

Nest (NestJS)는 효율적이고 확장 가능한 Node.js 서버 측 애플리케이션을 구축하기 위한 프레임 워크이다.

프로그레시브 JavaScript를 사용하고 TypeScript로 빌드되고 완벽하게 지원하며 OOP / FP / FRP 요소를 사용할수있게 해준다.

### 특징

- 안정성
- 확장성
- 캡슐화
- 구조

### **Lifecycle Events**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ebddca4a-ca69-44c8-9b55-2b4930855cca/Untitled.png)

### 요청 / 응답 생명 주기

1. ncoming request
2. Globally bound middleware
3. Module bound middleware
4. Global guards
5. Controller guards
6. Route guards
7. Global interceptors(pre-controller)
8. Controller interceptors(pre-controller)
9. Route interceptors(pre-controller)
10. Global pipes
11. Controller pipes
12. Route pipes
13. Route parameter pipes
14. Controller(method handler)
15. Service(if exissts)
16. Route interceptor(post-request)
17. Controller interceptor(post-request)
18. Global interceptor(post-request)
19. Exception filters(route, then controller, then global)
20. Server response

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/98c08a72-b973-4de7-8118-bdc03189f514/Untitled.png)

### DI / IOC 순한 참조 알아보기

SOLID원칙의 D에 해당하는 의존성 역전 원칙을 구현하기 위해서는 IoC 컨테이너라는 기술이 필요하다.
프로파이더를 다른 컴포넌트에 주입할 때 사용했던 기술이다.

IOC의 도움으로 객체의 라이프 사이클에 신경쓰지 않아도 된다. 이는 곧 가비지 컬렉터가 알아서 관리해주기 때문에 신경쓰지 않아도 된다. 이로 인해서 코드가 간결해지고 이해하기 쉬워지게 되는 것도 큰 장점이다.

DI는 이렇게 IoC컨테이너가 직접 객체의 생명주기를 관리하는 방식이다.

```markdown
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

========================================================================

class MyApp {
constructor(@Inject('Person') private p: Person) { }
}

========================================================================

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

실제 DI 적용한 코드

```jsx
@Controller("todos")
export class TodoController {
  constructor(
    private readonly todoService: TodoService,
  ) {}

  @Get()
  selectTodos() {
    return this.todoService.getTodos();
  }
```

### Providers

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/61efba66-3755-4c4c-9da3-2cb97cacd9b6/Untitled.png)

컨트롤러는 요청과 응답을 가공하고 처리하는 역할을 맡는다.

하지만 서버가 제공하는 핵심기능은 전달받은 데이터를 어떻게 비즈니스 로직으로 해결하는가이다.

즉, 비즈니스 로직을 수행하는 역할을 하는 것이 프로바이더이다. 소프트웨어 구조상 분리해 두는 것이 단일 책임 원칙(SRP)을 지킬 수 있다.

의존성을 주입하기 위한 라이브러리가 많이 있지만 Nest가 이를 제공 의존성 주입은 OOP에서 많이 활용하고 있는 기법 관심사를 분리할 수 있다.

`Injectable()` 데코레이터를 사용하여 다른 어떤 Nest 컴포넌트에서도 주입할 수 있는 프로바이더가 된다.

별도의 스코프를 지정해주지 않으면 일반적으로 싱글톤 인스턴스가 생성된다.

의존성 주입 방식

1. **생성자 기반 주입 방식**
2. setter 기반 주입 방식
3. **필드 기반 주입 방식**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/452fa41e-a407-4a31-b40f-42346cdcf872/Untitled.png)

### 생성자 기반 주입 방식

```jsx
@Injectable()
export class TodoService {
```

### 속성 기반 주입 방식(필드를 이용한 의존성 주입)

```markdown
export class BaseService {
@Inject(ServiceA) private readonly serviceA: ServiceA;
...

    doSomeFuncFromA(): string {
    return this.serviceA.getHello();

}
}
```

### 커스텀 프로바이더

1. Nest 프레임워크가 만들어주는 인스턴스 또는 캐시된 인스턴스 대신 인스턴스를 직접 생성하고 싶은 경우
2. 여러 클래스가 의존 관계에 있을 때 이미 존재하는 클래스를 재사용하고자 할 때

### Modules

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2cfd5f77-52e5-47bd-a261-03562a91c7a3/Untitled.png)

```jsx
App.module;

@Module({
  imports: [TypeOrmModule.forRoot(typeORMConfig), TodoModule, AuthModule],
})
export class AppModule {}
```

```jsx
TodoModule;

@Module({
  imports: [TypeOrmExModule.forCustomRepository([TodoRepository]), AuthModule],
  controllers: [TodoController],
  providers: [TodoService],
})
export class TodoModule {}
```

- `import`: 이 모듈에서 사용하기 위한 프로바이더를 가지고 있는 다른 모듈을 가져옵니다.
- `controllers` / `providers`: 모듈 전반에서 컨트롤러와 프로바이더를 사용할 수 있도록 Nest가 객체를 생성하고 주입할 수 있도록 해 줍니다.
- `export`: 이 모듈에서 제공하는 컴포넌트를 다른 모듈에서 import 해서 사용하고자 한다면 export 해야 합니다.

### AOP 패턴

**데코레이터**

데코레이터를 잘 사용하면 횡단관심사를 분리하여 관점 지향 프로그래밍을 적용한 코드를 작성할 수 있다.
파이썬의 데코레이터나 자바의 어노테이션과 유사한 기능을 한다.

데코레이터는 타입스크립트 스펙에서 아직 실험적인 기능이라 `experimentalDecorators:true`를 해야 함

데코레이팅 된 선언(데코레이터가 선언되는 클래스, 메서드 등)에 대한 정보와 함께 런타임에 호출되는 함수

```jsx

function deco(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  console.log('데코레이터가 평가됨');
}

class TestClass {
  @deco
  test() {
    console.log('함수 호출됨')
  }
}

const t = new TestClass();
t.test();

============================================================================
function deco(value: string) {
  console.log('데코레이터가 평가됨');
  return function (target: any, propertyKey: string,
descriptor: PropertyDescriptor) {
    console.log(value);
  }
}

class TestClass {
  @deco('HELLO')
  test() {
    console.log('함수 호출됨')
  }
}

```

데코레이터 합성

1. 각 데코레이터의 표현 위에서 아래로 평가됩니다.
2. 아래에서 위로 함수로 호출된다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b95fe923-4296-4f0b-9957-207457a5507e/Untitled.png)

### AOP

백엔드는 사용자의 핵심 기능에 대한 요구사항 뿐만 아니라 유효성 검사, 로깅, 보안, 트랜잭션과 같이 애플리케이션 전반에 걸쳐 제공해야 하는 공통 요소를 포함합니다. 이를 횡단관심사라고 합니다.

소스코드에서 횡단관심사를 따로 분리하여 구현하지 않으면 코드는 읽고 이해하기 힘들게 되고 모듈로서 응집도가 떨어지며 유지보수가 어렵게 된다.

Nest에서는 횡단관심사를 비지니스 로직과 쉽게 분리할 수 있다. 대표적인 컴포넌트로 인터셉터가 있다.

### Pipe

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c20218bc-0cc9-48a5-8254-10340be7e1d5/Untitled.png)

pipe는 exception 구역에서 돌아간다. 이 뜻은, pipe가 예외를 throw할때, exception layer에서 처리된다(global 예외 필터 그리고 현재 context에 적용된 [exceptions filters](https://docs.nestjs.com/exception-filters)
).

위를 감안하면, 예외가 pipe안에서 throw될때, 어떤 컨트롤러 메서드도 그 이후에 실행되지 않는다는 점을 분명히 해야 한다. 이는 system 영역의 외부 소스로부터 애플리케이션 안으로 들어오는 유효한 데이터를 위한 좋은 모범 사례임을 보여준다.

### Nest 트랜잭션 처리

1. QueryRunner를 이용해서 단일 DB 커넥션 상태를 생성하고 관리하기
2. transaction 객체를 생성해서 이용하기
3. @Transaction, @TransactionManager, @TransactionRepository 데코레이터를 사용하기 (권장 X)

QueryRunner 방식은 UnitTest에서 Repository에 대한 Mocking을 할 때 좀 더 수월하게 진행할 수 있다.

**QueryRunner 클래스를 사용하는 방법**

```jsx

private async saveUserUsingQueryRunner(name: string, email: string, password: string, signupVerifyToken: string) {
  const queryRunner = this.connection.createQueryRunner();

  await queryRunner.connect();
  await queryRunner.startTransaction();

  try {
    const user = new UserEntity();
    user.id = ulid();
    user.name = name;
    user.email = email;
    user.password = password;
    user.signupVerifyToken = signupVerifyToken;

    await queryRunner.manager.save(user);

    // throw new InternalServerErrorException(); // 일부러 에러를 발생시켜 본다

    await queryRunner.commitTransaction();
  } catch (e) {
    // 에러가 발생하면 롤백
    await queryRunner.rollbackTransaction();
  } finally {
    // 직접 생성한 QueryRunner는 해제시켜 주어야 함
    await queryRunner.release();
  }
}
```

**transaction 객체를 생성해서 이용하는 방법**

```jsx

private async saveUserUsingTransaction(name: string, email: string,
 password: string, signupVerifyToken: string) {
  await this.connection.transaction(async manager => {
    const user = new UserEntity();
    user.id = ulid();
    user.name = name;
    user.email = email;
    user.password = password;
    user.signupVerifyToken = signupVerifyToken;

    await manager.save(user);

    // throw new InternalServerErrorException();
  })
}
```

### Isolation Level 설정하기

- 첫 번째 매개변수에 격리 수준을 전달한다.
- 종류: `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`

```
await getManager().transaction("SERIALIZABLE", manager => {});
```

`READ UNCOMMITTED` (level 0) : 트랜잭션 처리중 or 아직 commit되지 않은 데이터를 다른 트랜잭션이 읽는 것을 허용

`READ COMMITTED` (level 1) : 커밋된 읽기 (dirty read 방지) 트랜잭션이 commit 되어 확정 된 데이터만을 읽도록 허용

`REPEATABLE READ` (level 2) : 트랜잭션이 완료될 때까지 select 문장이 사용하는 모든 데이터에 `shared lock` 이 걸린다. 따라서 다른 사용자는 해당 영역에 대한 데이터 수정이 불가능하다.

`SERIALIZABLE` (level 3) : 완벽한 읽기 일관성 모드 제공하며 성능 측면에서 동시 처리성능이 가장 낮다. 거의 사용되지 않음!

### API 가드

passport

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/52261dba-d793-41d3-b779-88825acf4fee/Untitled.png)

```jsx
@Injectable()
export class AuthService {
  constructor(private jwtService: JwtService) {}
  jwtCreate() {
    const payload = { email: "rm@kakaostyle.com", sub: "zigzag" };

    return {
      token: this.jwtService.sign(payload),
    };
  }
}
```

```jsx
@Module({
  imports: [
    PassportModule.register({ defaultStrategy: "jwt", session: false }),
    JwtModule.register({
      secret: "secret",
      signOptions: { expiresIn: "1y" },
    }),
  ],
  providers: [AuthService, JwtStrategy],
  exports: [AuthService],
})
export class AuthModule {}
```

```jsx
@Injectable()
export class JwtAuthGuard extends AuthGuard("jwt") {}
```

```jsx
import { PassportStrategy } from "@nestjs/passport";
import { ExtractJwt, Strategy } from "passport-jwt";

export class JwtStrategy extends PassportStrategy(Strategy) {
  constructor() {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      secretOrKey: "secret",
      ignoreExpiration: false,
    });
  }
  async validate(payload) {
    if (payload) {
      return "okay";
    }
  }
}
```

```jsx
@UseGuards(JwtAuthGuard)
```

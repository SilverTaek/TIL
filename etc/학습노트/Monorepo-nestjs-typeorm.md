개발자 향로님의 블로그 필사입니다.

Title : NestJS & TypeORM 환경에서 Monorepo 구성하기 - 기본 환경 구성 및 명려어

https://jojoldu.tistory.com/594?category=635878

본문에서 NestJS는 Spring 중에서도 Spring MVC와 같은 역할을 하는 것이지 Batch / Cloud / Security / Data 등을 모두 지원하는 엔터프라이즈 프레임워크인 Spring 프레임쿼크 전치와 비교하기엔 어렵다고 설명한다.

모노레포 구성을 CLI가 지원하게 때문에 아래의 명령어로 실행한다.

```
npm install -g @nestjs/cli
```

```
nest new monorepo-nestjs-typeorm
```

구조는 apps / libs 인데 apps는 별도의 서버로 배포될 애플리케이션 , libs는 apps에서 이들을 의존해서 사용

nest build api : 배포할 때는 npm install 를 할 필요 없이 CI 서버에서 빌드를 끝내고 각 서버들은 해당 단일 파일을 실행만 하면 된다.

### UserApiController

1. 비동기 함수인 signUp에 생성한 Request dto를 받는다.
2. 그리고 반환은 따로 생성한 Response객체를 반환한다.
3. await 를 사용하여 userApiService를 실행한다. 이때 인자는 dto의 toEntity 메서드를 실행시킨다.
4. 정상적으로 실행된다면 만들어진 ResponseEntity.OK()를 반환한다.
5. 실패한다면(catch) 로거로 에러를 찍는다.
6. 그리고 ResponseEntity 에러 로그를 찍는다.

Deep Dive

모르는 것

- @Expose()
- class-validator를 사용한다. req 클래스에
- @Exclude()
- @ApiProperty

프로젝트에 적용할만 한 것

- js-joda 라이브러리
- deadline 을 transform해서 적용
- Req / Res 응답 객체를 따로 생성해서 관리

# 캐시

- Cache란 자주 사용하는 데이터나 값을 미리 복사해 놓는 임시 장소를 가리킨다. 아래와 같은 저장공간 계층 구조에서 확인할 수 있듯이, 캐시는 저장 공간이 작고 비용이 비싼 대신 빠른 성능을 제공한다.

**메모리 계층 구조**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6a1199a4-c189-4c98-8303-766af8633764/Untitled.png)

**파레토의 법칙** : 원인 중 상위 20%가 전체 결과의 80%를 만든다는 법칙

즉, 20프로의 일을 빠르게 처리하면 80%의 일을 효율적으로 처리할 수 있다.

## Local Cache vs Global Cache

### Local Cache

- Local 장비 내에서만 사용되는 캐시로, Local 장비의 Resource를 이용한다.
- Local에서만 작동하기 때문에 속도가 빠르다.
- Local에서만 작동하기 때문에 다른 서버와 데이터 공유가 어렵다.

### Global Cache

- 여러 서버에서 Cache Server에 접근하여 사용하는 캐시로 분산된 서버에서 데이터를 저장하고 조회할 수 있다.
- 네트워크 I/O가 발생하여 Local Cache에 비해 상대적으로 느리다.
- 별도의 Cache서버를 이용하기 때문에 서버 간의 데이터 공유가 쉽다.

**데이터 지역성의 원리**

- 시간 지역성
  - for문의 int i =0
- 공간 지역성
  - 배열
- 순차 지역성

cache miss / cache hit

CDN

웹 캐시

응답 캐시

프록시 캐시

브라우저 캐시

Redis

- Remote Dictionary Server
- 데이터가 자동으로 지워지지는 않는다.
- Database, Cache, Message broker
- In-memory Data Structure Store
- Supports rich data structure

In-memory Database (Cache)

Database보다 더 빠른 Memory에 더 자주 접근하고 덜 자주 바뀌는 데이터를 저장

Collection

- String
- List
- Set
- Sorted Set
- Hash

서버가 여러대인 경우 Consitency의 문제 발생

멀티 스레드 환경에서 Race Condition 발생

- 여러 스레드가 병합하면서 Context Switching 때문에 기본적으로 싱글 스레드
- Redis 자료구조는 Atomic Critical Section에 대한 동기화를 제공
- 서로 다른 Transaction Read/Write 를 동기화

주의할 점

- 싱글 스레드 서버이므로 시간 복잡도를 고려해야 한다.
- In-Memory 특성상 메모리 파편화, 가상 메모리등의 이해가 필요
- 싱글 스레드?
  - IO - bound Process : 메모리 IO시간을 필요하므로 옵티마이저 효율이 크지 않다.
  - Event Driven
  - Context Switching의 효율이 적다
  싱글 스레드이므로 빨리빨리 처리해야한다.
  따라서 처리가 빨라야 하므로 시간 복잡도 O(N)의 명령어는 주의(KEYS, Flush, GetAll 연산 주의)

메모리 파편화

- 메모리를 할당받고 해제하는 과정에서 부분부분 비어있는 과정이생기는데 실제 물리적 메모리에서 사용하지 못하는 경우→ 이 과정에서 프로세스가 죽을 수 있다. 메모리를 여유있게 사용해야한다.
- 가상 메모리 swap 일부만 올려서 메모리에 올려서 사용하고 디스크에 저장했다가 메모리에 올리는경우 레이턴시가 발생하고 싱글스레드라서 문제가 발생할 가능성이 있다.
- 레플리케이션 - 포크 : 휘발성 메모리 저장소 유실될 문제를 안고있어야한다. 즉 복제 기능을 제공하는데 복사해서 디스크나 다른 곳에 저장한다. 복사가 일어날 때 메모리가 가득 차있다면 복사본이 생성되지 않고 죽는 경우가 발생할 수 있다. → 메모리를 여유있게 사용

- Redis Persistent, RDB, AOF
- Redis Cluster
- Contant Hashing
- Data Grid

- Nest 캐시 적용하기

```tsx
nest new nestjs-cache
npm i cache-manager
npm i -D @types/cache-manager
```

```tsx
@Module({
  imports: [CacheModule.register()],

  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

```tsx
@Injectable()
export class AppService {
  constructor(@Inject(CACHE_MANAGER) private readonly cacheManager: Cache) {}

  async getHello(): Promise<string> {
    await this.cacheManager.set("cached_item", { key: 32 }, { ttl: 10 });
    await this.cacheManager.del("cahced_item");
    await this.cacheManager.reset();
    const cached = this.cacheManager.get("cached_item");
    console.log(cached);
    return "Hello World!";
  }
}
```

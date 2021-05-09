# Cache?
- Cache란 자주 사용하는 데이터나 값을 미리 복사해 놓는 임시 장소를 가리킨다. 아래와 같은 저장공간 계층 구조에서 확인할 수 있듯이, 캐시는 저장 공간이 작고 비용이 비싼 대신 빠른 성능을 제공한다.
![](https://images.velog.io/images/rudus1012/post/b476dc8e-68df-45d9-9671-229f2a764675/image.png)
## Local Cache vs Global Cache
### Local Cache
* Local 장비 내에서만 사용되는 캐시로, Local 장비의 Resource를 이용한다.
* Local에서만 작동하기 때문에 속도가 빠르다.
* Local에서만 작동하기 때문에 다른 서버와 데이터 공유가 어렵다.
### Global Cache
* 여러 서버에서 Cache Server에 접근하여 사용하는 캐시로 분산된 서버에서 데이터를 저장하고 조회할 수 있다.
* 네트워크 I/O가 발생하여 Local Cache에 비해 상대적으로 느리다.
* 별도의 Cache서버를 이용하기 때문에 서버 간의 데이터 공유가 쉽다.

# Spring Cache?
간단하게 이야기하면 db까지 콜이 가지 않도록 하는 것
사용자가 많은 서비스의 경우 몇만건의 select쿼리가 날릴경우 서버 입장에서 부담이 갈 수 밖에 없기때문에 이러한 문제를 해결하고자 spring cache를 사용하여 해결하고자 한다.

현재 프로젝트에서 아직 SessionStorage를 Redis로 지정하지 않았기때문에 ConcurrentHashMap을 활용하고자 한다.

spring boot cache starter를 추가해서 사용할 수 있다.
* ConcurrentHashMap
* caffeine

@EnableCache : 사용하고 싶은 프로젝트에 사용한다.

@Cacheable : 캐시하고 싶은 메서드에 추가한다.

@CacheEvict : 캐시를 제거하고자하는 메서드에 추가한다.



참고 문헌
https://mangkyu.tistory.com/69

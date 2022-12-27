# JPA(Java Persistence API)
- 자바 진영의 ORM 기술 표준

## ORM(ObjectRelationalMapping)
- 객체 관계 매핑
- 관계형 데이터베이스는 관계형 데이터베이스대로 설계
- ORM 프레임워크가 중간에서 매핑
- 대중적인 언어에는 대부분 ORM 기술이 존재

## JPA는 애플맄이션과 JDBC 사이에서 동작

![image](https://user-images.githubusercontent.com/43171179/128598817-9049cf7e-0813-4d4e-9295-4400d1425aa0.png)

## JPA 동작 - 저장

![image](https://user-images.githubusercontent.com/43171179/128598851-2db89420-7ba8-46bc-b519-686d91f3da4c.png)

## JPA 동작 - 조회

![image](https://user-images.githubusercontent.com/43171179/128598865-ff0b93d8-1377-434b-ba24-666cf2c73767.png)

## JPA 사용 이유
- SQL 중심적인 개발에서 객체 중심으로 개발
- 생산성
- 유지보수
- 패러다임의 불일치 해결
- 성능
- 데이터 접근 추상화와 벤더 독립성
- 표준

## JPA의 성능 최적화 기능
- 1차 캐시와 동일성 보장
- 트랜잭션을 지원하는 쓰기 지연
- 지연 로딩

## 1차 캐시와 동일성 보장
- 같은 트랜잭션 안에서는 같은 엔티티를 반환 - 약간의 조회 성능 향상
- DB Isolation Level이 Read Commit이어도 애플리케이션에서 Repeatable Read 보장

## 트랜잭션을 지원하는 쓰기 지연 - Insert
- 트랜잭션을 커밋할 때까지 INSERT SQL을 모음
- JDBC BATCH SQL 기능을 사용해서 한번에 SQL 전송

## 트랜잭션을 지원하는 쓰기 지연 - Update
- UPDATE, DELETE로 인한 로우(ROW)락 시간 최소화
- 트랜잭션 커밋 시 UPDATE, DELETE SQL 실행하고, 바로 커밋

## 지연로딩과 즉시 로딩
- 지연 로딩 : 객체가 실제 사용될 때 로딩
- 즉시 로딩 : JOIN SQL로 한번에 연관된 객체까지 미리 조회


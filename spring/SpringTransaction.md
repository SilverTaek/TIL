# Transaction이란?
* 데이터베이스의 상태를 변환시키는 하나의 논리적 기능을 수행하기 위한 작업의 단위 또는 한꺼번에 모두 수행되어야 할 일련의 연산들을 의미한다.


![](https://images.velog.io/images/rudus1012/post/cc84d123-c291-4c21-9546-f506da4917da/image.png)

예를 들어 현 선물하기 프로젝트에서 회원이 상품을 확인하고 상품의 잔여수량이 충분할때 결제를 진행하고 선물하기 기능 로직으로 넘어가며 상품의 잔여 수량이 감소해야합니다.

그런데 상품 결제하기 단계에서 예외가 발생하여 결재가 진행되지않았는데 선물하기가 된다던가 상품의 잔여 수량이 감소하는 상황이 발생할 수 있습니다. 이러한 상황은 곧바로 엄청난 비용 손실을 유발하는데, 이러한 문제를 해결하기 위해 Transaction 기술이 탄생하였습니다.

## Transaction의 기본 로직
2개 이상의 쿼리를 하나의 커넥션으로 묶어 DB에 전송하고, 이 과정에서 에러가 발생할 경우 자동으로 모든 과정을 원래대로 되돌려 놓습니다. 이러한 과정을 구현하기 위해 Transaction은 하나 이상의 쿼리를 처리할 때 동일한 Connection 객체를 공유하도록 합니다.


# Spring Transaction
Spring은 코드 기반의 트랜잭션(Programmatic Transaction) 처리 뿐만 아니라 선언적 트랜잭션(Declarative Transaction)을 지원하고 있습니다. Spring이 제공하는 트랜잭션 템플릿 클래스를 이용하거나  설정파일, 어노테이션을 이용해서 트랜잭션의 범위 및 규칙을 정의할 수 있습니다. Spring에서는 주로 선언적 트랜잭션을 이용하는데, <tx:advice>태그 또는 @Transactional 어노테이션을 이용하는데(https://velog.io/@rudus1012/Spring-AOP) 이는 Spring AOP로 손쉽게 구현되어 있습니다. 퀴리문을 처리하는 과정에서 에러가 났을 경우 자동으로 Rollback 처리를 해줍니다.

Spring Transaction에는 중요한 키워드들이 있는데 살펴보자.

## Tractional Manager
기존에는 low level로 commit과 rollback 코드를 명시적으로 사용해야했지만 Spring PSA를 바탕으로 구현체를 사용하면 손쉽게 바꿔서 사용할 수 있습니다. 가령 JDBC를 사용하는 DatasourceTransactionManager, JPA를 사용하는 JpaTransactionManager, Hibernate를 사용하는 HibernateTransactionManager처럼 바꿔끼기 용이합니다.

## propagation(전파)
(여러 트랜잭션이 발생할때 합칠거냐 떨어뜨릴거야 결정)
* REQUIRED : 트랜잭션 필요. 진행 중이라면 해당 트랜잭션 사용. 없으면 생성
* MANDATORY : 트랜잭션 필요. 트랜잭션 존재하지 않으면 익셉션 발생
* NEVER : 트랜잭션이 불필요. 진행중인 트랜잭션 존재하면 익셉션 발생
* NESTED : 기존 트랜잭션 존재하면 중첩된 트랜잭션에서 메서드 실행


## isolation level(격리 레벨)
* DEFAULT : 기본 설정
* READ_UNCOMMITED : 다른 트랜잭션에서 커밋하지 않는 데이터 읽기 가능
* READ_COMMITED : 다른 트랜잭션에 의해 커밋된 데이터 읽기 가능
* REPEATABLE_READ : 처음 읽은 데이터와 두 번째 읽은 데이터가 동일
* SERIALIZABLE : 동일한 데이터에 대해 두 개 이상의 트랜잭션 수행 불가
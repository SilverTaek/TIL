Spring 프로젝트에 JPA를 도입하고 싶지만 어디서부터 어떻게 사용해야할지 모르는사람들을 위한 가이드 1편!

물론 JPA를 알기전에 JDBC -> JDBD API -> Mybatis, hibernate 등 알아야할것들이 많지만 이론공부를 할 시간이 없고 당장 프로젝트에 도입해야한다면!? 이것만은 꼭 알고 사용하자!

JPA(Java Persistence API)
# Spring Data JPA 인터페이스
- 공통 인터페이스 : Repository, CrudRepository, PagingAndSortingRepository
- JpaRepository 인터페이스는 JPA에 특화된 기능을 제공하는 인터페이스
![](https://images.velog.io/images/rudus1012/post/21f70276-25ee-4728-b601-00fa48de0b56/image.png)
## CrudRepository
- CRUD 관련 기능들을 제공
## PagingAndSortingRepository
- 페이징 및 sorting 관련 기능들 제공
## JpaRepository
- JPA 관련 특화 기능들 ex) 배치성 작업 + CrudRepository, PagingAndSortingRepository

결론적으로 닭잡는데 소잡는 칼을 쓸필요는 없다. 따라서 단순 CRUD 작업은 CrudRepository
그 외에 페이징, sorting, jpa 특화 기능들을 사용하길 원한다면 JpaRepository를 사용하면 됨들을 사용하길 원한다면 JpaRepository를 사용하면 됨
# 핵심 어노테이션
## @Entity
- 선언된 클래스를 JPA가 관리합니다.
- 필드에 final, enum, interface, class를 사용할 수 없습니다.
- 생성자중 기본 생성자가 반드시 필요
- name : 엔티티 이름을 지정합니다. 기본값으로 클래스 이름을 그대로 사용
## @Table
- 맵핑할 테이블을 지정
### 속성
1. name : 매핑할 테이블의 이름을 지정합니다.

2. catalog : DB의 catalog를 맵핑합니다.

3. schema : DB 스키마와 맵핑합니다.

4. uniqueConstraint : DDL 쿼리를 작성할 때 제약 조건을 생성합니다.
## @Id
- JPA가 객체를 관리할 때 식별할 기본키를 지정

## @GeneratedValue
- 일반적으로 PRIMARY 키의 기본값을 자동으로 생성할때 사용한다.
### 속성
- GenerationType.IDENTITY : 데이터베이스에 키 생성방법을 위임
- GenerationType.AUTO : 각 데이터베이스 방언에 따라 자동으로 지정(기본 값)
- GenerationType.TABLE
- GenerationType.SEQUENCE : 데이터베이스의 시퀀스를 이용해서 키 값을 생성

## Builder 패턴
해당 클래스의 빌더 패턴 클래스를 생성
생성자 상단에 선언 시 생성자에 포함된 필드만 빌더에 포함

HOST - http://localhost:8080/api

# 강의 목록 조회 API

Method: GET
Path: /lecture
QueryString

- teacher_name?: (강사명): "김영한"
- lecture_title?: (강의명): "모든 개발자를 위한 HTTP 웹 기본 지식"
- student_id?: (수강생 ID): 1
- category?: (강의 카테고리명): "db"
- limit?: (제한 갯수): default 20
- next_id?: (다음 아이템 ID)

Response

- 200 OK
  {
  "total_count":2,
  "next_id":2,
  "item_list":[
  {
  "id":2,
  "category":"web",
  "title":"모든 개발자를 위한 HTTP 웹 기본 지식",
  "teacher_name":"김영한",
  "amount":54000,
  "student_amount":1250000,
  "date_created":"1667283949"
  },
  {
  "id":1,
  "category":"web",
  "title":"더 JAVA 8",
  "teacher_name":"백기선",
  "amount":54000,
  "student_amount":1250000,
  "date_created":"1667283949"
  }
  ]
  }

- 200 OK (검색 조건에 해당하는 값이 없을 경우)

{
"total_count":0,
"next_id":null,
"item_list":[]
}

- 400 { "code": "LECTURE_ERROR_100", "message": "잘못된 정보" }
- 500 { "code": "LECTURE_ERROR_999", "message": "일시적으로 사용 불가" }

# 강의 상세 조회 API

Method: GET
Path: /lecture/:lecture_id
Parameter

- lecture_id(강의ID): 1

Response

- 200 OK
  {
  "id":2,
  "title":"모든 개발자를 위한 HTTP 웹 기본 지식",
  "description":"개발자에게 필요한 HTTP 지식을 강의합니다.",
  "category":"web",
  "amount":54000,
  "student_amount":1250000,
  "date_created":"1667283949",
  "date_updated":"1667283949",
  "student_list":[
  {
  "id":1,
  "student_nickname":"알엠",
  "date_registerd":"1667283949"
  },
  {
  "id":2,
  "student_nickname":"단테",
  "date_registerd":"1667283949"
  }
  ]
  }

# 강의 등록 API

Method: POST
Path: /lecture/:teacher_id
Parameter

- teacher_id(강의ID): 1

Body

- title (강의명): "모든 개발자를 위한 HTTP 웹 기본 지식"
- amount (가격): 54900
- description (강의 설명): "개발자에게 필요한 HTTP 지식을 강의합니다"
- category (강의 카테고리): "web"

Response

- 200 OK
  {
  "lecture_id": 12345678,
  }

- 400 { "code": "LECTURE_ERROR_100", "message": "잘못된 정보" }
- 500 { "code": "LECTURE_ERROR_999", "message": "일시적으로 사용 불가" }

# 강의 대량 등록 API

Method: POST
Path: /lecture/:teacher_id
Parameter

- teacher_id(강의ID): 1

Body

- title (강의명): "모든 개발자를 위한 HTTP 웹 기본 지식"
- amount (가격): 54900
- description (강의 설명): "개발자에게 필요한 HTTP 지식을 강의합니다"
- category (강의 카테고리): "web"

Response

- 200 OK
  {
  "lecture_id": 12345678,
  }

- 400 { "code": "LECTURE_ERROR_100", "message": "잘못된 정보" }
- 500 { "code": "LECTURE_ERROR_999", "message": "일시적으로 사용 불가" }

# 강의 수정 API

Method: PUT
Path: /lecture/:lecture_id
Parameter

- lecture_id(강의ID): 1

Body

- title (강의명): "모든 개발자를 위한 HTTP 웹 기본 지식"
- amount (가격): 54900
- description (강의 설명): "개발자에게 필요한 HTTP 지식을 강의합니다"

Response

- 200 OK
  {
  "lecture_id": 12345678,
  "title":"모든 개발자를 위한 HTTP 웹 기본 지식",
  "description":"개발자에게 필요한 HTTP 지식을 강의합니다.",
  "category":"web",
  "amount":54000,
  "student_amount":1250000,
  "date_created":"1667283949",
  "date_updated":"16672849149",
  }

- 400 { "code": "LECTURE_ERROR_100", "message": "잘못된 정보" }
- 500 { "code": "LECTURE_ERROR_999", "message": "일시적으로 사용 불가" }

# 강의 오픈 API

Method: PUT
Path: /lecture/open/:lecture_id
Parameter

- lecture_id(강의ID): 1

Response

- 200 OK
  {
  "result": "SUCCESS",
  }

- 400 { "code": "LECTURE_ERROR_100", "message": "잘못된 정보" }
- 500 { "code": "LECTURE_ERROR_999", "message": "일시적으로 사용 불가" }

# 강의 삭제

Method: DELETE
Path: /lecture/:lecture_id
Parameter

- lecture_id(강의ID): 1

Response

- 200 OK
  {
  "result": "SUCCESS",
  }

- 400 { "code": "LECTURE_ERROR_100", "message": "잘못된 정보" }
- 500 { "code": "LECTURE_ERROR_999", "message": "일시적으로 사용 불가" }

# 수강생(회원) 가입 API

Method: POST
Path: /student

Body

- nick_name (수강생 닉네임): "모든 개발자를 위한 HTTP 웹 기본 지식"
- email (수강생 이메일): "rudus1012@gmail.com"

Response

- 200 OK
  {
  "student_id": 12345678,
  }

- 400 { "code": "LECTURE_ERROR_100", "message": "잘못된 정보" }
- 500 { "code": "LECTURE_ERROR_999", "message": "일시적으로 사용 불가" }

# 수강생(회원) 탈퇴 API

Method: DELETE
Path: /student/:student_id
Parameter

- student_id(수강생 ID): 1

Response

- 200 OK
  {
  "result": "SUCCESS",
  }

- 400 { "code": "LECTURE_ERROR_100", "message": "잘못된 정보" }
- 500 { "code": "LECTURE_ERROR_999", "message": "일시적으로 사용 불가" }

# 강의 수강 신청 API

Method: POST
Path: /student/:student_id/lecture-register

Parameter

- student_id(수강생 ID): 1

Body

- lecture_id_list(강의 ID 리스트): number[]

Response

- 200 OK
  {
  "lecture_list":[
  {"lecture_id":1,
  "lecture_id":2}
  ]
  }

- 400 { "code": "LECTURE_ERROR_100", "message": "잘못된 정보" }
- 500 { "code": "LECTURE_ERROR_999", "message": "일시적으로 사용 불가" }

## 체크 꼭 해야하는 부분

- 조회할 때, date_deleted & display_type
- 응답 클래스 형태로 통일
- 에러 나면 서버 종료되는건 해결
- 서버 시작 시 디비 테이블 생성 -> teacher 더미 데이터 생성
- 메서드 네이밍 다시 확인
- repo에서 쿼리 합칠 수 있으면 합치기 (중복 제거)
- 테스트 코드 짜기 좋은 코드 생각해보기
- 순수 함수 짜는 것 생각 해보기
- SQL 인젝션 처리
- query / execute 차이 확인해보기
- URI 재작성
- 강의 대량 등록 and 수강 신청 대량 시 비동기 처리 확인
- 인덱스 체크(explain)
- 회원 탈퇴하면 자동으로 수강생 숫자도 깎여야하나?
- count \* 로 해야하나?
- any 체크
- package.json 분류하기

## 고민했던 부분

- 수강생 수 로 정렬할 경우 페이지네이션 처리할 때, 기준이 되는 next_id 값을 알기어려움
  ORDER BY student_amount DESC
  LIMIT 20

### 순환참조

- GW 만들어서 해결

### DB Connection vs DB pool

DB Connection

1. MySQL 모듈을 불러온다.
2. DB와 연결한다
3. 쿼리를 실행한다
4. 연결을 끊는다.

DB pool

Connection Pool방식은 미리 연결을 저장해둔 Pool에서 요청이 있을 때 연결을 대여하고 다시 반납받아 저장합니다.

따라서 초기에만 연결 객체가 생성되고, 그 상태를 유지하므로 다시 연결 설정할 필요가 없습니다.

또한 end가 아닌 connection.release()를 사용합니다.
여기서 Connection Pool은 연결을 반납하는 것이지, 해제하지 않는다는 것을 직관적으로 알 수 있습니다.

단일 연결방식과는 다르게 옵션에 connectionLimit가 있습니다.

결과적으로 async await 방식을 사용하기 위해 promise를 사용하였고 connection Poll 방식을 사용하였습니다.

### mysql2 connection pool promise any 타입 문제

- 우선 콜백 함수 지옥을 벗어나기 위해 promise를 사용하면 타입이 any 로 떨어진다.
- 따라서 함수 매칭도 안되고 강제로 선언해주면 마찬가지로 콜백함수 지옥이 시작된다.
- 답은 이것...import mysql from "mysql2/promise";

### 대량 등록에서 등록 메서드를 재사용하려고 했으나 정상적으로 순서가 보장되지 않는 문제 발생

- category / 수강 신청 테이블 분리(정규화) -> 확장성
- soft delete 이유 -> 추후 사용을 고려
- Join 중 InnerJoin 을 사용한 이유 -> 성능 확인
- NoOffSet 페이지네이션 적용한 이유 -> 성능 확인
- 수강생수를 따로 쿼리로 뺀 이유는 쿼리마다 서브쿼리 잘못쓰면 쿼리가 더 나감
- 레이어드 아키텍처
- DB는 mysql
- Docker compose로 작성

### SQL 인젝션 어떻게 막을래?

### 유효성검증할 때, throw 하면 그냥 서버가 다운되어버림

### 대량 등록 시, for문 때문에 비동기 10번이 동시에 실행되는 이슈가 있다. -> 한번씩 실행되다가 에러 하나라도 나면 끝나야 하는데...

### 쿼리 체크해보기 like 인덱스 타는지 explain 결과 분석

## 체크 포인트

- 응답으로 넘어올 때, JSON 객체는 리터럴이다. 클래스의 인스턴스가 아니다.

  - 꼭 외부 API로 받은 값에서만 발생하지 않고, 프론트엔드에서 넘겨준 Request Body 에서도 값과 행위가 함께 응집력 있는 코드가 필요한 경우가 대부분입니다.

- 아무래도 백엔드에서는 번들링에 대한 걱정이 없기 때문에 아래와 같은 이유로 js-joda 를 개인적으로 추천합니다.

- 불변 보장
- 리치 인터페이스
- 변경 실패시 Error 보장
- 타임존 지원

지환 좀 길어요~

- 요구 사항

강의 목록 조회
○ 강사명 / 강의명 / 수강생 ID를 검색어로해서 검색이 가능해야 합니다.
○ 강의 카테고리를 검색 조건으로 사용할 수 있습니다.
■ 전체 카테고리 검색도 가능해야 합니다.
○ 최신순 / 수강생수로 정렬이 가능해야 합니다.
○ 페이징이 되어야 합니다.
○ 목록의 각 객체에는 아래 항목들이 포함되어 있어야 합니다.

■ 강의 ID
■ 강의 카테고리
■ 강의명
■ 강사명
■ 가격
■ 수강생수
■ 강의 생성 일자

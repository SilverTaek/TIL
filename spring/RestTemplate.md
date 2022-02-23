# RestTemplate 이란?

* 스프링에서 제공하는 HTTP 통신 기능을 쉽게 사용할 수 있게 설계되어 있는 템플릿이다.

HTTP 서버와의 통신을 단순화하고 RESTful 원칙을 지킨다.

동기 방식으로 처리되며, 비동기 방식으로는 AsyncRestTemplate이 있다.

## RestTemplate 주요 메소드

|Method|HTTP|설명|
|:---|:---|:---|
|getForObject|GET|GET 형식으로 요청하여 객체로 결과를 반환 받음||
|getForEntity|GET|GET 형식으로 요청하여 ResponseEntity로 결과를 반환 받음||
|postForObject|POST|POST 형식으로 요청하여 객체로 결과를 반환 받음||
|postForEntity|POST|POST 형식으로 요청하여 ResponseEntity로 결과를 반환 받음||
|delete|DELETE|DELETE 형식으로 요청||
|put|PUT|PUT 형식으로 요청||
|patchForObject|PATCH|PATCH 형식으로 요청||
|exchange|any|HTTP 헤더를 생성하여 추가할 수 있고 어떤 형식에서도 사용할 수 있음||


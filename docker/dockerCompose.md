# Docker Compose란?
실행하기 불편하다는 이유로 도커를 포기하기에는 환경 독립성이 주는 장점이 너무 컸나봅니다.
도커가 출시된지 얼마 지나지 않아 독립된 개발 환경을 빠르게 구성할 수 있는 피스 프로젝트가 선보였습니다.
이땜나 해도 도커 명령을 실행하는 서드파티 같은 도구였으나 피그가 인기를 얻자, 도커에서는 피그 프로젝트를 흡수하여 도커 컴포즈라는 이름의 도구로 만들어버립니다.

도커 컴포즈를 사용하면 컨테이너 실행에 필요한 옵션을 docker-compose.yml이라는 파일에 적어둘 수 있고, 컨테이너 간 실행 순서나 의존성도 관리할 수 있습니다.

이후의 과정을 따라하려면, 도커 엔진의 버전이 1.13.1 이상이어야 하고, 도커 컴포즈의 버전은 1.6.0 이상이어야 합니다. 최근에 도커를 설치했다면 큰 문제없이 따라하 실 수 있을겁니다.

Sub-2 명세서에 나와있는 docker-compose.yml 파일을 분석해 봅시다.

```
version: "3.8"
services:
  db:
    image: mysql:5.7
    container_name: ssafy_db
    restart: always
    ports:
      - "32000:3306"
    environment:
      MYSQL_ROOT_PASSWORD: 1235
      TZ: "Asia/Seoul"
    privileged: true
    volumes:
      - ./db:/docker-entrypoint-initdb.d
    networks:
      - backend
  kurento:
    image: kurento/kurento-media-server:latest
    restart: always
    ports:
      - "8888:8888"
    environment:
      TZ: "Asia/Seoul"
      KMS_STUN_IP: "54.180.26.236"
      KMS_STUN_PORT: "3478"
      KMS_TURN_URL: "myuser:mypassword@54.180.26.236:3478?transport=udp"
    networks:
      - backend
  app:
    build: 
      context: ./
    container_name: ssafy_app
    restart: always
    ports:
      - "80:8080"
      - "443:8443"
    environment:
      TZ: "Asia/Seoul"
      SERVER_ADDRESS: "0.0.0.0"
      SPRING_DATASOURCE_URL: "jdbc:mysql://db:3306/ssafy_web_db?useUnicode=true&characterEncoding=utf8&serverTimezone=Asia/Seoul&zeroDateTimeBehavior=convertToNull&rewriteBatchedStatements=true"
      JAVA_TOOL_OPTIONS: "-Dkms.url=ws://kurento:8888/kurento"
    depends_on:
      - db
      - kurento
    networks:
      - backend
networks:
  backend:

```

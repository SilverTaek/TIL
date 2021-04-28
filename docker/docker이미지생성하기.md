# dockerFile을 이용한 도커 이미지 생성하기

## 간단한 dockerfile 예시
```
FROM alpine:3.10
ENTRYPOINT ["echo", "hello"]
```
FROM은 새로운 이미지를 생성할 때 기반으로 사용할 이미지를 지정합니다. 따라서 위 코드는 alpine:3.10 이미지를 기본 이미지로 사용합니다.

Dockerfile을 작성하였으면 docker build 명령어로 이미지를 생성할 수 있다.

```
docker build --tag echoalpine:1.0 .
```

--tag(또는 -t) 옵션은 새로 생성할 이미지 이름을 지정합니다. 
마지막에 점(.)은 Dockerfile의 위치를 경로로 지정합니다. Dockerfile이 아닌 경우 --file(또는 -f)옵션을 사용해서 파일을 지정합니다.

## 주요 명령어
* FROM : 이미지를 생성할 때 사용할 기반 이미지를 지정한다. 예제에서는 openjdk:8-jdk-alpine 이미지를 사용했다. 이 이미지는 알파인 OS에 JDK 8을 설치한 이미지이다.

* RUN : 이미지를 생성할 때 실행할 코드를 지정한다. 예제에서는 패키지를 설치하고 파일 권한을 변경하기 위해 RUN을 사용했다.

* WORKDIR : 작업 디렉토리를 지정한다. 해당 디렉토리가 없으면 새로 생성한다. 작업 디렉토리를 지정하면 그 이후 명령어는 해당 디렉토리를 기준으로 동작한다.

* COPY : 파일이나 폴더를 이미지에 복사한다. 위 코드에서 두 번째 COPY 메서드는 entrypoint.sh 파일을 이미지에 run.sh 이름으로 복사한다. 상대 경로를 사용할 경우 WORKDIR로 지정한 디렉토리를 기준으로 복사한다.

* ENV : 이미지에서 사용할 환경 변수 값을 지정한다. 위 코드는 PROFILE 환경 변수의 값으로 local을 지정했는데 이 경우 컨테이너를 생성할 때 PROFILE 환경 변수를 따로 지정하지 않으면 local을 기본 값으로 사용한다.

* ENTRYPOINT : 컨테이너를 구동할 때 실행할 명령어를 지정한다. 위에서는 run.sh을 실행하도록 설정했다.

## SpringBoot프로젝트 도커 이미지 생성 및 실행
이제는 기존에 작업중이던 SpringBoot jar파일 기준으로 도커 이미지를 생성하고 실행해보는 과정을 진행해보겠습니다.

## SpringBoot Dockerfile 생성
```
FROM openjdk:11 AS builder
RUN mkdir files
VOLUME ["/tmp, /files"]
COPY . .
RUN chmod +x ./gradlew
RUN ./gradlew clean build
FROM adoptopenjdk:11-jdk
COPY --from=builder build/libs/*.jar app.jar
EXPOSE 8197
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]

```

## React NGINX Dockerfile 생성
```
FROM node:12.16.1-alpine as builder
RUN mkdir homepage
WORKDIR /homepage
ADD . .
RUN yarn install
RUN yarn build

FROM nginx:stable-alpine as production
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
RUN true
COPY --from=builder /homepage/build /usr/share/nginx/html
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]
```
## Nginx.conf
```
server {
        listen 80 default_server;
        listen [::]:80 default_server;

		root /usr/share/nginx/html;

		index index.html index.htm index.nginx-debian.html;

        server_name _;

        return 301 https://$server_name$request_uri;

		location / {
			try_files $uri $uri/ /index.html;
		}
}

server {
		listen 80;
		listen [::]:80;

		server_name k4a106.p.ssafy.io;

		return 301 https://$server_name$request_uri;
}

server {
        listen 443 ssl;
        listen [::]:443 ssl;

		root /usr/share/nginx/html;

        index index.html index.htm index.nginx-debian.html;

        server_name k4a106.p.ssafy.io;
        client_max_body_size 50M;

        ssl_certificate /var/jenkins_home/workspace/jenkins_test/sslkey/fullchain.pem;
        ssl_certificate_key /var/jenkins_home/workspace/jenkins_test/sslkey/privkey.pem;

        location / {
                
                alias /usr/share/nginx/html/;
                try_files $uri $uri/ /index.html;
        }

        location /api {
                proxy_pass http://k4a106.p.ssafy.io:8197/;
                proxy_redirect off;
                charset utf-8;

                proxy_set_header Host $http_host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_set_header X-Nginx-Proxy true;
        }
}


```
## Docker 이미지 생성하기
```
$ sudo docker build -t frontend .
$ sudo docker build -t backend .
```

## Docker 컨테이너 생성하기
```
$ sudo docker run -d -p 80:80 frontend
$ sudo docker run -d -p 8197:8197 backend
```

## 실행중인 Docker 컨테이너 확인하기
```
$ sudo docker ps -a
```
## Docker 이미지 삭제하기
```
$ sudo docker rmi {이미지이름}
```
## Docker 컨테이너 삭제하기
```
$ sudo docker rm {컨테이너이름}
```

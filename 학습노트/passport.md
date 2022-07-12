header

payload

signature

login request -> email & password -> secret key -> jwt -> front 에 저장(로컬 스토리지 , http only cookie)

```
header 에다가 jwt를 실어서 api를 전송

jwt 가드를 통해서 jwt strategy를 실행

jwt 시크릿 키를 가지고 디코딩을 진행

유효한 토큰이면 api response
```

결론

1. 유효한 jwt 를 발급받아서 저장시켜 놓는다.
2. 그 저장되어 있는 jwt를 api request 할 때 헤더에 담아서 보낸다.
3. 받을 때 guard -> strategy 를 통해서 인증을 하고 인증이 완료되었는지 처리를 한다.
4. 인증되었다면 response를 한다. 인증되지 않으면 인증되지 않은 키라고 알려준다.

middleware -> guard 순서로 진행

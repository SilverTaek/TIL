# WebSocket?
* 일반적인 Http 통신을 하는 서버들과 달리 채팅 서버는 socket 통신을 하는 서버가 필요하다.
* 통상 Http 통신은 Client의 요청이 있을 때 서버가 응답하고 종료하는 단방향 통신이지만 Socket통신은 Server와 Client가 지속적으로 연결을 유지하고 양방향으로 통신을 하는 방식이다.
* 주로 실시간 처리를 요구하는 서비스에서 많이 사용된다.

## SpringBoot Websocket 서버 구축
### Gradle 라이브러리 추가
```
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springframework.boot:spring-boot-starter-websocket'
    compileOnly 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}
```
### ``Websocket Handler ``
일반적인 Socket 통신은 서버와 클라이언트가 1:N 관계이며 한 서버에 여러 클라이언트가 접속 할 수 있으며, 서버에는 여러 클라이언트가 발송한 메시지를 받아 처리해줄 Handler가 필요합니다.
TextWebSocketHandler를 상속받아 Handler를 작성하여 Client로부터 받은 메시지를 Console Log에 출력하고 Client로 환영 메시지를 보내는 역할을 합니다.
```
@Slf4j
@Component
public class WebSocketChatHandler extends TextWebSocketHandler {

    protected void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
        String payload = message.getPayload();
        log.info("payload {}", payload);
        TextMessage textMessage = new TextMessage("welcome chatting server~");
        session.sendMessage(textMessage);
    }
}
```
### ``Websocket Config``
Handler를 이용하여 Websocket을 활성화하기 위한 Config 파일을 작성합니다.
@EnableWebSocket을 선언하여 Websocket을 활성화합니다. 
Websocket에 접속하기 위한 endpoint는 /ws/chat으로 설정하고 도메인이 다른 서버에서도 접속 가능하도록 CORS : setAllowedOrigins(*)를 설정합니다.
```
@RequiredArgsConstructor
@Configuration
@EnableWebSocket
public class WebsocketConfig implements WebSocketConfigurer {
    private final WebSocketHandler webSocketHandler;

    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(webSocketHandler, "/ws/chat").setAllowedOrigins("*");
    }
}

```
ws://localhost:8080/ws/chat으로 커넥션을 연결하고 메시지 통신을 할 수 있습니다.
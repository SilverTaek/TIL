# WebRTC
    1. MediaStream : 사용자의 카메라 혹은 마이크 등 input 기기의 데이터 스트림에 접근
    2. RTCPeerConnection : 암호화 / 대역폭 관리 기능. 오디오 / 비디오 연결을 한다.
    3. RTCDataChannel : 일반적인 데이터 P2P통신
        1. Signaling을 통해 통신할 peer 간 정보를 교환
        2. WebRTC를 사용해 연결을 맺고, peer의 기기에서 미디어를 가져와 교환
## Node 서버 위에 socket.io를 사용하여 만듬
    1. Session control messages : 통신의 초기화, 종료, 그리고 에러 리포트
    2. Network configuration : 외부에서 보는 내 컴퓨터의 IP 주소와 포트는 ?
        1. ICE 프레임워크를 사용해서 서로의 IP 와 포트를 찾는 과정
        2. Candidate 에 서로를 추가
    3. Media capabilities : 내 브라우저와 상대 브라우저가 사용 가능한 코덱, 해상도?
        1. 미디어 정보 교환은 offer와 answer 로직으로 진행
        2. 형식은 SDP(Session Description Protocol)
    4. 이러한 내용은 스트리밍이 시작되기 전에 완료되어야만 한다.

ICE는 UDP 를 통해 기기들을 서로 직접 연결 시도한다.

1. 연결이 되었습니다. 이제 미디어를 교환합시다.
2. NAT 혹은 방화벽 뒤에 있나봅니다.

기기가 NAT 뒤에 있다면 STUN 서버가 이를 해결해 줄 수 있다.

STUN은 기기의 IP를 알려준다. 기기의 NAT가 직접 연결을 허용하는지 아닌지 파악하는 역할도 한다,.

클라이언트는 STUN 서버에 요청을 보낸다. STUN 서버는 클라이언트의 공인 주소와, 클라이언트가 NAT 뒤에서 접근이 되는지 알려준다.
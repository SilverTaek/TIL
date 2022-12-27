# 젠킨스 시작하기
젠킨스를 처음 실행하게되면 필수적으로 비밀번호를 입력하는 창이 나옵니다. 해당 경로를 통해 비밀번호를 확인하여 입력합니다.
![image](https://user-images.githubusercontent.com/43171179/115992495-f678e780-a608-11eb-9393-41d9e1be8426.png)
```
$ cat /var/jenkins_home/secrets/initialAdminPassword
```
시작하게 되면 필수적으로 필요한 플러그인을 설치하며 시작합니다.
![image](https://user-images.githubusercontent.com/43171179/115992505-0a244e00-a609-11eb-8f0d-bf5db83d0b9f.png)
계정 비밀번호를 입력하여 앞으로 접속할 젠킨스 관리자 계정을 설정합니다.
![image](https://user-images.githubusercontent.com/43171179/115992511-10b2c580-a609-11eb-83e6-ee17ef01795a.png)
앞으로 접속할 젠킨스 URL입니다.
![image](https://user-images.githubusercontent.com/43171179/115992517-17d9d380-a609-11eb-817e-6dc51240b5d5.png)
GitLab과 연동하기위해 GitLab관련 플러그인을 설치하도록 합니다.
![image](https://user-images.githubusercontent.com/43171179/115992528-23c59580-a609-11eb-9fc8-d56a84443ee1.png)
이번엔 GitLab 개인 accestoken을 발급받아 젠킨스와 연동하도록 합니다.
![image](https://user-images.githubusercontent.com/43171179/115992531-2922e000-a609-11eb-9bef-cb57b7695050.png)
젠킨스 설정에서 GitLab항목에서 Credentials를 Add하여 토큰을 등록하여 추가합니다.
![image](https://user-images.githubusercontent.com/43171179/115992542-2e802a80-a609-11eb-84ac-2e3b042823b4.png)
또한 새로운 pipeline item을 생성하여 Pipeline설정을 하도록 합니다.
![image](https://user-images.githubusercontent.com/43171179/115992546-32ac4800-a609-11eb-8984-62fd18f418e6.png)
웹훅 설정을 통해 GitLab에서 Push 이벤트가 발생하면 자동으로 젠킨스가 실행되도록 설정합니다.
![image](https://user-images.githubusercontent.com/43171179/115992551-38099280-a609-11eb-98d1-a35fc172a4c0.png)
마지막으로 GitLab에서 해당 레포지토리 settings에 Integrations의 Secret Token과 URL을 입력하여 push 테스트로 정상적으로 연동이 되었는지 확인합니다.
![image](https://user-images.githubusercontent.com/43171179/115992552-3d66dd00-a609-11eb-8454-f0c8fff28a70.png)
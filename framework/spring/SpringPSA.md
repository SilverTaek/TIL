# PSA (Portable Service Abstraction)
우리는 Spring의 AOP가 Proxy 패턴을 발전시켜 만들어 졌다는것을 이전 포스팅들을 통해서 알게되었습니다. 그리고 FactoryBean을 통해 Proxy가 Bean이 생성될때 자동으로 생성 되는 것 또한 알게 되었습니다.

여기에 우리가 간과하고 있던 사실이 있습니다. @Transactional 어노테이션을 선언하는 것 만으로 별도의 코드 추가 없이 트랜잭션 서비스를 사용할 수 있다는 사실입니다. 그리고 내부적으로 트랜잭션 코드가 추상화되어 숨겨져 있는 것입니다. 이렇게 추상화 계층을 사용하여 어떤 기술을 내부에 숨기고 개발자에게 편의성을 제공해주는 것이 서비스 추상화(Service Abstraction)입니다.

![image](https://user-images.githubusercontent.com/43171179/122998501-1863d000-d3e8-11eb-9843-b59fc25935fb.png)
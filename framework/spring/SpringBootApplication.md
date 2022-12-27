# @SpringBootConfiguration
    1. 기존 @Configuration과 마찬가지로 해당 클래스가 @Bean 메서드를 정의되어 있음을 Spring 컨테이너에 알려주는 역할을 한다.
# @EnableAutoConfiguration
    1. @ComponentScan에서 먼저 스캔해서 Bean으로 등록하고 tomcat등 스프링이 정의한 외부 의존성을 갖는 class들을 스캔해서 Bean으로 등록
# @ComponentScan
    1. @ComponentScan은 해당 어노테이션 하위에 있는 객체들 중 @Component가 선언된 클래스들을 찾아 Bean으로 등록하는 역할을 한다.
    2. 이 때 꼭 @Component가 아니여도 @Component가 선언되어 있는 어노테이션인 @Service, @Repository, @Controller 등등도 포함
    3. @EnableAutoConfiguration이 스캔하기 전에 먼저 @ComponentScan이 진행
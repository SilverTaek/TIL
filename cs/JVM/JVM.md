# JVM 이란?
1. 태초에 문제가 있었다
C/C++ 는 컴파일 플랫폼과 타겟 플랫폼이 다를 경우, 프로그램이 동작하지 않는다.

배포할 때 문제 발생
* 플래폼이 달라질 경우, 타겟 플랫폼에서 프로그램이 동작하지 않는다.

![image](https://user-images.githubusercontent.com/43171179/122680973-012cb300-d22d-11eb-90ea-712bb3b68e47.png)

크로스 컴파일(Cross Compile)
* 타겟 플랫폼에 맞춰 컴파일하는 것을 '크로스 컴파일'이라 한다.

![image](https://user-images.githubusercontent.com/43171179/122681017-3d601380-d22d-11eb-87ea-f36dc8bde385.png)

JVM 으로 문제를 해결

* 자바 바이트코드는 타겟 플랫폼에 상관 없이 JVM 위에서 동작한다.
* 물론, JVM은 타겟 플랫폼에 의존한다.

![image](https://user-images.githubusercontent.com/43171179/122681036-61bbf000-d22d-11eb-9ddf-2cbdf4ec9577.png)

자바 코드가 실행되기까지

![image](https://user-images.githubusercontent.com/43171179/122681105-ae9fc680-d22d-11eb-9f60-7abd367d4170.png)

Runtime Data Areas

![image](https://user-images.githubusercontent.com/43171179/122681163-076f5f00-d22e-11eb-8c88-29116ea6766e.png)

* Method Area, Heap은 스레드가 공유

![image](https://user-images.githubusercontent.com/43171179/122681210-3be31b00-d22e-11eb-98e7-b81ebce3b7a8.png)

![image](https://user-images.githubusercontent.com/43171179/122681227-4f8e8180-d22e-11eb-8833-d1a947c0f006.png)


![image](https://user-images.githubusercontent.com/43171179/122681296-89f81e80-d22e-11eb-86dd-a9c4bc6930e8.png)
![image](https://user-images.githubusercontent.com/43171179/122681304-91b7c300-d22e-11eb-9e96-700bbd1736c2.png)
![image](https://user-images.githubusercontent.com/43171179/122681325-a431fc80-d22e-11eb-876f-b85822213a84.png)


# JVM은 도대체 어떻게 구동될까?
* HotSpot VM의 구조
* JIT 옵티마이저
* JVM의 구동 절차
* JVM의 종료 절차
* 클래스 로딩의 절차
* 예외 처리의 절차

## HotSpot
Java HotSpot Performance Engine
Sun사에서 자바의 성능을 개선하기 위해서 Just In Time(JIT) 컴파일러를 만들었고, 이름을 HotSpot으로 지었다.
HotSpot은 자바 1.3 버전부터 기본 VM으로 사용되어 왔기 때문에, 지금 운영되고 있는 대부분의 시스템들은 모두 HotSpot 기반의 VM이다.

HotSpot VM의 주료 세 가지 컴포넌트
* VM(Virtual Machine) 런타임
* JIT(Just In Time) 컴파일러
* 메모리 관리자

JIT는 우리나라말로 하면 '적절한 시간'이라는 의미이다. JIT를 사용한다는 것은 언제나 자바 메서드가 호출되면 바이트 코드를 컴파일하고 실행 가능한 네이티브 코드로 변환한다는 의미이다.
하지만 매번 JIT로 컴파일을 하면 성능 저하가 심하므로, 최적화 단계를 거치게 된다.

JIT는 애플리케이션에서 각각의 메서드를 컴파일할 만큼 시간적 여유가 많지 않다. 그러므로, 모든 코드는 초기에 인터프리터에 의해서 시작되고, 해당 코드가 충분히 많이 사용될 경우에 컴파일할 대상이 된다. HotSpot VM에서 이 작업은 각 메서드에 있는 카운터를 통해서 통제되며, 메서드에는 두 개의 카운터가 존재한다.

* 수행 카운터(invocation counter) : 메서드를 시작할 때마다 증가
* 백에지 카운터(backedge counter) : 높은 바이트 코드 인덱스에서 낮은 인덱스로 컨트롤 흐름이 변결될 때마다 증가

백에지 카운터는 메서드가 루프가 존재하는지를 확인할 때 사용되며, 수행 카운터 보다 컴파일 우선순위가 높다.

이 카운터들이 인터프리터에 의해서 증가될 때마다, 그 값들이 한계치에 도달했는지를 확인하고, 도달했을 경우 인터프리터는 컴파일을 요청한다.

여기서 수행 카운터에서 사용하는 한계치는 CompileThreshold이며, 벡에지 카운터에서 사용하는 한계치는 다음의 공식으로 계산한다.

compileThreshold * OnStackReplacePercentage / 100

참고 
: XX:CompileThreshold=35000
: XX:OnStackReplacePercentage=80

즉, 메서드가 3만 5천번 호출되었을 때 JIT에서 컴파일을 하며, 백에지 카운터가 3,5000 * 80 / 100 = 28,000 되었을 때 컴파일된다.


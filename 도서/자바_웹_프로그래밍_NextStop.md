# 2장 문자열 계산기 구현을 통한 테스트와 리팩토링
두 번째 양파 껍질을 벗기기 위한 첫 번째 과정으로 추천하는 학습은 테스트와 리팩토링이다.
테스트와 리팩토링은 개발자가 갖추어야 할 중요한 역량이다.

## main() 메소드를 활용한 테스트의 문제점
```
public class Calculator {

	int add(int i, int j) {
		return i + j;
	}

	int subtract(int i, int j) {
		return i - j;

	}

	int multi(int i, int j) {
		return i * j;
	}

	int divide(int i, int j) {
		return i / j;
	}

	public static void main(String args[]) {
		Calculator cal = new Calculator();
		System.out.println(cal.add(3, 4));
		System.out.println(cal.subtract(5, 4));
		System.out.println(cal.multi(2, 6));
		System.out.println(cal.divide(8, 4));
	}
}
```
위와 같은 코드는 여러 문제가 발생할 수 있는데 첫 번째 문제점은 프로덕션 코드와 테스트 코드(main() 메소드)가 같은 클래스에 위치하고 있다는 것이다.
테스트 코드의 경우 테스트 단계에서만 필요하기 때문에 굳이 서비스하는 시점에 같이 배포할 필요가 없다.

이러한 문제를 해결하기 위해 다음과 같이 테스트 코드를 각 메소드별로 분리할 수도 있다.

```

public class CalculatorTest {

	public static void main(String args[]) {
		Calculator cal = new Calculator();

		add(cal);
		subtract(cal);
		multi(cal);
		divide(cal);
	}

	private static void divide(Calculator cal) {
		System.out.println(cal.divide(8, 4));

	}

	private static void multi(Calculator cal) {
		System.out.println(cal.multi(2, 6));

	}

	private static void subtract(Calculator cal) {
		System.out.println(cal.subtract(5, 4));

	}

	private static void add(Calculator cal) {
		System.out.println(cal.add(3, 4));

	}

}
```
하지만 이 또한 최종적인 해결책이 될 수 없다.
위 테스트 코드는 Calculator 클래스가 가지고 있는 모든 메소드를 테스트할 수밖에 없다.
main() 메소드를 활용한 테스트의 이 같은 문제점을 해결하기 위해 등장한 라이브러리가 JUnit이다.
Junit은 내가 관심을 가지는 메소드에 대한 테스트만 가능하다. 또한 로직을 실행한 후의 결과 값 확인을 프로그래밍을 통해 자동화하는 것이 가능하다.

## JUnit을 활용해 main()메소드 문제점 극복

```
public class CalTest {

	@Test
	public void add() {
		Calculator cal = new Calculator();
		System.out.println(cal.add(6, 3));
	}
	
	@Test
	public void multi() {
		Calculator cal = new Calculator();
		System.out.println(cal.multi(2, 4));
	}

}
```

이와 같이 각각의 테스트 메소드를 독립적으로 실행할 수 있기 때문에 현재 내가 구현하고 있는 프로덕션 코드의 메소드만 실행해 볼 수 있다.

## 결과 값을 눈이 아닌 프로그램을 통한 자동화
main() 메소드의 두 번째 문제점은 실행 결과를 눈으로 직접 확인해야 한다는 것이다.
JUnit은 이 같은 문제점을 극복하기 위해 assertEquals() 메소드를 제공한다.

```
import static org.junit.Assert.*;

import org.junit.Test;

public class CalTest {

	@Test
	public void add() {
		Calculator cal = new Calculator();
		assertEquals(9, cal.add(3, 6));
	}

	@Test
	public void subtract() {
		Calculator cal = new Calculator();
		assertEquals(3, cal.subtract(6, 3));
	}

}
```
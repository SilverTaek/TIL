# 함수형 인터페이스와 람다 표현식 1

함수형 인터페이스를 정의한 경우 `@FunctionalInterface` 를 추가해주면 좋다.
* 함수형 인터페이스란 1개의 추상 메소드를 갖는 인터페이스를 말한다.

```
@FunctionalInterface
public interface RunSomething {

    void doIt();

}

```

```
public class Foo {

    public static void main(String args[]) {

        RunSomething runSomething = new RunSomething() {
            @Override
            public void doIt() {
                System.out.println("Hello)";
            }
        }
    }
}

// 람다 표현 식
public class Foo {

    public static void main(String args[]) {

        RunSomething runSomething = () -> {
            System.out.println("Hello");
        };
    }
}
```

Java에서 퓨어하게 함수형 프로그래밍을 하고 싶은 사람들은 값이 변경될 여지가 있는 부분을 주의하면서 사용해야한다.

### Java에서 기본으로 제공하는 함수형 인터페이스

* java.lang.function 패키지
* unction<T, R>
* BiFunction<T, U, R>
* Consumer<T>
* Supplier<T>
* Predicate<T>
* UnaryOperator<T>
* BinaryOperator<T>

고차 함수의 특성을 활용할 수도 있다.


## 람다 표현식

사실상 람다는 scope이 람다를 감싸고 있는 메소드랑 같다 즉, 쉐도잉이 일어나지 않는다.


## 메소드 레퍼런스

콜론이 2개 :: => 스태틱한 방법으로 생성






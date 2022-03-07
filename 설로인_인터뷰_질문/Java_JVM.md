## Q. JVM 에서의 autoboxing 이란 어떤 현상을 말하는 걸까요?
Wrapper classes 와 primitive data type 사에에 이루어 지고 있는 자동 변환 기능을 Autoboxing 과 Unboxing이라 부르고 읽습니다.

Autoboxing은 자바 컴파일러가 pribitive data type을 그에 상응하는 wrapper class로 자동 변환 시켜주는 것을 의미합니다.

예시) 

```
public static void main(String args[]) {
    char ch = 'j';
    autoBoxing(ch);
}

public static void autoBoxing(Character chr) {
    System.out.println("autoboxing test result : chr = ["+chr+"]");
}

```

실행 결과는 아래와 같습니다.

autoboxing test result : chr = [j]

반대로 Unboxing은 자바 컴파일러가 wrapper class를 primitive data type으로 자동 변환 시켜 주는 것을 말합니다.

## Q. interface default implementation 이란? abstract class 를 상속받는 것과 기본 구현을 들고 있는 interface 를 implements 하는것은 어떤 차이가 있나요?

Java8에서 인터페이스에 디폴트 메소드가 생겼습니다. 기존 인터페이스는 메소드 정의만 할 수 있고 구현은 할 수 없었지만 Java8부터 디폴트 메소드라는 개념이 생겨 구현 내용도 인터페이스에 포함시킬 수 있습니다.

추상 클래스와 default를 포함 한 인터페이스의 차이는 없어보이지만 실제로 다음과 같은 차이가 있습니다.

1) 추상 클래스는 public, protected, private 메소드를 가질 수 있지만, 인터페이스는 public만 허용됩니다.
2) 추상 클래스는 멤버변수 선언이 가능하지만 인터페이스는 public static 변수만 선언이 가능합니다.
3) 인터페이스는 implements 키워드로 여러 인터페이스를 구현할 수 있습니다. 반면 추상클래스는 extends 키워드로 1개의 클래스만 상속받을 수 있습니다.

## Q. Java stream method 중 map 과 flatMap 의 차이에 대해 설명해주세요.

## Q. 메소드에서 리스트 타입의 파라미터를 받을 때, ArrayList - List - Collection - Iterable 처럼 구체 타입 뿐 아니라 상위 타입도 받을 수 있습니다. 컬렉션을 받는 어떤 API 를 구현하실 때 구체 타입의 API 디자인을 선호하는지, 추상 타입의 API 디자인을 선호하는지를 설명해 주세요. 왜 그런 선택을 하시나요?

## Q. Java 의 equals 와 == 의 차이에 대해 설명해주세요. Kotlin 의 == 와 === 는 어떤 차이가 있나요?

## Q. 스프링의 @Autowired 를 가급적 쓰지 말라는 이야기가 종종 들리는데 원인이 뭘까요?
결론적으로 필드 주입방식보다 생성자 주입방식이 좋은 점은, 

1. 의존관계 설정이 되지 않으면 객체 생성이 불가하다. => 컴파일 타임에 인지 가능하고 NPE 방지할 수 있다.

2. 의존성 주입이 필요한 필드를 final로 선언가능 => Immutable

3. (스프링) 순환참조 감지가능 -> 순환참조시 앱구동 실패

4. 테스트 코드 작성 용이

라는 장점이 있습니다.

그렇다면, @Autowired를 사용하면 어떤 점이 안좋은지 설명하겠습니다.

필드 주입은 필드에 바로 의존 관계를 주입하는 방법입니다. IntelliJ에서 필드 인젝션을 사용하면 

Field injection is not recoomended라는 경고 문구가 발생합니다.

필드 주입을 이용하면 코드가 간결해져서 과거에 상당히 많이 이용되었던 주입 방법입니다. 하지만 필드 주입은 외부에서 변경이 불가능하다는 단점이 존재합니다. 따라서 테스트 코드의 중요성이 부각됨에 따라 필드의 객체를 수정할 수 없는 필드 주입은 거의 사용되지 않게 되었습니다. 또한 필드 주입은 반드시 DI프레임워크가 존재해야 하므로 가급적 쓰지 말라는 이야기가 들리는 것 같습니다.


## Q. final 키워드를 변수, 메소드, 클래스에 선언하는 것은 어떤 의미가 있습니까?

## Q. synchronized 를 메소드에 선언하는 것과, 특정 객체에 선언하는 것은 어떤 차이가 있습니까?

## Q. Reflection 을 유용하게 사용하는 사례를 말씀해 주세요.

## Q. JDK/JVM 은 대표적으로 OpenJDK 와 Oracle JDK 로 나뉘는데요, 업무에 어떤 JDK 를 사용하시겠습니까? 선택의 이유를 말씀해 주세요.

## Q. hashCode / equals 메소드의 역할에 대해 아시는 내용을 최대한 설명해주세요.

## Q. Java 의 Collections.unmodifiableList 같은 API 를 이용해 List 같은 collection 을 변경 불가능하게 만들 수 있습니다. 그렇다면 이 API 를 사용하면 immutability 를 달성할 수 있을까요?

## Q. 다음 싱글턴 코드의 어떤 점을 개선하실 수 있습니까? (개선이 필요 없을 수도 있음 / 왜?)
```
class MySingleton {
  private static MySingleton instance;

  public static synchronized MySingleton getInstance() {
    if (instance == null) {
        instance = new MySingleton();
    }
    return instance;
  }
}
```
## Q. java 9 이상에 도입된 추가 기능들 중 마음에 드는거 아무거나 하나만 설명해주세요.

## Q. 민감한 정보를 String 으로 저장하는 것과, char[] 또는 StringBuilder/StringBuffer 같은 클래스로 저장하는 것은 어떤 차이가 있나요?

## Q. 크기를 지정하지 않고 ArrayList 를 new 로 생성하면 크기 10의 ArrayList 가 생성됩니다. Array 는 크기를 넘길 수 없는데 반해 ArrayList 는 꽉 찬 List 에 element 를 추가로 더할 수 있습니다. 그렇다면 10개의 element 를 채워넣은 ArrayList 의 11번째 element 을 add 하기위해 어떤 일이 일어나는지 설명해주세요.

## Q. java.lang.String 의 hashCode 구현에 대해 고찰해 봅시다. 왜 그런 구현일지, 문제점은 없을지 이야기해주세요.

## Q. lambda 와 메소드 1개만 있는 익명 클래스 직접 선언은 문법적 차이 외에 어떤 내부적인 차이가 있을까요?

## Q. Java generics 에는 primitive type 을 쓸 수 없는 문제가 있습니다. 왜 그럴까요? 어떻게 해결할 수 있을까요?

## Q. I/O 를 Java nio 로 코딩할 때 주의점은 어떤게 있을까요?

## Q. Java 는 Pure OOP 언어가 아니라고 하는데, 왜 그런 걸까요?

## Q. java.lang.String 의 length 메소드는 정확한 결과를 반환하지 않는 경우가 종종 있습니다. 정확한 의 의미란 무엇이고, 왜 그럴까요?

## Q. Maven 이나 Gradle 이, 의존성 선언한 artifact 들을 찾는 과정에 대해 설명해주세요.

## Q. java.util.Property extends Hashtable, java.util.Stack extends Vector 같은 클래스는 상속으로 망한 대표 사례입니다. 이유를 설명해 주세요.

## Q. Spring boot 가 stereotype annotation 을 붙인 클래스들을 어떻게 찾고 bean 으로 등록하는지 그 과정을 최대한 상세하게 설명해주세요.

## Q. Spring 은 @Transactional 어노테이션 붙인 메소드를 어떻게 찾고 트랜잭션을 처리하나요? 그 내부 구현을 상세하게 설명해 주세요.

## Q. 메소드에 @Transactional 을 붙이는 것과, TransactionTemplate 을 사용해 트랜잭션을 직접 제어하는 것에는 어떤 차이가 있나요? 어떤 방식을 더 선호하시는지 그 이유도 함께 설명해 주시기 바랍니다.
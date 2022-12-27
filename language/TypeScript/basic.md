# TypeScript

* 2012년 MS사에서 출시
* open-source

JavaScript의 동적인 타입에 런타임 에러가 발생하기 때문에 TS를 활용하면 컴파일 시점에 에러를 잡을 수 있다.

더욱 객체지향적으로 프로그래밍 할 수 있다.

컴파일러는 자체 컴파일러나 BABEL을 사용할 수 있다.

## OOP
modern programming

## 공부 방법
* JS에 대한 기본적인 지식

# TypeScript

## 기본 타입

### Boolean
* 참/거짓(true/false) 값
```
let isDone: boolean = false;
```
### Number
* 16진수, 10진수 리터럴에 더불어 2진수, 8진수 리터럴도 지원
```
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
```
### String
* 텍스트 데이터 타입을 string 으로 표현
```
let color: string = "blue";
color = 'red';

```
### Array
* JavaScript처럼 값들을 배열로 다룰 수 있게 해준다.
* let list: number[] = [1, 2, 3];
* let list: Array<number> = [1, 2, 3];

차이는 readonly라고 하면 절대 변ㅂ경할 수 없고 읽을 수 만 있다.
리드온니 다음은 array는 못쓴다.
리드온니가 많이 쓰여서 string[] 을 쓰는게 좋다.


### Tuple -> 타입알리아스 인터페이스 클래스로 대체해서 사용
* 튜플 타입을 사용하면, 요소의 타입과 개수가 고정된 배열을 표현할 수 있다.
서로 다른 타입을 가질 수 있다.
```
// 튜플 타입으로 선언
let x: [string, number];
// 초기화
x = ["hello", 10]; // 성공
// 잘못된 초기화
x = [10, "hello"]; // 오류
```

튜블을 사용하는 것을 권장하지 않음

인덱스 처럼 접근하는게 가독성이 떨어짐

튜블대신에 오브젝트나 클래스 형태로 대신 사용 권장
student.name



### Enum
* 표준 자료형 집합과 사용하면 도움이 될만한 데이터형이다.
```
enum Color {Red, Green, Blue}
let c: Color = Color.Green;
```

### Any
* 사용자로부터 받은 데이터나 서드 파티 라이브러리 같은 동적인 컨텐츠에서 올 수 있다.
```
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false; // 성공, 분명히 부울입니다.
```

무엇이든 할당할 수 있다
가능하면 쓰지 않는 것이 좋다

### Void

아무런 것도 리턴하지 않는다
자동으로 void로 선언되어 있음
변수에 선언해서 사용하지 않는다.

### Null
person 또한 string 이거나 null 만 담을 수 있는 변수

### Undefined

숫자 또는 undefined 아직 결정되지 않는 타입

### unknown

무슨 타입인지 모른다
따라서 쓰지 않는다.
타입이 없는 js랑 사용할 수 있어서 리턴하는 타입이 모를 수 있어서 
왠만하면 쓰지 않는 것이 좋다

### Never
앱에서 어떤 에러를 던질 때
절대절대 리턴할 수 없다
while 문을 돌면서 끝나지 않게 코드를 작성해야함


### Object

어떤 타입의 오브젝트를 담을 수 있다

쓰지 않는 것이 좋다.

### Type assertions
### let

### function

Optional parameter

전달해도 되고 전달하지 않아도 되는 인자
인자 뒤에 ?면 전달할 수 도 있고 않을 수 도 있다.

### Default parameter

내가 썼던 디폴트 파라미터 ㅋㅋ

### Rest parameter

인자 갯수의 상관 없이 쓸 수 있는 것

...numbers: number[]


### Type aliases

기본적인 타입 정의부터 복잡하고 재미쓴 타입을 정의할 수 있다.

type Text = string;
const name: Text = 'taek'

### String literal Types

type Name = 'name';
type JSON = 'json';

-> 쓰는 이유

### union 타입

OR 로 이해하면 충분

type Direction = 'left' | 'right' | 'up' | 'down';

로그인 함수의 리턴은 대부분 promise 비동기로 받아와야하니까

discrimitive union

### intersection

모든 것을 다 합한 것

AND

### enum

여러가지 상수값들을 한 곳에 모아줌

자바스크립트 X

가능한 쓰지 않는 게 좋음

타입 추론을 통해서 타입을 생략할 수 있는데 

이넘으로 타입이 지정된 변수에 다른 어떤 숫자도 할 당할 수 있다는 게 문제이다.

타입이 정확하게 보장되지 않는다.

enum은 스트링 리터럴로 충붆리 대체되어 사용할 수 있음 union 마찬가지

대부분 케이스는 유니언이 대체하여 사용

모바일 네이티브랑 할 때 이넘을 쓰긴 함

### 타입 추론

type inference

let text = 'hello';

선언함과 동시에 타입을 지정했기 때문에 미리 알 수 있음

회색 ... 은 에러는 아니지만 경고

근데 굳이 좋지는 않음

### type assertion

썩 좋지는 않다.

피할 수 있는 방법이 없을까? 하지만 js때문에 불가피하게 사용될 수 있다.

문자열을 확실히 리턴한다고 생각하지만 막상 api를 사용할 수 없다.

(result as string).length
<string> result
장담을 해도 에러나 경고 메시지가 안남 하지만 undefined가 발생할 수 있다.

! 를 작성하면 정말 확신할 때 사용

무조건 널이 아님

함수 뒤에도 사용 100% 사용




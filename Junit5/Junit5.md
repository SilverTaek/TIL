# Junit 5

@BeforeAll // static void로 작성해야 함
static void beforeAll() {
    System.out.println("before all");
}



@AfterAll
static void beforeAll() {
    System.out.println("after all");
}

@BeforeEach
void beforeEach() {
    System.out.println("Before each);
}

@AfterEach
void afterEach() {
    System.out.println("After each);
}

## 테스트 이름 표기법

* 언더바로 작성
* DisplayNameGeneration(DisplayNameGenerator.ReplaceUnderscores.class)

* DisplayName

Assertion

assertAll로 묶어주면 연관 된 모든 테스트를 실행할 수 있다.


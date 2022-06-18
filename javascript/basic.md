# JS 이것만은 알고 가자!

# 역사

1993 : Mosaic Web Browser가 나오게 되는데 웹 브라우저

→ Netscape(Marc Andreessen) : Html / Css 로 페이지를 만들었음

Scripting 언어를 추가하자!

선택지

- Java : 다소 어렵고 무거움
- Scheme(Brendan Eich)하고 10일안에 만들어버림

1994 : Mocha → LiveScript(Interpreter)

LiveScript → JavaScript로 변경 (자바의 인기때문)

1995 : JavaScript

MS가 Reverse engineering 바이너리 분석을 통해 소스코드를 구현

MS가 만든게 JScript를 내놓음

개발자들 고민의 시발점

ECMA한테 찾아가서 네스케이프사가 말함

1997 : ECMAScript1 language specification

2000 : 95% 사용자가 InternetExplorer가 표준이야!

2004 : Moz://a → firefox ActionScript3 Tamarin엔진

Jesse James Garrett : AJAX 도입

개발자들의 커뮤니티 생성

jQuery dojo mootoos 등이 나옴 → 다른 브라우저를 신경쓰지 않게끔

2008 : Google Chrome : JIT 엔진 포함(just-in-time compilation)

2009 : ECMAScript 5

2015 : ECMAScript 6

사용자에게 배포할 때만 JavaScript transcompiler로 변환해서 ECMA5 or ECMA6

= > BABEL

# JS 실행하는 방법

- 기본적으로 Chrome에 V8엔진을 통해서 실행할 수 있다.(개발자 모드 F12)
- Node.js를 설치하여 JS를 실행할 수 있다.

## use strict

- 조금 더 엄격하게 JS 문법을 봐준다.
- 약간의 성능 향상을 기대할 수 있다.

## Node.js REPL

- 간단한 자바스크립트 코드를 실행해 결과를 확인해 볼 수 있다.

1. Js 배열 ?
    1.  const post = { id, text, created_at } 일때 사용할 수 있는 메소드
    2. const post = [ {id}, {text}, {created_at} ] 
    3. a랑 b가 다른지?
    
2. find 와 filter 차이
    1. let 변수가 사용할 수 있는 메소드 확인해보기

1. router에서 API 스펙에 따라서 알아서 post put delete 등을 해주는지 확인하기

1. promise 확인해보기

1. 등호 비교 확인해보기 = / == / ===

1. app.use 살펴 보기
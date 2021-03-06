# 1. 파이썬이란?

## 1. 파이썬이란?

- 폭넓은 사용자층을 가진 프로그래밍 언어

- **장점**

  1. 빠른 학습속도

  2. 명령의 수행 결과를 빠르게 확인 가능
  3. 확장 기능 지원
  4. 다양한 플랫폼에서 사용 가능

- **단점**

  1. 수행 속도가 느림
     - 하지만 성능에 영향을 미치는 부분은 C언어 등으로 모듈화할 수 있어 단점 극복 가능

- 여러 기관 및 산업계에서 사용

- 이용 분야 급격히 증가 -> 빅데이터 분석 / 머신러닝 / 딥러닝 / IoT





## 2. 파이썬의 역사와 종류

- **독립적**이며, 인터프리터 방식의 **객체지향**이고, 동적인 그리고 대화형을 가진 프로그래밍 언어
- **파이썬의 종류**
  1. Cpython : C로 작성된 파이썬 (표준)
  2. IronPython : .Net과 Momo용으로, C#으로 구현
  3. Jython : 자바로 구현된 파이썬, 자바가상머신에서 동작 (자바클래스, 자바 표준 라이브러리 사용 가능)
  4. PyPy : 파이썬으로 구현





## 3. 파이썬의 특징

### 파이썬의 철학

- 아름다운 것이 추한 것보다 낫다

- 명시적인 것이 묵시적인 것보다 낫다

- 단순한 것이 복잡한 것보다 낫다

- 복잡한 것이 난해한 것보다 낫다

- 가독성이 중요하다

  

### 파이썬의 특징

1. 인터프리팅 방식 : 명령의 실행 결과를 대화형으로 바로 확인
2. 동적 타이핑 : 실행 시간 값에 의해 자료형 결정
3. Garbage Collector : 생성된 객체에 대한 메모리 관리는 Garbage Collector 이용
4. 가독성 : 예) 코드블록의 들여쓰기
5. 풍부한 라이브러리 : 표준 라이브러리와 통합환경이 배포판과 함께 제공
   - 정규 표현식
   - 운영 체제의 시스템 호출
   - XML처리
   - 직렬화
   - 각종 통신 프로토콜
   - 전자 메일이나 CSV 파일의 처리
   - 데이터베이스 접속
   - 그래픽 사용자 인터페이스
   - HTML, 파이썬 코드 구문 분석 도구
6. 유니코드
7. 오픈소스 : 파이썬 소프트웨어 재단에서 관리
8. 다양한 프로그래밍 패러다임 지원 : 객체지향, 함수형 프로그래밍 지원
9. 학습 용이성 
   - [프로그램의 문서화]도 언어의 기본 기능에 포함
   - 도움말 문서와 API (운영체제가 제공하는 함수의 집합체)도 체계적으로 정리
   - 읽기 쉽고, 효율적인 코드를 간단하게 쓰려는 철학 반영

10. 내장 스크립트 언어 : 다른 언어로 쓰인 모듈을 연결하는 목적으로 이용되며 많은 상용 프로그램에 내장되어 스크립트 언어로 활용

    

### 파이썬 2.0과 3.0의 차이점

- 파이썬 3.0 : 2.X대 버전과 하위호환성 없음

1. 내장자료형의 내부적인 변화 및 일부 자료형의 구성 요소 제거
2. 표준 라이브러리의 패키지 재배치
3. 향상된 유니코드 지원
4. print문의 print() 함수로의 변화



### 유니코드

대표 코드 : 유니코드 (16bit) / 아스키코드 (7bit)

- **유니코드** : 각 나라별 언어를 모두 표현하기 위해 만든 통합 코드체계 -> 최대 65,536자를 표현 가능
  - 0~9 , A~F를 사용한 16진수를 활용하여 4bit 입력





## 4. 파이썬의 활용 분야

빅데이터, 모바일, IoT, 인공지능 분야에서의 활용 급증

### 파이썬의 인기 분야

1. 웹 애플리케이션 개발 분야
2. 데이터 수집 분야
3. 데이터 과학 및 인공지능 분야

----



# 2. 개발환경과 코드 작성

## 1. 통합개발환경 (IDE)

하나의 환경에서 수많은 개별 작업 가능

**통합 개발 환경** : 코딩을 위한 코드 편집기, 컴파일을 위한 컴파일러(혹은 인터프리터), 디버깅을 위한 디버거 등 프로그램 개발에 필요한 도구들이 하나의 프로그램 개발 환경으로 통합되어 개발 생산성을 높이는 소프트웨어





## 2. 파이참 개발환경 구성

- 파이참 프로젝트 : 파이썬 개발 작업을 통합 관리하기 위한 논리적 개념
  - 파이썬 코드 파일, 각종 리소스 파일 (프로젝트 설정 파일, 멀티미디어 파일 등)로 구성
- 디버깅 : 컴퓨터 프로그램의 정확성이나 논리적인 오류(버그)를 찾아내는 테스트 과정으로 표과적으로 수행하기 위해서는 자동화된 디버거 소프트웨어가 필요함
  - 중단점 지정 -> 프로그램 실행정지 -> 메모리에 저장된 값 확인 -> 실행 재개, 코드 실행





## 3. 비주얼 스튜디오 코드 개발환경 구성





## 4. 파이썬의 코드 작성법

### 코드 작성의 기본

- **들여쓰기** : 알기 쉬운 코드, 가독성이 좋은 코드를 만들기 위해 사용

  - 파이썬 인터프리터에 의해 잘못된 들여쓰기가 검사되지 않으면 치명적인 버그 발생
  - 동일 코드 블록 내 같은 들여쓰기 사용

- **소스코드 인코딩** : #을 추가하면 해당 행 이후의 내용이 주석 처리됨

  - #주석에 작성된 코딩 지시자는 특별한 의미로 해석됨

    -> 소스코드 인코딩 지정

- **세미콜론** : 생략하여 사용 가능

  - 여러 문장을 기술할 경우 문장을 구분하기 위해 필수적으로 ; 사용

- **파일과 모듈**

  - 모듈 : 라이브러리 성격의 기능 / 프로그램의 진입점 역할

----



# 3. 기초 문법의 이해

## 1. 숫자형의 특징

- 리터럴(Literal) : 소스코드 상에서 내장 자료형의 상수 삾을 나타내는 용어

  - 정수형 리터럴 : 15
  - 부동소숫점 숫자형 리터럴 : 3.14
  - 문자열 리터럴 : '파이썬'
  - 부울형 리터럴 : True
  - 리스트형 리터럴 : [1, 2, 3]

- 리터럴의 자료형을 확인할 때는 type() 함수 사용

  - 값에 의해 자료형이 결정되는 동적 타이핑 언어의 성격을 가짐

  - type() 함수의 인자로 해당 리터럴을 전달하면 함수의 반환값으로 자료형의 정보를 얻을 수 있음

    - ```python
      - type(15)
        <class 'int'>
      
      - type(3.14)
        <class 'float'>
      
      - type('파이썬')
        <class 'str'>
      
      - type(True)
        <class 'bool'>
      
      - type([1, 2, 3])
        <class 'list'>
      ```

- **숫자형** : 숫자 리터럴이 사용된 자료형
  - **정수형** : 양의 정수 / 0 / 음의 정수
    - 길이는 무제한이며, 메모리가 허용하는 범위까지 사용 가능
    - 0o 접두어 : 8진수 사용
    - 0x 접두어 : 16진수 사용
    - 0b 접두어 : 2진수 사용
    - 정수형 리터럴 내의 _는 무시됨
  - **부동 소수점형** : 양의 부동소수점 / 음의 부동소수점
    - 소수부 / 정수부 생략 가능
    - 매우 큰 수, 매우 정밀한 수를 표현하기 위해 지수 표기법 사용
    - 부동 소수점형 리터럴 내의 _는 무시됨
  - **허수형** 
    - j 접미사를 사용함 2+3j
    - 허수형 리터럴 내의 _는 무시됨





## 2. 문자열의 특징

- **문자열** : 문자들의 집합
  - "", '' 사용
  - "안녕하세요" : 문자열 길이 5
  - "5" : 문자열 길이 1
  - 파이썬은 자료형으로서의 문자형은 제공하지 않음
  - 큰 따옴표 안에 작은 따옴표를 넣어서 사용 가능
  - 한 따옴표 안에 같은 따옴표를 넣을 수 없음
    - 작은 따옴표 문자 자체를 의미하는 이스케이프 시퀀스 작은 따옴표(|') 문자 조합 사용
    - 큰 따옴표 문자 자체를 의미하는 이스케이프 시퀀스 큰 따옴표(|") 문자 조합 사용
  - """ 문자열 """ / ''' 문자열 ''' : 다중행으로 표현된 문자열 생성
- **이스케이프 시퀀스** : 프로그램의 소스 코드 내에서 사용할 수 있도록 백슬래시(|) 기호와 조합해서 사용하는 사전에 정의해둔 문자 조합으로, 문자열의 출력 결과를 제어하기 위해 사용함
  - || : 백슬래시 (|)
    - 백슬래시 하나를 사용할 경우, 백슬래시와 큰 따옴표의 이스케이프 문자 조합이 또 다른 이스케이프 시퀀스가 됨
  - |' : 작음 따옴표 (')
    - 작은 따옴표는 문자열 리터럴을 만들 때 사용되므로 작은 따옴표 자체를 의미하려면, 백슬래시와의 이스케이프 문자 조합이 필요
  - |" : 큰 따옴표 (")
    - 큰 따옴표는 문자열 리터럴을 만들 때 사용되므로 큰 따옴표 자체를 의미하려면, 백슬래시와의 이스케이프 문자 조합이 필요
  - |n : 라인 피드 - 줄바꿈
  - |t : 수평 탭 - 탭





## 3. 문자열 포맷팅

문자열 내에 사용된 문자열 표시 유형 (문자열 포맷 코드)을 특정 값으로 변경하는 기법

- %-포맷팅, str.format() 함수를 이용한 문자열 포맷팅 제공

### %-포맷팅을 사용한 문자열 포맷팅

- 's' : 문자열 포맷

  - % 다음의 값을 문자열로 변환해 처리하는 기능을 가짐

  - ```python
    "이름 : %s" % "홍길동"
    -> '이름 : 홍길동'
    ```

  - 자료구조 튜플 사용, 각 원소를 인자로 각각의 %s에 전달함

  - ```python
    - "이름 : %s|n나이 : %s 세" % ("홍길동, 20")
      -> '이름 : 홍길동|n나이 : 20세'
    
    - "이름 : %(name)s|n나이 : %(age)s 세" % {"name" : "홍길동", "age" : 20}
      -> '이름 : 홍길동|n나이: 20 세'
    ```

- 'c' : 문자 포맷. 정수를 유니코드 문자로 변환해 출력

- 'd' : 10진 정수로 출력

  - ```python
    "%c => %d" % (97, 97)
    -> 'a => 97'
    ```

- 'o' : 8진수로 출력

- 'x' : 16진수로 출력

  - ```python
    - "%d %o %x" % (10, 10, 10)
      -> '10 12 a'
    
    - "%s %d %x" % ("가", ord("가"), ord("가"))
      -> '가 44032 ac00'
    ```

- 'f' : 부동소수점 숫자로 출력. 소수점 이하 6자리의 정밀도를 기본값으로 지정

  - ```python
    "%f %d" % (3.14, 3.14)
    -> '3.140000, 3' 
    ```

  - %d는 부동소수점에서 정수부만 출력

- '%' : % 문자 자체를 출력

  - ```python
    "%d 점은 상위 %d%%에 속합니다." % (98, 1) 
    -> '98점은 상위 1%에 속합니다.'
    ```



### 문자열 출력 폭과 정렬 방향

- `"%10s" % "우측정렬"` : 문자열의 폭이 10, 정렬의 방향이 우측임

    ->` '_ _ _ _ _ _우측정렬'`

- `"%-10s" % "좌측정렬"` : 문자열의 폭이 10, 정렬의 방향이 좌측임

    -> `'좌측정렬_ _ _ _ _ _'`



### 부동소수점 숫자의 출력 폭 지정, 소수점 이하의 정밀도 표현 적용

- `"%0.2f" % 3.141592` : 부동소수점을 소수점 2자리까지 표시함

  -> `'3.14'`

- `"%10.2f" % 3.141592` : 부동소수점을 포함한 전체 자리수를 10으로 함

  -> `'_ _ _ _ _ _3.14'`

- `"%010.2f" % 3.141592` : 부동소수점을 소수점을 포함한 전체 자릿수는 10, 소수점 이하 두 자리까지 표시하고, 앞의 남은 자리를 0으로 채움

  -> `'0000003.14'`



### str.format() 함수를 이용한 문자열 포맷

- str.format() 함수에서 전달할 인자의 위치 인덱스는 0부터 시작함

  - `"이름 : {0}, 나이 : {1} 세".format("홍길동", 20)`

    -> `'이름 : 홍길동, 나이 : 20세'`

- 위치 인덱스{} 안에 숫자를 넣지 않으면 해당 인자를 순차적으로 적용해 변환된 결과를 생성함

  - `"이름 : {}, 나이 : {} 세".format("홍길동", 20)`

    -> `'이름 : 홍길동, 나이 : 20세'`

- 문자열 내의 {}에서 : 뒤에 문자열 표시 유형을 사용해 포맷 지정

  - `"{0:c} => {1}".format(97, 97)`

    -> `'a => 97'`

- ord() 함수를 통해 정수값을 얻고, 이 정수값에 대한 문자열 변환 실시

  - `"{0}, {1}, {2:x}".format("가", ord("가"), ord("가"))`

    -> `'가, 44032, ac00'`

  - `"{0:f} {1:.2f}".format(3.14, 3,14)`

    -> `'3.140000, 3.14'`

- str.format() 함수에서 이름=값 형식으로 인자를 구성하면 이름을 이용해 인자 전달

  - `"이름 : {name}, 나이 : {age} 세".format(name="홍길동" , age=20)`

    -> `'이름 : 홍길동, 나이 : 20세'`

- `"{0:<10}".format("좌측정렬")` : <는 정렬의 방향이 좌측임을, 10은 출력할 문자열의 폭이 10을 의미함

  -> `'좌측정렬_ _ _ _ _ _'`

- `"{0:>10}".format("우측정렬")` : >는 정렬의 방향이 우측임을, 10은 출력할 문자열의 폭이 10을 의미함

  -> `'_ _ _ _ _ _우측정렬'`

- `"{0:^10}".format("중앙정렬")` : ^는 정렬의 방향이 중앙임을, 10은 출력할 문자열의 폭이 10을 의미함

  -> `'_ _ _중앙정렬_ _ _'`

- `"{0:*^10}".format("중앙정렬")` : *는 공백을 채울 문자, ^는 정렬의 방향이 중앙, 10은 출력할 문자열의 폭이 10을 의미함

  -> `'***중앙정렬***'`



### 부동소수점 숫자 폭, 소수점 이하 정밀도 표현

- `"{0:0.2f}".format(3.141592)`

  -> `'3.14'`

- `"{0:10.2f}".format(3.141592)`

  -> `'_ _ _ _ _ _3.14'`

- `"{0:010.2f}".format(3.141592)` : 전체 자릿수 10, 소수점 이하 두 자리까지 표시, 앞의 남은 자리를 0으로 채움

  -> `'0000003.14'`

- `"{{   {0: .1f}   }}".format(98.5)`

  -> `{98.5}`





## 4. 주석

**주석** : 프로그램의 코드 앞에 #을 붙여 작성된 부분으로, 소스코드에 대한 상세 설명을 달거나 특정 코드를 실행하지 않을 목적으로 사용함

- 인터프리터의 문법 검사에서 무시되고 실행되지 않음

----



# 4. 변수

## 1. 변수

**변수** : 어떠한 값을 저장하는 그릇 / 값을 저장할 때 사용하는 식별자

- 변수명 = 값
  - num : 정수형 변수
  - str : 문자열 변수
  - lst : 리스트 변수
- 파이썬의 동적 타이핑 언어 특징, 저장된 값의 자료형에 의해 변수 자료형 결정
- 변형이 가능한 변수에 의도하지 않은 값이 전달되면, 변수의 자료형이 변경됨
- TypeError와 같은 오류 발생 가능, 변수는 하나의 자료형만을 사용할 것을 권장
- **변수명** : 문자 / 숫자 / _ 의 조합
  - 숫자로 시작하는 변수는 만들 수 없으며, 대소문자는 꼭 구분해야 함
  - 파이썬3부터는 한글 변수명 사용 가능
  - 파이썬의 예약어는 사용할 수 없음
- **변수와 객체** : 변수는 객체에 대한 식별자 역할 수행





## 2. 변수와 자료형

- **Bool** : 참, 거짓을 판단하는 표현식에 사용하는 자료형

  - True 와 False 값을 가짐
  - 관계 연산자, 논리 연산자를 사용하는 표현식이 Bool 값 반환

- **Tuple** : () 안에 서로 다른 자료형의 값을 콤마(,)로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형

  - 0부터 시작하는 인덱스를 이용해 접근할 수 있음
  - 한번 저장된 항목은 변경할 수 없음
    - 같은 변수에 새로운 튜플 객체를 참조하는 것은 문제가 안됨
  - 인덱스를 이용해 튜플의 개별 항목에 접근
    - 두 개의 원소를 갖고 있는 튜플이라면, 유효한 인덱스의 범위는 0~1

- **List** : [] 안에 서로 다른 자료형의 값을 콤마(,)로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형

  - 0부터 시작하는 인덱스를 이용해 접근할 수 있음
  - 한번 저장된 항목이라도 변경할 수 있음
  - 같은 변수에 새로운 튜플 객체를 참조하는 것도 가능
  - 인덱스를 이용해 개별 항목에 접근할 수 있음
    - 두 개의 원소를 갖고 있는 튜플이라면, 유효한 인덱스의 범위는 0~1

- **Set** : {} 안에 서로 다른 자료형의 값을 콤마(,)로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형

  - 순서의 개념이 존재하지 않아 인덱스를 사용할 수 없음
  - 데이터 항목의 중복을 허용하지 않음 -> 하나만 입력
  - 집합의 개념을 가지고 있는 자료구조로 합집합 연산자 제공
  - 새로운 set 객체 참조

- **Dictionary** : {} 안에 키:값 형식의 항목을 콤마(,)로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형

  - 키를 이용해 딕셔너리의 개별 항목에 접근 가능 (1부터 사용)
  - 항목 추가
    - 동일 키가 없음 -> 새로운 항목 추가
    - 동일 키가 있음 -> 저장된 항목 변경

- **None** : null(객체가 존재하지 않는 상태) 객체 상태를 표현함

  - 최초 변수를 선언할 때 초기화를 하지 않으면 에러가 발생함

    -> 초기화 값을 제공하지 않을 경우엔 None 객체 저장 필요

  - 어떠한 값도 저장하고 싶지 않을 경우 None 객체를 저장





## 3. 변수의 생성 및 제거

- **변수의 생성**
  - **=** : 변수는 기본적으로 한 번에 하나씩 생성하지만, 그 이상의 변수를 한 번에 생성할 수도 있음
  - 쉽게 변수의 값 교체 가능
- **변수의 제거**
  - **Garbage Collector** : 객체가 사용한 메모리 공간 자동 관리
  - 개발자가 메모리 관리를 직접할 필요 없음
  - 변수 제거는 del() 함수 이용

----



# 5. 연산자

## 1. 산술, 대입 연산자

### 산술 연산자

| 연산자 | 의미                                  | 예                  |
| ------ | ------------------------------------- | ------------------- |
| +      | 양변의 값을 더하기                    | a = 3 + 2 # a는 5   |
| -      | 양변의 값을 빼기                      | a = 3 - 2 # a는 1   |
| *      | 양변의 값을 곱하기                    | a = 3 * 2 # a는 6   |
| /      | 좌변의 값을 우변의 값으로 나누기      | a = 3 / 2 # a는 1.5 |
| //     | 좌변의 값을 우변의 값으로 나눈 몫     | a = 3 // 2 # a는 1  |
| %      | 좌변의 값을 우변의 값으로 나눈 나머지 | a = 3 % 2 # a는 1   |
| **     | 좌변의 값을 우변의 값으로 제곱        | a = 3 ** 2 # a는 9  |

- 문자형과 숫자형 연산

  - 두 개의 문자열을 연결한 새로운 문자열을 만드는 문자열 접합(+) 연산

    - ```python 
      a, b, c = "2", "3", 4
      print(a + b)
      23
      ```

    - ```python
      a, b, c = "2", "3", 4
      print(int(a) + int(b)) // 문자열을 정수로 변환
      5
      ```



### 대입 연산자

- 변수 선언
- 연산 결과를 변수에 저장
- 함수 반환값을 변수에 저장

| 연산자 | 의미                                                         | 예                     |
| ------ | ------------------------------------------------------------ | ---------------------- |
| =      | 대입(할당)                                                   | a = 3                  |
| +=     | 좌변의 변수에서 우변의 값을 더해서 좌변의 변수에 대입        | a = 3; a += 2 # a는 5  |
| -=     | 좌변의 변수에서 우변의 값을 빼서 좌변의 변수에 대입          | a = 3; a-= 2 # a는 1   |
| *=     | 좌변의 변수에서 우변의 값을 곱해서 좌변의 변수에 대입        | a = 3; a*= 2 # a는 6   |
| /=     | 좌변의 변수에서 우변의 값을 나누어 좌변의 변수에 대입        | a = 3; a/= 2 # a는 1.5 |
| //=    | 좌변의 변수에서 우변의 값을 나눈 몫을 좌변의 변수에 대입     | a = 3; a//= 2 # a는 1  |
| %=     | 좌변의 변수에서 우변의 값을 나눈 나머지를 좌변의 변수에 대입 | a = 3; a%= 2 # a는 1   |
| **=    | 좌변의 변수에서 우변의 값을 제곱해서 좌변의 변수에 대입      | a = 3; a**= 2 # a는 9  |
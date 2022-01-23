# 01. 파이썬 기초

- `type()` : 해당 데이터 타입 확인
- `id()` : 해당 값의 메모리 주소 확인

## 1. **자료형**

- **Boolean Type**

  - True
  - False : 0, 0.0, (), [], {}, '', None
  - `bool()` : 특정 데이터가 True인지 False인지 검증

- **Numeric Type**

  - **int**

    - 8진수 : 0o
    - 2진수 : 0b
    - 16진수 : 0x
    - 지수 표현에서 e(E) = 10

  - **float**

    - 실수의 경우 실제로 값을 처리하기 위해서는 주의

    - `round(값, 소수점 자릿수)` : 0~4는 내림, 짝수에서는 5 내림, 홀수에서는 5 올림

      - `round(3.5 - 3.12, 2)` -> 0.38

    - 실수 빼기 계산 확인

      - ```python
        a = 3.5 - 3.12
        b = 0.38
        
        abs(a - b) <= 1e-10
        ```

      - ```python
        # epsilon : 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
        import sys
        abs(a - b) <= sys.float_info.epsilon
        ```

      - ```python
        import math
        math.isclose(a, b)
        ```

  - **complex**

    - 문자열 '1+2j'를 complex로 변환할 때, 연산자 앞 뒤에 공백 있으면 안됨

- **String Type**

  - immutable : 변경할 수 없음

  - iterable : 순회 가능함

  - ```python
    a = '123'
    for char in a:
        print(char)
        
    => 1
       2
       3
    ```

  - 중첩따옴표

    - 문자열 안에 작은 따옴표를 사용하려면 큰 따옴표로 묶는다.
    - 문자열 안에 큰 따옴표를 사용하려면 작은 따옴표로 묶는다.

  - 삼중따옴표

    - **"""** 사용

    - 문자열 안에 따옴표를 넣을 때 사용

    - 여러 줄에 걸쳐있는 문장을 표현할 때 사용

    - ```python
      print("""문자열 안에 '작은 따옴표'나
      "큰 따옴표"를 사용할 수 있고
      여러 줄을 사용할 때도 편리하다.""")
      
      => 문자열 안에 '작은 따옴표'나
      "큰 따옴표"를 사용할 수 있고
      여러 줄을 사용할 때도 편리하다.
      ```

  - String Interpolation

    - % - formatting

      ```python
      name = '김정현'
      score = 4.5
      
      print('내 이름은 %s' % name) => 내 이름은 김정현
      print('내 학점은 %d' % score) => 내 학점은 4
      print('내 학점은 %f' % score) => 내 학점은 4.500000
      print('내 학점은 %.2f' % score) => 내 학점은 4.50
      ```

    - str.format

      ```python
      print('내 이름은 {}이고, 내 학점은 {}이다'.format(name, score))
      print('내 이름은 {}이고, 내 학점은 {:.2f}이다'.format(name, score))
      ```

    - f-string

      ```python
      print(f'내 이름은 {name}이고, 내 학점은 {score}이다')
      print(f'내 이름은 {name}이고, 내 학점은 {score:.2f}이다')
      ```

      - 형식을 지정할 수 있음
      - 연산과 출력형식 지정도 가능

- **None**

  - 값이 없음을 표현



## 2. 컨테이너

- **시퀀스형**

  - **리스트** : 가변형

    - 마지막 요소는 -1로 접근할 수 있다는 거 잊지 말기

  - **튜플** : 불변형

    - 하나의 항목으로 구성된 튜플은 생성 시 값 뒤에 쉼표를 붙여야 함

      ```python
      a = 1, # 쉼표 안 붙이면 튜플로 인식 못함
      ```

      

  - **레인지** : 불변형

  - **문자형**

  - 패킹 / 언패킹

    - 패킹 : 별 기호 표시된 변수에 리스트로 대입
    - 언패킹 : 튜플 형태로 대입
    - *가 대입식의 좌측에 위치함
    - *가 단항 연산자로 사용됨

- **비시퀀스형**

  - **세트** : 가변형
    - 순서가 없고, 중복된 값이 없음
    - 빈 세트는 `set()` 사용 ({} 사용 불가)
    - {} 사용
    - 차집합 -
    - 합집합 |
    - 교집합 &
    - 순서를 보장하지 않음
  - **딕셔너리** : 가변형
    - {}
    - 빈 딕셔너리는 `dict()` 혹은 {} 사용
    - 순서를 보장하지 않음
    - key는 변경 불가능한 데이터만 가능 -> strind, integer, float, boolean, tuple, range
    - value는 모든 것이 가능
    - `.keys()` : key를 list로 확인해 볼 수 있음
    - `.values()` : value를 list로 확인해 볼 수 있음
    - `.items()` : 딕셔너리 각각의 key와 value가 튜플의 형태로 저장되어 list를 구성



## 3. 연산자

- **산술 연산자**

  - `divmod(a, b)` : a를 b로 나눈 몫과 나머지가 튜플의 형태로 출력

- **비교 연산자**

  - `is` : 객체 아이덴티티
    - 특정 변수가 비어있는지 확인하기 위해서는 x is None을 쓰는 것을 권장
  - `is not` : 객체 아이덴티티가 아닌 경우

- **멤버십 연산자**

  - `in, not in` : 요소가 시퀀스에 속해있는지 확인 가능

- **슬라이싱**

  - ```python
    s = 'abcdefghi'
    print(s[::]) => abcdefghi
    print(s[::-1]) => ihfedcba
    ```



## 4. 프로그램 구성 단위

- 식별자 > 리터럴 > 표현식 > 문장 > 함수 > 모듈 > 패키지 > 라이브러리



# 02. 제어문

## 1. 조건 표현식

- `true_value if <조건식> else false_value`

- ```python
  num = int(input('숫자를 입력하세요: '))
  print('0보다 큼') if num > 0 else print('0보다 작음')
  ```

## 2. for문

- 인덱스로 접근하는 것보다 이런 방식이 나을 수 있음

  ```python
  for i in chrs:
      print(i)
  ```

- for문을 통해 딕셔너리에 접근하면 key를 순회할 수 있음

  - ```python
    for key in dict:
        print(key)
        print(dict[key])
    ```

  - ```python
    for key in dict.keys():
        print(key)
        print(dict[key])
    ```

  - ```python
    for val in dict.values():
        print(val)
    ```

  - ```python
    for key, val in dict.items():
        print(key, val)
    ```

- **`enumerate()`**

  - 인덱스와 값을 함께 활용 가능

  - 열거 객체를 돌려줌

  - ```python
    memebers = ['민수', '영희', '철수']
    for idx, member in enumerate(members):
        print(idx, member)
    ```

  - ```python
    print(list(enumerate(members)))
    => [(0, '민수'), (1, '영희'), (2, '철수')]
    ```

    - ```python
      # enumerate()에 의해 반환되는 인덱스가 1로 시작하여 카운트되는 for 반복문
      for idx, member in enumerate(members, start=1):
          print(idx, member)
      ```

- List comprehension

  - ```python
    # 1~3의 세제곱 리스트 만들기
    cubic_list = []
    for number in range(1, 4):
        cubic_list.append(number ** 3)
    print(cubic_list)
    
    # List comprehension 활용
    cubic_list = []
    list((number**3)) for number in range(1, 4)
    print(cubic_list)
    ```

- Dictionary comprehension

  - ```python
    # 1~3의 세제곱 딕셔너리 만들기
    cubic = {}
    for number in range(1, 4):
        cubic[number] = number**3
    print(cubic)
    
    # Dictionary comprehension 활용
    cubic = {}
    dict({number : (number**3)} for numbers in range(1, 4))
    ```

- Pass : 무시해도 되는 구문

- Continue : 특정 조건일 때는 실행 안하고 다시 반복문으로 돌아감



# 03. 함수

## 1. 함수의 인자

- ```python
  # 입력된 값이 없는 경우 => '익명, 안녕?'
  # 입력된 값이 길동인 경우 => '길동, 안녕?'
  def greeting(a = '익명'):
      return f'{a}, 안녕?'
  ```

- ```python
  print('다섯번째 문장', '마지막 문장', sep='/', end='끝!')
  => 다섯번째 문장/마지막 문장끝!
  ```

- 가변 인자 리스트

  - ```python
    def func(*args):
        # *args : 임의의 개수의 위치인자를 받음
        # 함수 내부에서 tuple 자료형으로 사용됨
    ```

  - 

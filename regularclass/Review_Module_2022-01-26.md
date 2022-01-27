# Review_모듈 _2022-01-26



## 1. 모듈과 패키지

### 1. 모듈과 패키지

- **모듈**
  - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- **패키지**
  - 특정 기능과 관련된 여러 모듈의 집합
  - 패키지 안에는 또 다른 서브 패키지를 포함

### 2. 모듈과 패키지 불러오기

- **import** module
- **from** module **import** var, function, Class
- **from** module **import** * : 전부 import

- **from** package **import** module
- **from** package.module **import** var, function, Class

- ```python
  import random
  
  print(random.sample(range(1, 46), 6))
  ```

- ```python
  # 1. 
  import pprint
  a = {}
  pprint.pprint(a)
  
  # 2.
  from pprint import pprint
  a = {}
  pprint(a)
  ```

-----



## 2. 파이썬 표준 라이브러리

### 1. 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 내장 함수

### 2. 파이썬 패키지 관리자(pip)

- PyPI(Python Package Index) 에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
- 기본 라이브러리 말고도 다른 패키지를 사용하고 싶을 때

### 3. 파이썬 패키지 관리자(pip) 명령어

- **패키지 설치**

  - 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음

  - 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음

  - ```python
    $ pip install SomePackage 
    $ pip install SomePackage==1.0.5 # 특정 버전
    $ pip install 'SomePackage>=1.0.4' # 특정 버전 이상
    # 모두 bash, cmd 환경에서 사용되는 명령어
    ```

- **패키지 삭제**

  - pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌

  - ```python
    $ pip uninstall SomePackage
    ```

- **패키지 목록 및 특정 패키지 정보**

  - ```python
    $ pip list
    $ pip show SomePackage
    ```

- **패키지 freeze**

  - 설치된 패키지의 비슷한 목록을 만들지만, pip install에서 활용되는 형식으로 출력

  - 해당하는 목록을 requirements.txt (관습)으로 만들어 관리함

  - ```python
    $ pip freeze
    ```

  		- 설치된 패키지의 버전을 협업자와 동일하게 만들기 위해

  - **패키지 관리하기**

    - 아래의 명령어들을 통해 패키지 목록을 관리(1)하고 설치할 수 있음(2)

    - 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함

    - ```python
      $ pip freeze > requirements.txt
      $ pip install -r requirements.txt
      ```

- 다양한 파이썬 프로젝트에서 사용됨

----



## 3. 사용자 모듈과 패키지

### 1. 모듈 만들기

- ```python
  # check.py
  NAME = 'APPLE'
  
  def odd(n):
      return n % 2
  
  def even(n):
      return n % 2 == 0
  ```

- ```python
  import check
  check.NAME
  # 'APPLE'
  check.odd(2)
  # False
  
  from check import NAME
  NAME
  # 'APPLE'
  
  from check import *
  NAME
  # 'APPLE'
  odd(1)
  # True
  even(2)
  # True
  ```

### 2. 패키지

- 패키지는 여러 모듈 / 하위 패키지로 구조화
  - 활용 예시 : package.module
- 모든 폴더에는 `__init__.py`를 만들어 패키지로 인식
  - 하위 버전 호환 및 프레임워크 등에서의 동작을 위해 파일을 생성하는 것을 권장

### 3. 패키지 만들기

- 수학과 통계 기능이 들어간 패키지를 아래와 같이 구성

  - math의 tools : 자연 상수 e, 원주율 pi 값, 최대값을 구하는 my_max 함수

  - statistics tools : 평균을 구하는 mean 함수

  - 폴더 구조

    `my_package/`

    ​		`__init__.py`

    ​		`math/`

    ​				`__init__.py`

    ​				`tools.py`

    ​		`statistics/`

    ​				`__init__.py`

    ​				`tools.py`

-----



## 4. 가상환경

### 1. 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야 함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음

### 2. venv

- 가상환경을 만들고 관리하는데 사용되는 모듈
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
  - 특정 폴더에 가상 환경이 (패키지 집합 폴더 등) 있고
  - 실행 환경 (예 - bash)에서 가상환경을 활성화 시켜
  - 해당 폴더에 있는 패키지를 관리 / 사용함

### 3. 가상환경 생성

- 가상환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨
- `$ python -m venv <폴더명>`

### 4. 가상환경 활성화 / 비활성화

- <venv>는 가상환경을 포함하는 디렉토리의 경로
- 가상환경 비활성화는 `$ deactivate` 명령어를 사용


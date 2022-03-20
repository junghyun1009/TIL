# 과목평가 5회차 (Framework)



## Web Framework

- Django : 파이썬 웹 프레임워크

- **Web**
  - **Static web page (정적 웹 페이지)**
    - 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
    - 서버가 정적 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄 (클라이언트 : 네트워크 환경을 통해서 정보나 서비스 요청, 웹 브라우저 / 서버 : 네트워크 환경을 통해서 정보나 서비스 제공)
      - 클라이언트 --요청--> 서버
      - 클라이언트 <--응답-- 서버
    - **모든 상황에서 모든 사용자에게 동일한 정보 표시**
    - 일반적으로 HTML, CSS, JavaScript로 작성
  - **Dynamic web page (동적 웹 페이지)**
    - 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
    - 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
    - 서버 사이드 프로그래밍 언어 사용(파이썬, 자바, C++), 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐

- **Framework**
  - 재사용할 수 있는 수많은 코드를 프레임워크로 통합
  - 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 됨
  - 성격 : Opinionated (다소 독선적)
  
- **Web Framework**
  - 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적

- **Framework 구조**

  - MVC Design Pattern (Model-View-Controller)
  - 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있음
  - Django는 **MTV Pattern**이라고 함
    - **Model**
      - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리 (추가, 수정, 삭제)
    - **Template**
      - 파일의 구조나 레이아웃을 정의
      - 실제 내용을 보여주는 데 사용
    - **View** (중요)
      - HTTP 요청을 수신하고 HTTP 응답을 반환
      - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
      - template에게 응답의 서식 설정을 맡김

  - ```python
    1. HTTP 요청을 받음
    2. urls.py에서 받아들여 적절한 view로 보내줌
    3. views.py에서 필요한 경우 model과 상호작용하거나 template을 읽어옴
    4. HTTP 응답을 보냄(html의 형태)
    ```

---



## Django Intro

- ```python
  1. 가상환경 만들기 (독립적인 개발환경 만들기)
  	python -m venv venv
  2. 가상환경 활성화
  	source venv/Scripts/activate
  3. django 설치
  	pip install django==3.2.12
  4. 프로젝트 생성
  	django-admin startproject 프로젝트이름 .
      (프로젝트 이름은 python이나 django 내부에서 사용중인 키워드, -은 사용하면 안됨)
  5. 서버 열기
  	python manage.py runserver
  6. 애플리케이션 생성
  	python manage.py startapp 앱이름
      (앱 이름은 복수형으로 하는 것을 권장)
  ```

- **프로젝트 구조**
  - _ _ init.py _ _ : python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시
  - asgi.py : django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움 (배포)
  - settings.py : 애플리케이션의 모든 설정을 포함
  - urls.py : 사이트의 url과 적절한 views의 연결을 지정
  - wsgi.py : django 애플리케이션이 웹 서버와 연결 및 소통하는 것을 도움
  - manage.py : django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티


- **애플리케이션 구조**
  - _ _ init.py _ _
  - admin.py : 관리자용 페이지를 설정하는 곳
  - apps.py : 앱의 정보가 작성된 곳
  - models.py : 앱에서 사용하는 Model을 정의하는 곳
  - tests.py : 프로젝트의 테스트코드를 작성하는 곳
  - views.py : view 함수들이 정의되는 곳


- **프로젝트**
  - 애플리케이션의 집합


- **애플리케이션**
  - 실제 요청을 처리하고 페이지를 보여주는 등의 역할
  - 일반적으로 하나의 역할 및 기능 단위로 작성
  - 반드시 생성 후 INSTALLED_APPS에 등록해야 함
  - INSTALLED_APPS에 등록할 때 권장 순서
    - local apps (우리가 만든 앱)
    - third party apps (pip install 등으로 설치한 앱)
    - django apps (장고 내 기본 앱)

---



## 요청과 응답

- **URLs**

  - url 작성할 때 ' / ' (엔드 슬래시) 꼭 써주기

  - trailing comma 작성 권장

  - ```python
    urlpatterns = [
        path('url/', 요청 보낼 view),
        path('index/', views.index),
    ]
    ```

- **Views**

  - 꼭 request 인자를 받아야 함 (요청 객체의 정보 넘어옴)
  - 템플릿 render해서 반환


- **Templates**
  - Template 파일 경로의 기본 값은 app 폴더 안의 templates 폴더로 지정되어 있음

---



## Template

- **Django Template Language (DTL)**
  - 조건, 반복, 변수 치환, 필터 등의 기능
  - python 코드로 실행되는 것이 아님

- **DTL Syntax**

  - **{ { variable } }**

    - render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용

      - render()의 세번째 인자로 { 'variable' : value }와 같이 딕셔너리 형태로 넘겨줌
      - 'variable'로 value에 접근

    - 변수명은 영어, 숫자, _ (맨 앞에 오면 안됨)의 조합

    - `random.choice(a)` : a의 요소 중에서 랜덤으로 하나 뽑아줌

    - . 을 사용하여 변수 속성에 접근 가능

      - ```python
        foods = ['a', 'b', 'c']
        info = {
            'name' : 'Alice',
        }
        context = {
            'foods' : foods,
            'info' : info,
        }
        return render(request, 'greeting.html', context)
        ```

      - ```html
        <!--딕셔너리 이름.키 값-->
        <p>
            안녕하세요 저는 {{ info.name }}입니다.
        </p>
        <!--인덱스 접근도 가능-->
        <p>
            제가 가장 좋아하는 음식은 {{ foods.0 }}입니다.
        </p>
        ```

  - **{ { variable | filter } }**
    - 표시할 변수를 수정할 때 사용
    - `{{ name | lower }}` : name 변수 안에 있는 것을 모두 소문자로 변환
    - `{{ pick | length }}` : pick의 길이를 반환해줌
    - `{{ foods | join:', ' }}` : foods라는 리스트 안에 있는 요소 각각에 ', '을 더하여 반환
    - 여러 개의 필터를 연결하는 것도 가능 (chained)

  - **{ % tag % }**
    - 반복, 논리 연산 수행
    - 일부 태그는 시작과 종료 태그가 필요
      - **{ % if % }{ % endif % }**
        - `{ % if forloop.first % }` : 첫 반복일 때만 수행 (나머지는 `{ % else % }` 안에 있는 것 수행)
      - **{ % for  in % }{ % endfor % }**
        - `{{ forloop.counter }}` : 인덱스 1부터 번호를 매기면서 써줌
        - `{{ forloop.counter0 }}` : 인덱스 0부터 번호를 매기면서 써줌
        - `{ % empty % }` : 객체가 비었다면 특정한 일 수행하도록

  - **주석**
    - 한 줄 주석 `{ # # }`
    - 여러 줄 주석 `{ % comment % }{ % endcomment % }`

  - 기타
    - 연산 : add만 가능
      - `{{ 4 | add:6 }}` 하면 10 반환
      - 연산할거면 view 함수에서

- **템플릿 상속**
  - 사이트의 모든 공통 요소 포함
  - 하위 템플릿이 재정의할 수 있는 블록 정의
  - `{ % extends '' % }`
    - 반드시 템플릿 최상단에
  - `{ % block 이름 % }{ % endblock % }`
  - base.html을 인식하게 하기 위해 추가 템플릿 경로 등록해주기
    - settings.py > `TEMPLATES > 'DIRS' : [ BASE_DIR / 'templates', ]`
      - BASE_DIR : 장고 프로젝트를 포함하고 있는 최상단 폴더
    - 원래는 앱 폴더 내의 templates 폴더만 확인함
  - base.html 안에 nav 넣고 싶으면 앱 > templates 안에 _nav.html 만들어주고 base.html에서 body 태그 안에 `{ % include '_nav.html' % }` 도 가능

- **Django Template System (설계 철학)**
  - 표현과 로직을 분리
    - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
  - 중복을 배제
    - 상속

---



## HTML Form

- **form**

  - 사용자 정보를 입력하는 여러 방식 제공, 사용자로부터 할당된 데이터를 서버로 전송

  - 핵심 속성
    - **action** : 입력 데이터가 전송될 URL 지정
    - **method** : 입력 데이터 전달 방식 지정

- **input**
  - 사용자로부터 데이터를 입력 받기 위해 사용
  - 핵심 속성
    - **name** 
      - name이라는 이름에 설정된 값을 넘겨서 가져올 수 있음
      - GET / POST 방식으로 서버에 전달하는 파라미터로 매핑
        - GET : `?key=value&key=value` 형식으로 데이터 전달

- **label**
  - 사용자 인터페이스 항목에 대한 설명
  - input 요소와 연결하기
    - input의 id 속성과 label의 for 속성 맞춰주기
      - **for**
        - for 속성의 값과 일치하는 id를 가진 문서의 첫 번째 요소 제어
      - **id**
        - 고유해야하는 식별자 정의

- **HTTP**
  - HyperText Transfer Protocol
  - 웹에서 이루어지는 모든 데이터 교환의 기초
  - 수행할 작업을 나타내는 request methods를 정의
    - GET, POST, PUT, DELETE
    - **GET**
      - 서버로부터 정보 조회
      - 데이터를 가져올 때만 사용해야 함
      - 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송

---



## URL

- 웹 애플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작됨
- **Variable Routing**
  - URL 주소를 변수로 사용, view 함수의 인자로 넘길 수 있음

- URL Path converters
  - **str**
    - 비어 있지 않은 모든 문자열과 매치 (' / ' 제외)
    - 작성하지 않을 경우 기본값
  - **int**
    - 0 또는 양의 정수와 매치
  - **slug**
    - ASCII 문자, 숫자, -, _ 로 구성된 모든 문자열과 매치 

- App URL mapping
  - 모든 것을 프로젝트의 urls.py에서 관리하는 것은 유지보수에 좋지 않음
  - **각 app에 urls.py 작성**
  - `include()`
    - 다른 URLconf (app1/urls.py)들을 참조할 수 있도록 도움
    - `include()`를 만나면 URL의 그 시점까지 일치하는 부분을 잘라내고, include된 URLconf로 전달
  - 명시적 상대경로(`from .module import..`) 권장

- Naming URL Patterns
  - path() 함수의 name 인자 정의해서 사용
  - url 태그 사용해서 path() 함수에 작성한 name 사용
    - `{ % url '' % }`
      - 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소 반환
      - DRY 원칙 위반하지 않으면서 링크 출력

---



## Namespace

- 서로 다른 앱의 같은 이름을 가진 url name은 이름 공간을 설정해서 구분

- templates, static등은 정해진 경로 하나로 모아서 보기 때문에 중간에 폴더를 임의로 만들어 줌으로써 이름 공간을 설정
  - 장고에서 약속된 경로는 `앱 > templates`
  - 그래서 그 이후의 경로만 작성
  - 같은 이름의 경로가 있다면 첫번째에 등록된 앱의 경로로만 이동하게 됨

- `app_name` 설정
  - url 태그 안에 `{ % url '앱 이름:index' %}`로 작성
  - templates 폴더 안에 앱 이름과 같은 이름의 폴더를 만들어 html 파일들 이동시켜주기
  - `'앱(폴더) 이름/index.html'`로 바꿔주기



## Static files

- **static file**

  - 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일

  - ```python
    1. INSTALLED_APPS에 django.contrib.staticfiles 포함되어 있나 확인
    2. settings.py에서 STATIC_URL 정의
    3. 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL을 빌드
    	{ % load static % }
        <img src="{ % static 'my_app/example.jpg' % }" alt="My image">
    4. 앱의 static 디렉토리에 정적 파일을 저장
    	my_app/static/my_app/example.jpg (템플릿이랑 비슷)
    ```
    

- **staticfiles app** (settings.py에서 수정하기)

  - ```python
    1. STATICFILES_DIRS = [BASE_DIR / 'static']
    	- 추가적인 정적 파일 경로 목록 정의
    2. STATIC_URL = '/static/'
    	- STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL
        - 개발단계에서는 기본 경로 및 STATICFILES_DIRS에 정의된 추가 경로 탐색
        - 실제 파일이나 디렉토리가 아님
        - 이미지 URL을 만들어줌
    3. STATIC_ROOT
    	- 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
        - settings.py에서 DEBUG = True라고 되어있으면 적용 안됨 (개발 단계)
    ```


- **static file 가져오기**
  - `{ % load static % }
     <img src="{ % static 'my_app/example.jpg' % }" alt="My image">`
  - `load`
    - 사용자 정의 템플릿 태그 세트를 로드 (static 태그가 빌트인 태그가 아니어서)

  - `static`
    - STATIC_ROOT에 저장된 정적 파일에 연결 (개발 단계에서는 기본 경로에서 찾아옴)

  - 장고에서 정적 파일 가져오려면 무조건 static 태그 사용해야 함


# 내가 정리하는 Django



## 1. 장고 프로젝트 생성 및 확인

1. 가상환경 생성 및 활성화
   - `python -m venv venv`
   - `source venv/Scripts/activate` (VS code 열 때마다 활성화)
2. django 설치
   - `pip install django==3.2.10`
3. 프로젝트 생성
   - `django-admin startproject 프로젝트이름 .`
4. 서버 켜서 로켓 확인하기
   - `python manage.py runserver`
5. 서버 끄고 싶을 땐 ctrl + c



## 2. 프로젝트

- **프로젝트 구조**
  - pjt 폴더 내부
    - _ _ init _ _.py : 파이썬 모듈인 것을 인식하게 해줌
    - asgi.py : 만질 일 없음
    - settings.py : 모든 설정
    - **urls.py** : 사이트의 url과 적절한 views의 연결을 지정
      - urls와 또다른 urls 파일 연결도 가능
    - wsgi.py : 만질 일 없음
  - venv 폴더 내부
    - **manage.py** : 장고 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티



## 3. 애플리케이션

- `python manage.py startapp 앱이름` 으로 앱 생성하기
  - 일반적으로 애플리케이션 명은 복수형으로 하는 것을 권장
- 앱 생성 후 settings.py 내 INSTALLED_APPS에 추가해주기 (내가 추가한 걸 위에 넣어준다)



## 4. 요청과 응답

### URLs

- HTTP 요청(request)을 알맞은 view(애플리케이션에 있음)로 전달

- ```python
  # 프로젝트 폴더 내 urls.py
  
  from django.contirb import admin
  from django.urls import path
  from articles import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('index/', views.index),
  ]
  ```

### View

- HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성

  - 하나의 html 문서 (html response 형태)로 만들어 줌

- Template에게 HTTP 응답 서식을 맡김

  - html 파일에 작성

- ```python
  # 각 애플리케이션 폴더 내 views.py
  
  from django.shortcuts import render
  
  def index(request):
      return render(request, 'index.html')
  	# return render(A, B, C)
      # A : index 함수의 변수 그대로 가져옴
      # B : 템플릿 (html 파일)
      # C : views에서 가공한 데이터를 C에 담아서 템플릿으로 넘겨주기 위한 창구
  ```

- 


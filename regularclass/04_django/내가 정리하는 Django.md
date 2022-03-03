# 내가 정리하는 Django



## 1. 장고 프로젝트 생성 및 확인

1. 가상환경 생성 및 활성화
   - `python -m venv venv`
   - `source venv/Scripts/activate` (VS code 열 때마다 활성화)
2. django 설치
   - `pip install django==3.2.10`
3. 프로젝트 생성
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

- 프로젝트 앱 : 프로젝트 명과 같은 이름의 앱이
- `python manage.py startapp 앱이름` 으로 앱 생성하기
- settings.py 내 INSTALLED_APPS에 추가해주기 (내가 추가한 걸 위에 넣어준다)
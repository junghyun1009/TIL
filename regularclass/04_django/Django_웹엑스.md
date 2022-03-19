# Django_웹엑스



## Model

- **Model**

  - 사용자가 지정하는 데이터들의 필수적인 **필드**들과 **동작**들을 포함

  - 저장된 데이터베이스의 구조

  - **장고는 model을 통해 데이터에 접속하고 관리**

  - 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑됨
  - **웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구**

- **데이터베이스(DB)**
  - 체계화된 데이터의 모임
  - 기본 구조
    - **스키마**
      - 데이터베이스의 구조
      - 데이터베이스의 제약조건 (자료의 구조, 표현방법, 관계)
    - **테이블** : 데이터 요소들의 집합
      - 열 (column) : 필드 / 속성 => 고유한 데이터 형식 지정
      - 행 (row) : 레코드 / 튜플 => 데이터 저장
      - **PK (기본키)** : 각 행의 고유값

- **쿼리**
  - 데이터를 조회 / 추출 / 조작하기 위한 명령어

---



## ORM

- Object-Relational-Mapping
- **객체 지향 프로그래밍 언어**를 사용하여 호환되지 않는 유형의 시스템 간에 (장고-SQL) 데이터를 변환하는 기술
- 파이썬을 이용하여 DB 조작을 가능하게 함 => **DB를 객체로 조작하기 위해 사용**
- 장점
  - SQL을 잘 알지 못해도 DB 조작 가능
  - 객체 지향적 접근으로 인한 높은 생산성
- 단점
  - ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음
  - 효율성이 조금 떨어짐

### models.py

- 각 모델은 django.models.Model 클래스의 서브 클래스

  - ```python
    class Article(models.Model):	# django.db.models 모듈의 Model 클래스 상속받음
        # models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지
        title = models.CharField(max_length=10)
        content = models.Textfield()
        # title과 content는 모델의 필드
        # 각 필드는 클래스 속성으로 지정, 각 속성은 각 db의 열에 매핑
    ```

  - ```python
    CharField(max_length=None, **options)
    	- 길이의 제한이 있는 문자열 넣을 때
    	- max_length는 필수 인자
    
    Textfield(**options)
    	- 글자의 수가 많을 때 사용
    ```

---



## Migrations

- 장고가 model에 생긴 변화를 반영하는 방법

- ```python
  1. makemigrations (python manage.py makemigrations)
  	- model을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용
      
  2. migrate (python manage.py migrate)
  	- 마이그레이션을 DB에 반영하기 위해 사용
      - model에서의 변경 사항들과 DB의 스키마가 동기화를 이룸
      
  3. sqlmigrate (python manage.py sqlmigrate 설계도이름)
  	- 마이그레이션에 대한 SQL 구문을 보기 위해 사용
  
  4. showmigrations (python manage.py showmigrations)
  	- 프로젝트 전체의 마이그레이션 상태 확인하기 위해 사용
  ```

- ```python
  class Article(models.Model):
      created_at = models.DateTimeField(auto_now_add=True)
      # DateTimeField는 DateField의 서브 클래스
      # auto_now_add : 최초 생성 일자 (Django ORM이 최초 insert시에만 갱신)
  	updated_at = models.DateTimeField(auto_now=True)
      # auto_now : 최종 수정 일자 (Django ORM이 save 할 때마다 갱신)
  ```

---



## Database API

- **DB API**
  - DB를 조작하기 위한 도구
  - **`Article.objects.all()`** (Class Name . Manager . QuerySet API)
    - Manager
      - 장고 모델에 데이터베이스 query 작업이 제공되는 인터페이스
    - QuerySet
      - 데이터베이스로부터 전달받은 객체 목록
      - 조회, 필터, 정렬 등 수행

- Django shell
  - DB API 구문 테스트 진행
  - 보통 shell_plus를 사용
    - django-extensions 설치하고 INSTALLED_APPS에 추가해준 후 실행

---



## CRUD

- Create - Read - Update - Delete

### 1. Create

1. 인스턴스 생성 후 인스턴스 변수 설정

   ```python
   article = Article()
   article.title = "첫번째 글"
   article.content = "첫번째 내용"
   article.save()
   ```

2. 초기 값과 함께 인스턴스 생성 (키워드 인자)

   ```python
   article = Article(title="두번째 글", content="두번째 내용")
   article.save()
   ```

3. create() 사용

   ```python
   Article.objects.create(title="세번째 글", content="세번째 내용")
   ```

- 관련 메서드
  - str() : 각각의 object를 우리가 읽을 수 있는 문자열로 반환하기 위해 사용



### 2. Read

1. 모든 데이터 조회

   - 현재 QuerySet의 복사본 반환

   ```python
   >>> Article.objects.all()
   <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]> 또는
   <QuerySet [<Article: 첫번째 글>, <Article: 두번째 글>, <Article: 세번째 글>]>
   ```

2. 하나의 데이터만 조회

   - 주어진 lookup 매개변수와 일치하는 객체 반환 (**고유성**을 보장하는 조회에서 사용)
     - 객체가 없으면 DoesNotExist 예외
     - 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외

   ```python
   >>> article = Article.objects.get(id=1)
   >>> article.title
   '첫번째 글'
   ```

3. 조건에 맞는 데이터 조회

   - 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

   ```python
   >>> article = Article.objects.filter(title='첫번째 글')
   >>> article
   <QuerySet [<Article: 첫번째 글>]>
   ```



### 3. Update

```python
>>> article = Article.objects.get(pk=1)
>>> article.title = '첫번째 글 수정'
>>> article.save()
```



### 4. Delete

- QuerySet의 모든 행에 대해 SQL 삭제 쿼리 수행
- 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리 반환

```python
>>> article = Article.objects.get(pk=1)
>>> article.delete()
(1, {'articles.Article' : 1})
```

---



## Admin Site

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- Model class를 admin.py에 등록하고 관리
- record 생성 여부 확인에 유용

- **admin 생성**
  - `python manage.py createsuperuser`
  - 내가 만든 model 보기 위해서는 admin.py에 작성하여 Django 서버에 등록해야 함

- **admin 등록**

  - ```python
    from django.contrib import admin
    from .models import Article
    
    # admin site에 등록
    admin.site.register(Article)
    ```

  - models.py에 정의한 _ _ str _ _의 형태로 객체 표현

  - ModelAdmin option

    - ```python
      from django.contrib import admin
      from .models import Article
      
      class ArticleAdmin(admin.ModelAdmin):
          list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
          
      # admin site에 등록
      admin.site.register(Article, ArticleAdmin)
      ```

      - `list_display` : models.py에서 정의한 각각의 속성들의 값을 admin 페이지에 출력하도록 설정

---



## 기타

- 게시글 정렬 순서 변경

  - ```python
    # 1. DB로부터 받은 쿼리셋을 파이썬이 변경
    articles = Article.objects.all()[::-1]
    
    # 2. 처음부터 내림차순 쿼리셋으로 받음 (DB가 조작)
    articles = Article.objects.order_by('-pk')
    ```

- **HTTP method**
  - **GET**
    - 특정 리소스를 가져오도록 요청할 때 사용
    - 반드시 데이터를 가져올 때만 사용해야 함
    - DB에 변화를 주지 않음
    - CRUD에서 R 역할을 담당
  - **POST**
    - 서버로 데이터를 전송할 때 사용
    - 리소스를 생성 / 변경하기 위해 데이터를 HTTP body에 담아 전송
    - 서버에 변경사항을 만듦
    - CRUD에서 C / U / D 역할을 담당


- **CSRF 공격 방어**
  - CSRF Token
    - 사용자의 데이터에 임의의 난수 값을 부여하여 매 요청마다 해당 난수 값을 포함시켜 전송
    - 서버에서 요청받을 때마다 전달된 token 값의 유효성 검증
  - 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용
  - `{ % csrf_token % }`
    - CSRF 보호에 사용
    - input type이 hidden으로 작성, value는 장고에서 생성한 hash 값으로 설정
  - CSRF 공격 관련 보안 설정은 settings.py에서 MIDDLEWARE에 작성되어 있음


- **redirect()**
  - 새 URL로 요청을 다시 보냄
  - 사용 가능한 인자
    - model
    - view name
    - 절대 / 상대 URL
from django.db import models

# Create your models here.
# 데이터의 구조
class Articles(models.Model):
    # table의 형태로 id(자동생성), title, content 등 추가
    title = models.CharField(max_length=30) # 최대 글자 수 꼭 지정해줘야 함
    content = models.TextField() # 최대 글자 수 지정 안해줘도 됨
    
    # 각각의 field option들은 default 값으로 어떤 값이 들어있음. 공식문서에서 확인해서 조작해주기!
    # null : 기본적으로 false가 들어가 있음 (모든 field는 기본적으로 null 값이 허용되지 않음)
    # null=True로 지정해줘야 field에서 사용할 수 있음
    # id는 장고에서 자동으로 생성, 관리해줌
    # Model 조작(생성, 수정, 삭제) : 마이그레이션 생성 및 반영(적용)해줘야 함
    # 2. python manage.py makemigrations : 마이그레이션 생성
    # 3. python manage.py migrate : 마이그레이션 반영(기본 기능에 대한 데이터베이스를 반영)
    # python manage.py sqlmigrate 앱 이름 0001 : 각각의 migration이 sql로 변환된 것을 볼 수 있음
    # python manage.py showmigrations : 모든 migrations에 대해 적용 여부 확인
        # 앱
        # [적용됐으면 X] migrations

    created_at = models.DateTimeField(auto_now_add=True)
    # 자동으로 "최초 데이터"의 생성날짜와 시간을 저장해주는 옵션이 있음(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # "수정했을 때"의 생성날짜와 시간을 저장(auto_now=True)
    # python manage.py makemigrations 했더니 밑에 저게 뜸
    # You are trying to add the field 'created_at' with 'auto_now_add=True' to articles without a default; the database needs something to populate existing rows.
    # 1) Provide a one-off default now (will be set on all existing rows)
    # 2) Quit, and let me add a default in models.py
    # 2번 옵션을 선택할거면 default로 뭘 넣을지 말해줘야 함

    # Please enter the default value now, as valid Python
    # You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value. 
    # The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now   
    # Type 'exit' to exit this prompt
    # [default: timezone.now] >>>
    # 엔터 치면 현재 날짜와 시간을 default 값으로 넣어주겠다고 하는 것

    # << ORM 사용해보기 >>
    # python manage.py shell : 장고의 모든 기능을 쓸 수 있음 (ORM 포함)
    # ORM은 모델 객체를 사용 (어떤 데이터 쓸지 알려줘야 함)
    # from (앱 이름).models import (models 안에 쓴 클래스 이름)
    # 처음에는 빈 표
    # <QuerySet []>

    # Create (CRUD)
        # 방법 1. 인스턴스 만들기
        # article = Articles()
        # >>> article.title = "첫번째 글"  
        # >>> article.content = "정신차려 푸틴" 
        # >>> Articles.objects.all() : 전체 데이터 가져오기
        # <QuerySet []> : 저장을 안 해줘서 아직 빈 표
        # >>> article.save() : 저장을 해줘야 함
        # >>> Articles.objects.all() 
        # <QuerySet [<Articles: Articles object (1)>]> : 이제 데이터 들어옴
        # >>> article = Articles.objects.all()[0] : 첫번째 줄 데이터 가져오기
        # >>> article.title : title 잘 들어갔나 확인
        # '첫번째 글'
        # >>> article.content : content 잘 들어갔나 확인
        # '정신차려 푸틴'

        # 방법 2. 처음에 넣을 때 키워드 인자를 한꺼번에 넣어주기
        # >>> article = Articles(title="두번째 글", content="점심 뭐 먹지?")
        # >>> article.save()
        # >>> Articles.objects.all()
        # <QuerySet [<Articles: Articles object (1)>, <Articles: Articles object (2)>]>
        
        # 방법 3. 처음부터 한꺼번에 넣어주고 저장까지 완료하기
        # >>> Articles.objects.create(title="세번째 글", content="살 빼야하는데?")
        # <Articles: Articles object (3)>
        # >>> Articles.objects.all()
        # <QuerySet [<Articles: Articles object (1)>, <Articles: Articles object (2)>, <Articles: Articles object (3)>]>

    def __str__(self):
        return self.title
    # <QuerySet [<Articles: 첫번째 글>, <Articles: 두번째 글>, <Articles: 세번째 글>]>

    # import 안 하고 바로 클래스 불러오기
    # pip install django-extensions 해주고 나서 settings.py INSTALLED_APPS에 추가
    # pip freeze > requirements.txt
    # python manage.py shell_plus : import를 자동으로 해줌(from 어쩌구 import 어쩌구 안해줘도 됨)

    # Query set
    # 데이터베이스로부터 건네받은 객체의 목록

    # Read (CRUD)
        # 방법 1. 모든 데이터 조회하기
        # In [1]: Articles.objects.all()
        # Out[1]: <QuerySet [<Articles: 첫번째 글>, <Articles: 두번째 글>, <Articles: 세번째 글>]>
        # In [2]: article_1 = Articles.objects.all()[0]
        # In [3]: article_1.id
        # Out[3]: 1

        # 방법 2. 하나의 데이터만 가져오기
        # get 방식 써서 하나만 가져오기(딱 한개의 데이터만 가져옴)
        # In [4]: article = Articles.objects.get(id=1)
        # In [5]: article.title
        # Out[5]: '첫번째 글'
        # In [6]: Articles.objects.create(title="첫번째 글", content="실제로는 네번째 글이지롱")
        # Out[6]: <Articles: 첫번째 글>
        # In [7]: Articles.objects.all()
        # Out[7]: <QuerySet [<Articles: 첫번째 글>, <Articles: 두번째 글>, <Articles: 세번째 글>, <Articles: 첫번째 글>]>
        # In [8]: artcle = Articles.objects.get(title='첫번째 글') : 이렇게 하면 get은 하나의 데이터만 가져올 수 있으므로 오류 뜸
        # In [9]: article = Articles.objects.get(pk=4) : id와 pk는 같은 값으로 인식
        # In [10]: article.content
        # Out[10]: '실제로는 네번째 글이지롱'

        # 방법 3. 조건에 맞는 데이터 가져오기
        # filter : 조건과 일치하는 모든 것을 가져옴
        # In [11]: articles = Articles.objects.filter(title='첫번째 글')
        # In [12]: articles
        # Out[12]: <QuerySet [<Articles: 첫번째 글>, <Articles: 첫번째 글>]>
        # filter는 종류가 엄청 많음(공식문서 보면서 필요한 거 찾기 - 공식문서 내 Field lookups)
        # In [13]: articles = Articles.objects.filter(title__contains='첫')
        # In [14]: articles
        # Out[14]: <QuerySet [<Articles: 첫번째 글>, <Articles: 첫번째 글>]>

    # Update (덮어쓰기) (CRUD)
    # article = Articles.objects.all()[3]
    # In [16]: article.content
    # Out[16]: '실제로는 네번째 글이지롱'
    # In [17]: article.title = '네번째 글'
    # In [18]: article.save() : 고쳐주고 다시 저장해주기

    # Delete(삭제하기) (CRUD)
    # In [21]: article.delete()
    # Out[21]: (1, {'articles.Articles': 1})
    # In [22]: Articles.objects.all()
    # Out[22]: <QuerySet [<Articles: 첫번째 글>, <Articles: 두번째 글>, <Articles: 세번째 글>]>
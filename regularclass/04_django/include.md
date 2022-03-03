```python
# 프로젝트 root (firstpjt) 내 urls.py

from django.urls import path, include

urlpatterns=[
    path('articles/', include('articles.urls'))
    path('pages/', include('pages.urls'))
]

# articles랑 pages는 firstpjt 안에 있는 애플리케이션이야
# 그 애플리케이션 각각에 urls.py 파일을 만들었어
# 이제는 firstpjt 내 urls.py랑 애플리케이션 각각의 urls.py를 연결해줄거야
# 사용자의 요청을 처음에는 firstpjt의 urls.py가 받아들인대
# 그럼 이제 거기에서 articles에 있는 urls.py랑 pages에 있는 urls.py로 연결시켜주는 역할을 한대
# 그래서 나머지 path는 해당 애플리케이션 urls.py로 옮겨주고 얘네만 남았엉
```

```python
# articles 내 urls.py

from django.urls import path
from . import views
# articles에 있는 views를 불러옴

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>', views.hello, name='hello'),
    path('intro/<str:name>/<int:age>', views.intro, name='intro'),
]

# path 안에 있는 name은 url에 이름 붙여준거야
# 이제는 이름으로 불러서 그 url로 연결되게 해준대
# 이건 다음 타이포라에서 알려줄게
```

```python
# pages 내 urls.py

from django.urls import path
from . import views
# 현재 위치로부터 views 불러오기(pages 내 view)

app_name = 'pages'

urlpatterns = [
    path('index/', views.index, name='index'),
]
```


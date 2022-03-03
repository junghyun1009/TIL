```python
# articles 안에 있는 urls.py

from django.urls import path
from . import views

app_name = 'articles'
# 이번에는 여기!
# 여러 애플리케이션마다 링크 이름이 겹칠 수 있엉(밑에 보면 articles랑 pages 둘다에 링크 이름 'index' 있징? 걔 때문이야)

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>', views.hello, name='hello'),
    path('intro/<str:name>/<int:age>', views.intro, name='intro'),
]
```

```python
# pages 안에 있는 urls.py

from django.urls import path
from . import views

app_name = 'pages'
# 여기에도 있지?!

urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```python
# articles > catch.html

{% extends 'base.html' %}

{% block content %}
<h1>Catch</h1>
<h2>여기서 {{ message }} 를 받았어!</h2>

<a href="{% url 'articles:throw' %}">Throw로 이동하기</a>
# 이제 이 자리에 {% url '(위에서 쓴 app_name):(url 이름)'} 이렇게 쓰래
{% endblock content %}
```


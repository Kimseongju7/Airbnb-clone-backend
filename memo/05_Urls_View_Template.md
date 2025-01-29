# url
- `config.urls` 파일은 URL과 view를 연결해주는 역할을 한다.
- user가 특정 url에 접근했을 때 Django가 해야 할 행동들.
- 문법 : `path('url/', view, name='name')` : 특정 url에 접근했을 때 view 함수를 실행한다.
- 두가지 option이 있음. 
1. config.urls에 직접 view를 작성하는 방법
2. divide and conquer 방식으로 app별로 urls를 관리하는 방법. app마다 urls.py를 만들어서 관리하는 방법.
- `view.py` : user가 특정 url에 접근했을 때 실행되는 함수.
- import해서 사용할 거라 꼭 파일 이름이 `views.py` 일 필요는 없. Django에서 이렇게 이름을 마음대로 지정할 수 있는 파일은 매우 드묾.
- 그래도 관례기에 `views.py`로 이름을 지정하는 것이 좋다.
### view 함수 작성
- view 함수는 첫번째 인자로 request를 받는다.
- request object를 통해, 어떤 user가 요청했는지, 어떤 data가 전달되고 있는지 등을 확인할 수 있음.
- view 함수는 반드시 HttpResponse를 return 해야함.
- HttpResponse는 사용자에게 보여줄 내용을 담은 객체.
- `from django.http import HttpResponse`를 import 해야함.
## 1. config.urls에 직접 view를 작성하는 방법
- `from django.urls import path`를 import 해야함.
- `path('url/', view, name='name')` : 특정 url에 접근했을 때 view 함수를 실행한다.
- view가 있는 file을 import 해야함.
## 2. divide and conquer 방식으로 app별로 urls를 관리하는 방법
- app마다 urls.py를 만들어서 관리하는 방법.
- 모든 app은 각자의 urls.py를 가지게 되고, congif.urls에서는 각 app의 urls.py를 하나로 합치는 역할을 함.
### config.urls.py
- `from django.urls import path, include`를 import 해야함.
- `path('url/', include('app_name.urls'))` : app_name의 urls.py를 include한다.
- 'url/'로 시작하는 모든 url은 app_name의 urls.py로 이동한다.
- app을 import 해 줄 필요 없음.
### app_name.urls.py
- `from django.urls import path`를 import 해야함.
- config.urls.py와 같은 형식의 path를 작성하면 됨.
- app내의 urls.py에서는 ""로 시작하는 url을 작성해야함. 이미 url/로 들어온 상태이기 때문.
## url로부터 변수 받아오기
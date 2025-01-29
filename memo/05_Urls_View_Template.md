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
- url에서 변수를 받을 거라고 django에게 말해주는 법. <> 사용.
- `path('url/<type:variable>/', view, name='name')` : url에서 variable이라는 변수를 받아옴. variable 이름은 맘대로 지정 가능.
- 이 경우에는 view 함수에서 variable을 받아야함. 
- "<int:room_id>" : room_id라는 변수를 int로 받아옴. url에 string이 들어오면 에러가 발생함. 다른 path가 없을 경우.
- `<int:room_id/<str:room_name>`: 이런식으로 여러개의 변수를 받을 수 있음.
- <> 뒤에는 /가 있을 경우 없는 url을 입력해도 자동으로 redirect해줌. 없는데 있는 url로 가면 404 에러가 발생함.
## template rendering
- 어떻게 user에게 html을 보여주는 지, DB의 data를 html에 어떻게 넣어주는 지에 대한 내용.
### `see_alL_rooms` 구현
1. 모든 방의 정보를 구해와야 함. : `Room.objects.all()` (ORM 사용, object가 manager)
2. template redering : `return render(request, 'template_name.html', context)`
- django는 template을 찾을 때, app_name/templates/를 먼저 찾음. 그 다음엔 config/templates/를 찾음.
3. rooms data 넘겨주기
- context를 사용해서 template에 data를 넘겨줌.
- context : dictionary 형태로 data를 넘겨줌. key는 template에서 사용할 변수 이름, value는 넘겨줄 data.
- html에서 data를 사용할 때는 `{{ key }}`로 사용함.
- view함수의 variable과 <int:variable> 이름은 같아야 함.
## 왜 더 이상 template을 사용하지 않는가?
- template을 사용하면, html과 python 코드가 섞여 있어서 유지보수가 어려움.
- dynamic한 web을 만들기 어려움.
- 오직 html을 원할 때만 template을 사용함.
- 단순히 content만 있는 web 페이지를 만든다면 template을 사용해도 무방.
# Django Rest API
- Django Rest Framework는 산업 표준. 
1. Django Rest Framework 설치
2. `config/settings.py`에 `rest_framework` 추가
## API가 필요한 이유
- API는 Application Programming Interface의 약자로, 서버와 클라이언트 사이의 통신을 위한 규칙을 정의한 것.
- API는 서버와 클라이언트 사이의 데이터를 주고 받는 방법을 정의한 것.
- 지난 시간에는 템플릿 랜더링, html code를 전달함.
- dynamic한 UI를 만들기 위해서는 React.js를 사용함.
- 이제 특정 url에 접근했을 때 html을 전달하는 대신 json을 전달할 것.
- JSON은 JavaScript Object Notation의 약자로, 데이터 형식 중 하나, 데이터를 주고 받는 데 사용하는 표준 포맷.
- 사람들한테 코드를 보내는 하나의 형식임.
- React.js는 이 json을 받아서 화면을 그리는 역할을 함.
- 우리는 여러 url을 만든 후, 나중에 React application이 이 url을 사용해서 데이터를 가져올 것.
- url에서는 동사를 사용하지 않음. 명사만 사용함.
### Http Methods
- GET: 데이터를 가져올 때 사용. = data를 요청할 때
- POST: 데이터를 생성할 때 사용. = data를 보낼 때
- PUT: 데이터를 업데이트할 때 사용
- DELETE: 데이터를 삭제할 때 사용
## categories API
- `/categories/` : url을 만들어서 모든 카테고리를 보여줄 것.
- `/categories/1/` : url을 만들어서 특정 카테고리를 보여줄 것.
- GET /categories/ : 모든 카테고리를 보여줄 것.
- POST /categories/ : 새로운 카테고리를 만들 것.
- PUT /categories/1/ : 특정 카테고리를 업데이트할 것. 
- DELETE /categories/1/ : 특정 카테고리를 삭제할 것.
- 다 만들 필요 없고, 직원이나 관리자가 사용할 수 있는 API를 만들어도 됨.
### REST API를 쓰지 않고 만들기.
- templates와 똑같지만 html이 아닌 json을 반환해주는 것이 차이점
- "queryset is not json serializable"의 의미 : json으로 변환할 수 없다는 의미.
- serializable : json으로 변환할 수 있는 것.
- queryset을 json으로 변환해 줄 변역기가 필요 : serializer
- django serialization framework 사용. django model을 다른 포맷으로 변환해주는 방법 제공. doc 있음.
- queryset은 browser가 이해하지 못하니 이해할 수 있는 json으로 변환해주는 것이 필요.
- 단점 : 원할한 custom이 불가. name만 보여주고, pk는 보여주고 싶지 않을 때, 이런 custom이 불가.
## Django Rest Framework
- Django Rest Framework는 Django에서 API를 쉽게 만들 수 있게 해주는 프레임워크.
- 어떤 url에서, 어떤 view 함수에서 django Rest framework의 도움을 받을 지 선택할 수 있음.
- 그래서 어떤 부분에서 도움받을 지 설정해주어야 함.
- 설정 방법 : decorator 사용
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def list_categories(request):
    categories = Category.objects.all()
    return Response("hello")
```
- application을 개발할 때 사용할 수 있는 page를 보여줌.
- status, status code, method, response, url, login user 등을 알려줌
- 여기서 해야 할 것은 @로 api_view라는 거 알려주기, Response를 return해주기.
### 우선 수동으로 해보기
- Rest Framework 역시 queryset을 json으로 변환해주는 serializer를 사용해야 함.
- `serializers.py` 파일을 만들어서 serializer를 만들어야 함. (django의 serializer는 custom 불가하기에 rest에서 제공하는 것을 사용하여 만듦.)
- 여기서 category가 json으로 어떻게 표현될 지 알려주어야 함.
- `serializers.py` 파일에 `CategorySerializer`를 만들어야 함.
- all_categories를 넘겨줄 때, category의 list를 넘겨준다면, many=True로 설정해야 함.
- serializer는 json으로 변환해주는 번역기 일 뿐이라는 것을 기억하기.
### post method
- post method는 새로운 category를 만들 때 사용.
 - `@api_view(['GET', 'POST'])`로 설정해야 함.
- web에서 post 요청을 test할 수 있는 form을 갖게 됨.
- user가 준 data는 `request.data`로 가져올 수 있음
- serializer는 python, Django -> json으로 변환해주지만, json (user data) -> python, Django으로 변환할 수도 있음.
- 즉, serializer는 user로부터 data를 받아 django model을 만들기 위해서도 필요함.
- user로 부터 온 data를 그대로 database에 넣을 수 없음. serializer를 통해 data를 검증해야 함.
- json -> python, django 변역 방법은 다음과 같음.
- `serializer = CategorySerializer(data=request.data)`로 serializer를 만들고, `serializer.is_valid()`로 data가 유효한지 확인함.
1. python -> json : serializer의 첫번째 인자, instance에 python object를 넣어주면 됨.
2. json -> python : serializer의 data에 json data를 넣어주면 됨.
- `serializer.errors`로 에러를 확인할 수 있음.
- post 시 필수 항목에서 제외하는 방법은 `read_only=True`를 사용하면 됨.
- user에게서 온 data로 serializer를 만들고 save()를 실행하면, 자동으로 `create method`를 찾음.
- 이 create method는 우리가 정의해주어야 함.
- 그리고 이 create method는 새로는 객체를 return하거나, error를 발생시켜야 함.
- `Category.objects.create(**serializer.validated_data)`로 새로운 category를 만들 수 있음.
- `**validated_data`는 dictionary를 unpacking하는 방법.
```python
name = "Category from DRF",
kind = "rooms"
```
- 이렇게 바꿔줌
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
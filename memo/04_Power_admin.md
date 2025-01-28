### reivew의 전체 row말고 rating만 가져오고 싶음
- `room.review.all().values('rating')` : room의 review 중 rating만 가져옴
- 이 경우에는 query set이 조금 바뀌어서 `review.raing`을 사용할 수 없음
- 해당 코드의 반환값은 dictionary의 list임.
- `room.review.all().values('rating')` : `{'rating': 5}` 이런 식으로 반환됨.
- 이 경우에는
```python
for review in room.review.all().values('rating'):
    tot_rating += review['rating']
```
- 이런 식으로 사용해야 함.

## 원하는 항목으로 serach하기
- `search_fields` : admin panel에서 검색하고자 하는 field를 제한할 수 있음.
- Django의 search field는 기본적으로 contains를 사용함.
- startswith를 사용하고 싶을 때는 `^`를 사용함.
- `search_fields = ('title', '^city')` : title이나 city로 검색하고 싶을 때 사용함. title은 contains, city는 startswith로 검색함.
- exact : '='
### foreign key로 search하기
- username으로 search하고 싶을 때
- `search_fields = ('owner__ username',)` : 이렇게 하면 username으로 검색할 수 있음.

## admim action
- admin panel에서 action들을 추가할 수 있음.
- `@admin.action` decorator를 사용함.
- `def make_published(modeladmin, request, queryset):` : action을 정의함.
- admin action은 3개의 매개변수를 필요로 함
- modeladmin : admin class. 이 action을 호출하는 class
- request : request object. 이 action을 누가 호출했는 지에 대한 정보를 담고 있음.
- request.user : 이 action을 호출한 user에 대한 정보를 담고 있음. superuser인지에 따라 action을 실행할 지 말지도 결정할 수 있음.
- queryset : 선택된 object들. 선택 모든 객체의 list
- 해당하는 class에서 `actions = ['make_published']`를 추가함.

## custom filter
- foreign key로 filter를 추가하고 싶을 때
- `list_filter = ('user__username',)` : city로 filter를 추가함.
- `room__category`를 했다가 지우고 새로고침 시 에러가 나는 오류가 있었음. 그러나 이건 버그였고, 최신 버전에서는 고쳐졌다고 함.
- 정리해보자면 foreign key로 filtering을 할 때, __가 없으면 __str__ 값으로 필터링. __를 사용하면 foreign key의 속성으로 필터링 할 수 있음
- 그 속성 또한 foreign key일 경우, __를 연이어서 사용하면 그 속성의 속성으로 필터링 할 수 있음.
- `list_filter = ("rating", "room__owner__is_host", )` 이런 식으로 사용할 수 있음.
### review 내 특정 단어가 포함되는 필터 만들기
```python
class WordFilter(admin.SimpleListFilter):
    title = "filter by word"

```
- `SimpleListFiter`는 title, parameter_name, lookups(method), queryset(method)를 필요로 함.
- `lookupx\s` method는 self, request, model_admin을 받고, tuple list를 반환해야 함.
- tuple의 첫번째 값은 url에 나타날 것, 두번째 값은 admin panel에 나타날 것.
- `queryset` method는 self, request, queryset(filtering할 reviews)을 받고, queryset을 반환해야 함.
- queryset을 console에 출력 시, filter 위치에 따라 결과값이 다름.
- `request.GET`을 출력하면, url에 있는 query string을 출력함. 이 query string은 dictionary임.
- 이 query string을 보고 filtering 할 것을 알 수 있음.
- 물론 다른 쉬운 방법으로는 `self.value()`를 사용할 수 있음.
- action과 마찬가지로 다른 파일에 작성해도 되지만, admin class내에 입력해주어야 함.
- filter의 경우, list_filter에 추가할 때 ""를 사용하지 않는다는 것을 기억하기
- 뒤로가기 등으로 word가 none이 되는 경우 받은 query set 그대로 반환해주기
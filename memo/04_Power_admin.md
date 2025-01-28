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
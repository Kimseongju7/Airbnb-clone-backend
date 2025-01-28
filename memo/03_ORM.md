# ORM  : Object Relational Mapping
- 객체 관계 매핑. 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑해주는 것.
- ORM을 사용하면 객체를 통해 간단한 쿼리를 사용하여 데이터베이스에 접근할 수 있음.
- ORM의 좋은 점은 database에 있는 데이터들을 python 객체로 변환해준다는 것.
## python code로 데이터 베이스와 소통
- ORM을 사용하면 SQL을 사용하지 않고 python 코드로 데이터베이스와 소통할 수 있다.
- ` python mange.py shell` : python shell을 실행하는 명령어. python 코드로 데이터베이스와 소통할 수 있다.
### database에 있는 room 찾아오기
- `from rooms.models import Room` : rooms app의 models.py에서 Room을 import함.
- Django는 이 모델을 데이터베이스에 집어넣거나, admin 패널에 보여주거나, 이미 생성된 model의 data와 상호작용할 수 있게  함.
- `Room.objects` : objects 속성을 우리가 만들지 않았지만 Django가 자동으로 만들어줌. 이 object는 수많은 method를 가지고 있음.
- 이 method들을 이용하면 데이터베이스가 Room model에서 나온 data를 가지고 오도록 시킬 수 있음.
- `Room.objects.all()` : Room model에 있는 모든 object를 가지고 옴.
- `Room.objects.get(pk=1)` : Room model에서 pk(primary key)가 1인 object를 가지고 옴.
- `Room.objects.get(name = "test")` : Room model에서 name이 "test"인 object를 가지고 옴.
- `Room.objects.filter(name = "test")` : Room model에서 name이 "test"인 object를 가지고 옴.
```python
    from rooms.models import Room
     room = Room.objects.get(pk=1)
    room.name = "test" #database에는 저장되지 않음. 일시적.
    print(room.owner.email) #foreign key만 사용하여 owner의 email을 가져올 수 있음.
    room.save() #database에 저장됨. save() method는 Django가 제공하는 method.
```
---
## objects의 method
- `.all()` : database에 있는 모든 object를 가져옴.
  - for room in Room.objects.all():` : 이런 것 사용 가능.   
- `.get()` : 단 하나의 object만 반환. 반환하려는 object의 개수가 1개가 아니면 에러 발생. 0개일때도, 2개 이상일때도 에러 발생.
  - 나중에는 이런 error를 catch해서 404 not found를 반환하도록 할 것.
- `.filter()` : 조건에 맞는 모든 object를 반환. 여러 개의 object를 반환할 수 있음.
### `.filter()` method
- `__`를 사용하여 조건을 걸 수 있음.
- `Room.objects.filter(price__lte=100)` : price가 100이하인 모든 object를 반환.
- `Room.objects.filter(name__startswith="test")` : name이 "test"로 시작하는 모든 object를 반환.
- `Room.objects.filter(name__contains="test")` : name에 "test"가 포함된 모든 object를 반환.
### `.create()` method
```python
from rooms.models import Amenity
Amenity.objects.create(name="test")
```
### `.delete()` method
- `Room.objects.filter(name="test").delete()` : name이 "test"인 모든 object를 삭제.
- object를 가지고 오고 나서 delete() method를 사용할 수 있음.
### `.count()` method
- `Room.objects.count()` : Room model에 있는 object의 개수를 반환.
### `.first()` method
- `Room.objects.first()` : Room model에 있는 첫 번째 object를 반환.
### `.last()` method
- `Room.objects.last()` : Room model에 있는 마지막 object를 반환.
### `.order_by()` method
- `Room.objects.order_by("price")` : price를 기준으로 오름차순 정렬.
- `Room.objects.order_by("-price")` : price를 기준으로 내림차순 정렬.
- `Room.objects.order_by("price", "-bedrooms")` : price를 기준으로 오름차순 정렬하고, bedrooms를 기준으로 내림차순 정렬.
- `Room.objects.order_by("price").reverse()` : price를 기준으로 오름차순 정렬한 것을 reverse.
### `.exclude()` method
- `Room.objects.exclude(price__gt=100)` : price가 100 초과인 object를 제외한 모든 object를 반환.
### `.update()` method
- `Room.objects.filter(name="test").update(name="test2")` : name이 "test"인 object의 name을 "test2"로 바꿈.
### `.exists()` method
- `Room.objects.filter(name="test").exists()` : name이 "test"인 object가 존재하는지 확인.
---
## QuerySet
- QuerySet은 database로의 query를 만들어주는 것.
- 연산자를 함께 묶어주는 일을 함.
### 이중 filter
- `Room.objects.filter(price__lte=100).filter(bedrooms=3)` : price가 100이하이고 bedrooms가 3인 모든 object를 반환.
- method의 결과로 배열을 받았다면 이런 구문을 사용할 수 없음.
- method의 결과로 QuerySet을 받았기에 사용 가능.
- QuerySet은 method를 계속 연결할 수 있음.
- QuerySet은 게으름. 
- QuerySet은 구체적으로 요청받을 때만 database에 query를 보냄.
- lazy하기에 database를 힘들게 하지 않음.
- 실질적으로 필요한 데이터만 가져옴.
## lookups : __ operator
- `Room.objects.filter(price__lte=100)` : price가 100이하인 모든 object를 반환.
- `Room.objects.filter(price__lt=100)` : price가 100미만인 모든 object를 반환.
- `Room.objects.filter(price__gte=100)` : price가 100이상인 모든 object를 반환.
- `Room.objects.filter(price__gt=100)` : price가 100초과인 모든 object를 반환.
- `Room.objects.filter(price__range=(50, 100))` : price가 50과 100 사이인 모든 object를 반환.
- `Room.objects.filter(name__contains="super")` : name에 "super"가 포함된 모든 object를 반환.
- `Room.objects.filter(name__startswith="super")` : name이 "super"로 시작하는 모든 object를 반환.
- `Room.objects.filter(name__endswith="super")` : name이 "super"로 끝나는 모든 object를 반환.
- `Room.objects.filter(name__iexact="super")` : name이 "super"와 같은 모든 object를 반환. 대소문자 구분하지 않음.
- `Room.objects.filter(name__icontains="super")` : name에 "super"가 포함된 모든 object를 반환. 대소문자 구분하지 않음.
- `Room.objects.filter(price__in=[200, 300])` : price가 200이거나 300인 모든 object를 반환.
- `Room.objects.filter(price__in=[200, 300], bedrooms__in=[2, 3])` : price가 200이거나 300이고 bedrooms가 2이거나 3인 모든 object를 반환.
- `Room.objects.filter(created_at__year = 2025)` : created_at의 year가 2025인 모든 object를 반환.
- `Room.objects.filter(created_at__year__lte= 2025)` : created_at의 year가 2025이하인 모든 object를 반환.
---
## admin 패널
- Room에 Amenity의 개수가 몇개인지 admin 패널에 보여주고 싶다면?
- list_display에 속성을 집어넣으면 Django는 RoomAdmin의 내부, Room model, Room model의 method에서 해당하는 값을 찾음.
- `rooms.admin.py` 파일과 `rooms.models.py` 파일을 수정해야 함.
- `rooms.models.py` 파일에 추가한 필드 이름을 가진 method를 만들어야 함.
- method를 admin.py에 추가할 수도 있음
---
## reverse accessor
- 관계를 뒤집어서 접근할 수 있게 해줌.
- room은 user를 가리키고 있고, user 시점에서 몇개의 room이 나를 가리키는 지 알고 싶을 때 reverse accessor를 사용.
- `Room.objects.filter(user__username="test")` : user의 username이 "test"인 room을 가지고 옴.
- foreign key에서의 __는 foreign key의 속성을 사용할 수 있음.
- ` Room.objects.filter(owner__username="rlatjdwn").count()` 
- 이렇게도 할 수 있지만, 너무 반복적임. reverse는 거의 모든 Model에 필요하니 이런 필터링을 모든 model에 적용해야 함.
- `user.room, user.review, user.wishlist` : 이런 비슷한 것을 할 수 있게 될 것임. 이게 우리가 찾는 reverse
- `room.user, review.user, wishlist.user` : 이게 정방향. 정상작동 함.
- reverese를 우리는 user에 아무런 것도 추가하지 않고 사용할 수 있음.
```python
from users.models import User
me = User.objects.get(pk=1)
me.room_set.all() #me가 만든 모든 room을 가지고 옴.
me.review_set.all() #me가 만든 모든 review를 가지고 옴.
```
`dir(me)` : me에 있는 모든 property, class의 method, class의 instance를 보여줌.
- `dir()`을 통해 reverse accessor, `_set`을 찾을 수 있음.
### what is the _set rule?
- Django는 foreign key를 가지고 있는 model이 다른 model을 가리킬 때, 가리킴을 받는 쪽에 _set property를 만들어줌.
- review model은 foreign key로 user를 가리키고 user는 review_set을 가지게 됨.
- model의 이름을 소문자로 만들고 _set을 붙이는 것이 규칙.
### customizing reverse accessor`s name
- related_name을 사용하여 reverse accessor의 이름을 변경할 수 있음.
- `user = models.ForeignKey("users.User", related_name="rooms")` : user model의 reverse accessor를 rooms로 변경.
- `many to many` field에서도 사용 가능.
- `users = models.ManyToManyField("users.User", related_name="rooms")` : users model의 reverse accessor를 rooms로 변경.
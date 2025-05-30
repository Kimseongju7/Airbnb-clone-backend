from PIL.ImtImagePlugin import fieldfrom django.utils.archive import extractfrom users.serializer import TinyUserSerializer

## Room api urls
- authetication, relationship 필요

### authetication
- post, put, delete room을 할 때 필요
- post 시, read only가 아닌 모든 필수 field들이 들어가 있는 serializer를 사용해야 함
### reationship
- foreign key로 연결되어 있는 객체를 그냥 가져오면 id로 나타냄
- 관계를 확장하는 가장 간단한 방법은 serializer에서 `depth = 1` 설정
- 하지만 이 경우에 id로 연결된 객체의 모든 field를 가져오기 때문에 불필요한 정보까지 가져올 수 있음.
- 또한 customizing이 불가함.
- 모든 room을 가져오는 `api/v1/rooms/`의 경우, room data가 많기에 serializer는 tiny함.
- 이 경우에는 관계성 확장이 필요하지 않은 경우가 많음
- 반면, room detail을 가져오는 `api/v1/rooms/<int:pk>/`의 경우, room data가 많기에 serializer는 큼.
- 이 경우에는 관계성 확장이 필요한 경우가 많음
- 관계성 확장을 하면서 필요한 정보만 가져오기 위해서, 관계 확장 시 custom 한 serializer를 사용하라고 알려주어야 함
```python
# rooms.serializers.RoomListSerializer
owner = TinyUserSerializer()
amenities = AmenitySerializer(many=True)
```
### relation post
1. owner
- serializer를 통해 post를 할 때, serializer에 있는 field 값들을 주어야 함. 
- room을 만들려고 owner의 값을 줄 때, user의 값은 TinyUserSerializer의 형식으로 주어야 함.
- 하지만 room의 주인이 누구인지는 user가 입력한 data에서 오면 안 됨. 발신자 번호 번경 같은 짓임.
- user 한테 owner가 누구인지 설정할 수 있는 권한을 주어서는 안 됨.
- 하지만 serializer는 room에는 owner가 필요하고, 그 owner는 이러한 형태를 가져야 한다. 라는 정보만 알고 있음.
- 우선 `owner = TinyUserSerializer(read_only=True)`로 설정.
2. category, amenities
- 이 둘은 특정한 형태를 지니고 있음.
- 형식 뿐만 아니라, 기존 데이터 베이스에 존재하는 값을 넣어 주어야 함.
- 형식을 맞추어도 `.save()` 에서 에러가 발생함.
- `.create()`는 기본적으로 writable nexted serializer를 지원하지 않는 다는 에러 메시지 발생.
- read_only=True로 설정하여도 NULL이 될 수 없는 field(owner) 때문에 에러 발생

- 이를 해결하기 위해 serializer가 .save() method를 실행하기 전 owner를 전달해주어야 함.
- `request.user`를 이용하여 owner를 전달해주어야 함.
- 물론 그 전에, 요청한 user가 logged in 되어 있는지 확인해야 함.
- `request.user.is_authenticated`를 이용하여 확인
- `serializer.save(owner=request.user)`를 이용하여 owner를 전달해주어야 함.
- 이게 되는 이유는 save() 시 자동으로 create method가 호출되는 때, create method는 validated_data를 인자로 받아. Room.objects.create(**validated_data)를 실행함.
- owner = request.user를 넣어주면 자동으로 validated_data에 owner가 추가됨.
- serializer.save()를 호출하서 전달해주는 건 무엇이든지 validated_data에 추가됨.
- 단, 좌항은 무조건 model의 field여야 함.
### caegory
- owner와 같은 방식으로 serializer.save() 실행 시 전달해 줄 것임.
- request.data에서 category의 값을 가져와서 해당하는 category의 값을 datbase에서 찾아 serializer에서 넘겨줄 것임.
- category는 read_only이기에 serializer에서 validation을 진행하지 않기에, request.data에 category data가 존재하지 않을 시 ParseError를 발생시킬 것임.
- ParseError는 request가 잘못된 data를 가지고 있을 때 발생하는 에. 400 status code를 반환함.
### amenities
- amenity의 경우 room 생성 시 없을 수도 있음. 그래서 save method에 인자로 넘겨주지 않고, user가 amenity를 넘겨준 경우 room 생성 후에 추가할 것임.
- amenity는 many to many field이기에, 생성된 `room.amenities.add()`를 이용하여 추가하면 됨.
- (foreign key의 경우, room.amenities = amenity로 할당하면 됨.)
- user가 존재하지 않는 amenity를 넘겨주는 경우, 조용히 넘어갈 것인가, error를 발생시키면서 생성된 room을 삭제할 것인가?
### transaction
- 생성 후 삭제는 id를 낭비하게 됨.
- room 생성 시, owner, category, amenities를 모두 성공적으로 생성해야 room을 생성할 수 있음.
- 이를 위해 `transaction.atomic()`을 사용하여, 모든 작업이 성공적으로 이루어지지 않으면 rollback을 하도록 할 것임.
- 모든 코드가 성공하거나, 아무것도 성공하지 않기를 원할 때 사용함.
- 코드 조각을 만들어 그 중 하나라도 실패한다면 DB에 적용됨 변경사항이 모두 rollback됨.
- `django.db.transaction`을 import하여 사용
- 원래는 code를 실행할때마다, 쿼리가 즉시 데이터 베이스에 적용되는데 
- `with transaction.atomic():` 안에 코드를 넣게 되 django는 즉시 반영하지 않음.
- 코드를 살펴보면서 변경사항을 리스트로 만들어 에러가 발생하지 않으면 변경사항 리스트를 DB로 push.
- 에러가 발생하면 변경사항 리스트를 모두 rollback. 반영하지 않음.
- 단, try문은 삭제해야 함. transaction이 에러 발생을 알지 못하게 하기 때문.
- transaction을 try로 밖에서 감싸 user에게 에러 원인을 알려줌
- API로 보면 실행 결과는 같지만, DB에 적용되는 방식이 다름.
- transaction은 모든 code가 한번에 적용되길 바랄 때 사용함.
---
## Serializer custom method
- 요청한 데이터를 계산해서 field로 하거나, 요청자에 따라 다른 정보를 보여주고 싶을 때 사용함.
- `serializers.SerializerMethodField()`를 사용하여 custom method를 만들어 사용함.
### average room rating
```python
# rooms.serializers.RoomSerializer
average_rating = serializers.SerializerMethodField() # average_rating의 값을 계산할 method를 만들 것이라고 알려주는 것.
#method의 이름은 속성 이름 앞에 get을 붙인 것이어야 함.
def get_average_rating(self, room): # room는 serializer가 serialize하고 있는 instance
    return room.rating()
fields = ('average_rating',) # average_rating을 보여주기 위해 fields에 추가
```
### serializer context
- serializer에 context를 넘겨줄 수 있음.
- 내가 원하는 데이터를 넘겨줄 수 있음
```python
# rooms.serializers.RoomSerializer
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'
    def create(self, validated_data):
        print(self.context)

# rooms.views
serializer = serializers.RoomSerializer(data=request.data, context={'user': request.user, "request": request})
```
- 이런 data들을 넘겨주면, serializer에서 이를 사용할 수 있음.
- 이를 사용하면, 요청하는 user가 누군지에 따라, 다른 data를 보여줄 수 있음.
- 즉 dynamic field를 만들 수 있음.
- `rooms.serializers.UserDateilSerializer.get_is_oowner` 참고
- 인스타그램 좋아요 필드가 좋은 예시

## Reverse Serializer
- room에 대해 작성된 review를 보여주려고 함.
- review에 대한 serializer를 만들어야 함.
- 역접근자를 이용하면 됨. relative_name을 field에 넣어주고 만든 serializer를 사용하면 됨.
- 단, 역접근자를 field에 포함하는 것은 데이터 베이스를 죽일 수 있으므로 좋은 생각이 아님.
- 역접근자를 위헤서는 pagination을 사용해야 함.
- 한번에 모든 review를 가져오는 것은 좋은 생각이 아님.

## Pagination
- 한번에 모든 데이터를 가져오는 것은 좋은 생각이 아님.
- pagination을 사용하여 데이터를 나눠서 보여주는 것이 좋음.
- 다행히도 django는 pagination을 지원함.
1. 먼저 page 인자를 가지고 와야 함. 
   - `request.query_params`로 쿼리 확인해볼 수 있음.
   - `request.query_params.get('page', 1)`로 page를 가져올 수 있음. 기본값 1
   - (dictionary의 get method는 기본값을 지정할 수 있다는 거 기억. 'page'가 없을 경우 1을 반환)
2. page 인자 문자열 -> 숫자로 변환
   - `page = int(page)`
     - page가 숫자가 아닌 경우, 에러 발생. 이를 방지하기 위해 try except를 사용함. (ValueError)
3. 한번에 가져올 개수 지정
   - `room.reivews.all()[start:end]`로 가져올 수 있음.
   - `page_size = 3`로 지정
- Django의 장점은 `room.reivews.all()[start:end]` 이 code에서 볼 수 있음
- reviews를 전부 다 가져온 후 slicing을 하는 것이 아님.
- queryset은 게으름. = 즉각적으로 평가되지 않음.
- 그래서 모든 걸 가져오는 게 아니라 limit와 offset을 포함하는 sql문을 데이터 베이스로 보냄.
## file upload
- admin panel에서 사진을 업로드가고 그 사진을 보려고 하면 page not found가 뜸.
- Django에게 파일이 저장된 위치를 알려주지 않았기 때문.
- 기본적으로는 . 위치에 저장되지만, 경로를 바꾸기 위헤서는 `config.settings.py`에 `MEDIA_URL`과 `MEDIA_ROOT`를 설정해야 함.  
- `MEDIA_ROOT='uploads'`로 설정하면, uploads 폴더에 저장됨. / 필요 없음. 사진을 올리면 upload라는 새로운 폴더가 생성됨.
- 하지만 여전에 admin panel에서 사진을 볼 수 없음. user에게 어떻게 파일을 보여줄 건지 정해야 함. 어느 url에서 보여줄건지
- `MEDIA_URL`을 설정하여 user가 업로드된 사진에 접근할 수 있게 함. 이 때 MEDIA_URL은 반드시 /로 끝나야 함.
- 업로드 된 사진 clock시 장고가 MEDIA_URL url로 이동. 하지만 여전히 page not found가 뜸.
- 이는 장고가 MEDIA_URL로 가는 요청을 처리하지 않기 때문.
- 이를 해결하기 위해 `config.urls.py`에 `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`를 추가해야 함.
- `setting.py` 파일에 접근한 때 `from django.conf import settings`를 import하여 어느 파일에서든 간편하게 접근할 수 있음.
- page_size 등 필요한 것들을 setting.py에 넣어두고 간편하게 사용할 수 있음.
- MEDIA_URL은 file을 노출하는 방법, MEDIA_ROOT는 file이 실제로 있는 위치임.
- MEDIA_URL로 이동하는 것은 MEDIA_ROOT 폴더 안을 보라고 말하는 것임.
- 단 이런 과정은 실제 배포 환경에서는 사용하지 않음. 이는 개발 환경에서만 사용함. 보안 문제가 있음.
- 모르는 사람들이 code 근처에 파일을 업로드하는 것을 허용하는 것과 마찬가지 이기 때문.
### 파일을 다른 서버에 넣기
- 장고는 파일의 url만 알게 되고 업로드한 파일들은 AWS나 클라우드 이미지 서버에 저장할 것임
- 그러기 위해 media model을 수정해야 함.
- `models.URLField()`를 사용하여 url을 저장할 것임.
- 파일을 Cloudflare에 업로드 하면 Cloudflare가 파일을 저장하고, url을 반환함. 그리고 이 url을 django에게 주면 됨.
## Permission_classes
- permission_classes를 사용하여 user가 어떤 permission을 가지고 있는지 확인할 수 있음.
- `from rest_framework.permissions import IsAuthenticated`를 import하여 사용함.
- `permission_classes = [IsAuthenticated]`를 사용하여 user가 로그인 되어 있는지 확인할 수 있음.
- `from rest_framework.permissions import IsAdminUser`를 import하여 사용함.
- `permission_classes = [IsAdminUser]`를 사용하여 user가 admin인지 확인할 수 있음.
- `from rest_framework.permissions import IsAuthenticatedOrReadOnly`를 import하여 사용함.
- `permission_classes = [IsAuthenticatedOrReadOnly]`를 사용하여 user가 로그인 되어 있거나 읽기만 가능한지 확인할 수 있음. GET은 누구가 요청할 수 있게하고, POST, PUT, DELETE는 로그인한 사람만 요청할 수 있게 함.
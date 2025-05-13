# Django basic

- Django에서는 list보다 tuple을 사용함. 다만 tuple내 하나의 element만 있을 때는 뒤에 콤마를 붙여줘야 함. 그렇지 않으면 string으로 인식함.
- tuple은 변경할 수 없는 list이기에 보안에 좋음. 변경할 수 없는 데이터를 저장할 때 사용함.

### run server
manage.py : terminal에서 Django 명령어를 실행. 터미널에서 Django를 사용하기 위해 manage.py를 사용. 배포 단계에서는 사용하지 않음.

- `python manage.py runserver` : 서버를 실행하는 명령어. 서버를 실행하면 Django 프로젝트를 실행할 수 있음.
- `You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. Run 'python manage.py migrate' to apply them.` : 서버를 실행하면 이런 메시지가 뜸. 이 메시지는 데이터베이스에 적용되지 않은 변경 사항이 있다는 뜻. 이 메시지가 뜨면 `python manage.py migrate`를 실행하여 데이터베이스에 변경 사항을 적용해야 함.
- http://127.0.0.1:8000/admin : 서버를 실행하면 이 주소로 들어가면 관리자 페이지로 들어갈 수 있음. 관리자 페이지에서 데이터베이스를 관리할 수 있음.
---
- migrations : 데이터베이스의 모양을 변경할 때 사용. 데이터베이스의 모양을 변경할 때마다 migration 파일이 생성됨. migration 파일은 데이터베이스의 변경 사항을 기록한 파일. migration 파일을 데이터베이스에 적용하면 데이터베이스의 모양이 변경됨.
- 우리는 db에 django_session이라는 table을 생성하는 migration을 실행해야 함. 
- `You have 18 unapplied migration` : django는 이미 db의 state를 변경하는 18개의 migration(파이썬 코드)을 만들었지만, 아직 db에 적용하지 않았다는 뜻. 이 migration file들이 우리에게 필요한 table을 만들어줌.

### admin
- `python manage.py createsuperuser` : 관리자 계정을 생성하는 명령어. 이 명령어를 실행하면 username, email, password를 입력하면 관리자 계정이 생성됨. -> 관리자 계정을 database에 저장.
- django는 단순히 명령어만 실행 시켜도 admin 패널을 얻을 수 있음
- admin : 데이터베이스를 관리할 수 있는 페이지. 데이터베이스에 저장된 데이터를 추가, 수정, 삭제할 수 있음.

### Django 장점
1. user authentication, password hashing이 포함된 admin panel 제공
2. 모든 user listing, add new user, delete user, change user, serach user, filter user 등의 기능을 제공
이와 같은 기능을 직접 구현하는 것은 매우 어려움. Django는 이러한 기능을 제공해주기 때문에 개발 시간을 단축할 수 있음.

### library vs framework
- library : 개발자가 호출하는 것.
- framework : 개발자가 호출하는 것이 아닌 framework가 개발자가 작성한 코드를 호출하는 것. 개발자는 framework에 맞춰서 코드를 작성해야 함.
- `Note: You are 9 hours ahead of server time.` : 아마 서버 시간은 UTC. 이런 configuration은 어디서 했을까? -> settings.py에서 할 수 있음. time_zone을 통해 설정 가능.
  - setting 변경 후 저장 시 서버는 자동으로 재시작

### Django Apps
- Django project는 여러 개의 Apps들로 구성됨. 각 App은 특정한 기능을 담당함. 각 Apps에는 data와 logic이 있음
- folder같은 어플리케이션 상상하기
- 하나의 app은 airbnb에서 하나의 room을 위한 폴더가 될 것임.
- app은 data와 Logic을 합쳐서 캡슐화 함.
- data들을 어떻게 분리할 지를 결정하면 됨. room의 data와 user의 data를 분리하는 것처럼. 
- app들은 서로 연결되어 있음. room app은 user app과 연결되어 있음. review app은 room app, user app 과 연결되어 있음.
- module과 같은 것으로 생각
- app : project의 부분. project는 여러 개의 app으로 구성됨. 각 app은 특정한 기능을 담당함. 각 app은 data와 logic을 포함함.
---
# Django Apps

## Django App 생성
- `python manage.py startapp app_name` : app을 생성하는 명령어. 이 명령어를 실행하면 app_name이라는 폴더가 생성됨. 이 폴더에는 app을 구성하는 파일들이 들어 있음.
- `app_name` : app의 이름. app의 이름은 소문자로 작성함. app의 이름은 다른 app의 이름과 중복되면 안 됨.
- `models.py` : app의 데이터를 정의하는 파일. 데이터베이스의 테이블을 정의함. data의 모양을 django에게 알려주는 곳. app에서의 데이터를 묘사. 이 파일 덕분에 SQL 코드를 작성하지 않아도 됨.
- `views.py` : app의 로직을 정의하는 파일. 데이터를 처리하는 방법을 django에게 알려주는 곳.

### models.py
- `class` : 데이터베이스의 테이블을 정의하는 곳. 데이터베이스의 테이블은 class로 정의함. class의 이름은 테이블의 이름이 됨. models.Model을 상속받아야 함.
- 수정 후 저장해도 서버는 자동으로 재시작되지 않음. app을 install하지 않아 Django가 house app을 인식하지 못하기 때문. settings.py에 app을 등록해야 함.
- setting에서 installed_apps에 app을 등록하면 Django가 app을 인식함. app을 등록하면 app의 models.py, views.py를 인식함.
- 등록 방식 : `app_name.apps.AppNameConfig` : app_name은 app의 이름. AppNameConfig는 app의 설정 파일. app의 설정 파일은 apps.py 파일에 있음. houses 폴더의 apps.py 파일에 있는 housesConfig 클래스.

### field options
- `help_text` : 추가 도움말이 위젯 form과 함께 표시됨.
- `verbose_name` : admin panel에서 보여지는 이름. 필드의 이름을 지정함. 필드의 이름을 지정하지 않으면 Django는 attribute를 이용해서 이름을 자동으로 생성.

### 데이터의 모양을 설명해야 하는 이유
1. Django가 우리 database와 소통하기 위해 -> database는 SQL로 소통함. Django가 파이썬 코드를 보고 SQL 번역해서 소통.
2. 데이터 admin(관리) 패널을 자동으로 생성하기 위해.

### admin.py
- `from .models import ModelName` : models.py에서 정의한 ModelName을 import함.
- `@admin.register(ModelName)` : Model을 admin 패널에 등록함. Model을 admin 패널에서 관리할 수 있음.
- 등록 시 admin 창에 Model이 나타남.

## migration
- Django는 model을 통해 데이터의 모양을 알지만, database는 모르기 때문에 migration을 실행해야 함. migration을 실행하면 database에 table이 생성됨.
- `python manage.py makemigrations` : migration 파일을 생성하는 명령어.
- 생성 후 `python manage.py migrate`를 통해 database에 migration을 적용.
- model에서 변경사항 있을 시 migration을 다시 실행해야 함. makemigrations -> migrate 순서로 실행.

## admin panel
- admin panel 관리는 `admin.py`에서 함.
- action들도 추가로 만들 수 있음.
### House Object(1) 해결하기
- admin 패널에서 House Object(1)이라고 나오는 이유는 `__str__` 메소드를 정의하지 않았기 때문. `__str__` 메소드를 정의하면 admin 패널에서 House Object(1) 대신 House의 title이 나옴.
### House list 개선하기
- User admin panel의 list와 달리 House admin panel의 list는 name만 보여주고 있음. 이를 개선하기 위해서는 admin.py에서 list_display를 정의해야 함.
- `list_display` : admin.ModelAdmin 클래스의 속성. admin panel에서 보여줄 필드를 정의함. admin panel에서 보여줄 field들의 List를 작성하면 됨. 이 field들은 models.py에서 정의한 속성이어야 함.
### filter 추가하기
- admin.py에서 `list_filter`를 정의하면 admin panel에서 filter를 추가할 수 있음.
### search
- admin.py에서 `search_fields`를 정의하면 검색하고자 하는 field를 제한할 수 있음.
- '__startswith' : title이 검색어로 시작하는 house를 찾음. 
- '__contains' : title에 검색어가 포함된 house를 찾음.
---
# Users
- 프로필 사진 추가, 소셜 네트워크 허용 등 기존에 있는 Users를 커스텀 하고 싶음. 두 가지 방법이 있음.
1. profile이라는 새로운 app을 만들어 기존 Django의 User와 연결 시키는 방법
2. 새로운 우리만의 User model을 만들어 기존 Django의 User를 대체하는 방법 <- 권장
- 관련 document : substituting a custom user model
## Custom User Model
1. 새로운 app을 만들어 User model을 만듦.
2. AbstractUser를 상속받아 User model을 만듦.
3. 기존 User에서 수정할 것이 없다면 pass를 사용함.
4. settings.py에서 AUTH_USER_MODEL을 수정함. 
- 프로젝트 시작 시 교체를 권장하는 이유는 이미 기존 user로 사용자 생성 시 사용자가 이미 있는 상태에서는 교체할 수 없기 때문.
- 해결 방법은 데이터 배이스와 migration을 삭제해야 함.
- 주의할 점은 house의 migration을 삭제할 때, 폴더를 지우지 않고 0001이런 숫자로 시작하는 migration 파일만 지워야 함.
- 그 후 makemigration, migrate를 실행하면 됨.
### custum user admin panel
- admin.py에서 UserAdmin을 상속받아 CustomUserAdmin을 만듦.
- `fieldsets` : admin panel에서 보여줄 field를 정의함.
- fieldsets은 일종의 section안에 field를 넣고 그 section에 제목을 붙일 수 있음.
- fieldsets은 tuple의 tuple 로 구성됨. 각 tuple은 section을 나타냄. 각 section은 field를 나타냄.
- tuple의 첫 번째 element는 section의 제목을 나타냄. 두 번째 element는 section에 포함될 field를 나타냄.
- key로는 "fields"를 사용함.
- 두 번째 element는 dictionary로 구성됨. dictionary의 key는 field의 이름을 나타냄. dictionary의 value는 field의 속성을 나타냄.
- dictionary의 value는 보여주고 싶은 property의 tuple로 구성됨
- fields는 section이 없는 field를 나타냄.
- Dictionary에 여러 속성을 추가할 수 있음.
- `classes` : css class를 추가할 수 있음. collapse는 section을 접을 수 있음. wide는 section을 넓게 보여줌.
### user property 추가, 수정, 삭제
- first name, last name말고 하나의 name으로만 하고 싶음 -> editable = False로 설정.
## connecting dirrerent apps
- house에는 주인인 user가 있고, posting한 사진에는 post한 user가 있고, 좋아요를 누르면 좋아요 누른 사진이 있고, 모든 app은 연결되어 있음.
- house에 owner라는 id를 추가할 것임.
- 우린 id를 만든적이 없지만 django와 database는 자동으로 id를 만들어줌. 이 id를 이용해 user와 house를 연결할 것임.
- django documetation에서는 id를 `pk`, `primary key`라고 부름.
- 우리가 해야할 거는 house에 유저의 id를 추가하는 것.
- house에서 owner의 type은 `foreign key`로 설정함. foreign key는 다른 table의 primary key를 가리킴.
- data type을 `ForeignKey`로 설정함으로써 Django에게 이 field가 다른 table의 primary key를 가리킨다는 것을 알려줌.
- 단, 어떤 model 'pk'를 참조하는 것인지 알려주어야 함.
- `on_delete` : 참조하는 model이 삭제될 때 어떻게 할 것인지를 결정. 'foreign key'의 필수 옵션. user object가 삭제되면 연결된 house도 삭제되게 함.
- airbnb에서는 user가 삭제되면 house도 삭제되기 때문에 `on_delete=models.CASCADE`로 설정함. 
- 결제 내역 table이라면 user가 삭제되어도 결제 내역은 남아있어야 하기 때문에 `on_delete=models.SET_NULL`로 설정함.
---
# Models and Admin
- 더 다양한 model과 admin을 만들어보자.
### 입력으로 지정한 option 선택하기
- 성별의 경우, 선택지를 지정해주고 싶음.
- user class안에 GenderChoices class를 만들어 선택지를 지정함.
- class안에 선택지들을 집어넣는데 tuple로 집어넣음.
- 하나는 데이터 베이스에 저장되는 값, 다른 하나는 admin panel에서 보여지는 값(label).
- 그리고 gender field에 choices를 설정함.
- database에 들어가는 값은 max_length보다 작아야 함.
## app rooms 만들기
- `python manage.py startapp rooms` : rooms app을 생성함.
- 'config.settings'에 rooms app을 등록함. 
### many to many field
- house에는 여러 개의 편의시설이 있을 수 있고, 편의시설은 여러 개의 house에 있을 수 있음. 이런 경우, many to many field를 사용함.
- 'may to many' 관계는 여러 amenities가 여러 rooms에 있을 수 있게 함.
### 만들어진 날짜와 수정된 날짜
- DateTimeField를 사용하여 만들어진 날짜와 수정된 날짜를 추가함. 여기에 여러 속성들을 추가할 수 있음.
- auto_now_add는 생성된 날짜를 자동으로 추가함. 해당 필드의 값을 object가 처음 생성될 때의 시간으로 설정함.
- auto_now는 수정된 날짜를 자동으로 추가함. 해당 필드의 값을 object가 저장될 때의 시간으로 설정함.
- 이런 날짜를 여러 모델에 넣고 싶다면 코드가 반복됨.
- 이런 경우, abstract class를 사용함. abstract class는 다른 class에서 상속받아 사용할 수 있는 class.
- blank=True는 form에서 필드가 비어있어도 되는지를 나타냄. null=True는 필드가 database에서 null이 될 수 있는지를 나타냄.
## abstract class 사용하기
- 다른 app과 공유할 수 있는 code를 가지고 있음.
- `python manage.py startapp common`
### app common
- 기존 Django에서는 model을 볼 때마다 그 model을 database에 넣었음. admin 패널에도 추가되고.
- abstract class는 database에 추가되지 않을 model을 만들 때 사용함.
- 다른 model에서 재사용하기 위한 model임.
```python
  class Meta:
        abstract = True
```
- Django가 model을 configure할 때 사용하는 class
### amenities 올바른 복수형으로 고치기
- verbose_name_plural을 사용하여 복수형을 지정함.
- class Meta에 verbose_name_plural을 지정하면 됨.
### 상세화면 생성시간, 수정시간 추가하기
- `readonly_fields` : admin panel에서 수정할 수 없는 field를 나타냄.
### one-to-one relationship
- experience와 vedio는 1:1 관계를 가짐. 하나의 experience는 하나의 video를 가짐.
- `OneToOneField` : 하나의 object가 다른 object를 가리킬 때 사용함.
- ForeignKey와 비슷하지만, ForeignKey는 여러 object를 가리킬 수 있음.
- `OneToOneField`는 unique가 추가됨
- 한 활동이 동영상을 가지면 그 활동은 더이상 다른 동영상을 가질 수 없음.
## relative name
- rooms app도 room, direct_messages app도 room을 가지고 있고, 둘 다 user와 연결되는 경우 에러 발생.
- 같은 이름을 가진 model이 같은 model과 연결되면 에러 발생.
- 역방향 참조 시 사용할 이름
## App verbose name 수정하기
- admin panel에서 보여지는 app의 이름을 수정하고 싶음.
- app의 verbose name을 수정하면 됨.
- `apps.py`에서 `verbose_name`을 수정하면 됨.

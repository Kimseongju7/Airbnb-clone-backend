### Validation
- user가 자신의 email이나 username을 변경할 때, 이메일이나 username이 이미 존재하는지 확인해야 한다.
- ModelSerializer가 unique=True로 설정된 필드에 대해 기본적으로 unique validation을 수행한다.
- 우리가 해야하는 vaildation은 user 생성 시 password
## Create User API
1. user가 보낸 data에서 password 가지고 오기
2. user를 database에 저장하기 (아직 password 없는 상태)
3. `user.set_password(password)`로 password 암호화. user.password = 'password'로 하면 암호화가 안된다.
4. `user.save()`
- put하거나 post 할 때, 없는 field의 값이 들어와도 괜찮네. 그래서 serializer에 password가 지정되어 있지 않아도 user가 password data를 보낼 수 있는 듯.
- 이 API에서 생성된 user는 admin panel에 login 하지 못 함. is_staff, is_superuser가 False이기 때문.
## `api/v1/users/username/` API
- urls.py에 `path('<str:username>/')` 그냥 추가하면 안 됨.
- `path("me/`) 가 이미 있기 떄문.
- urlpattern 순서가 중요하다. `path("me/`)를 `path('<str:username>/')`보다 위에 두어야 한다.
- 순서대로 일치하는 지 확인하기 때문.
- 근데 'me'라는 username을 가진 user가 있다면 어떻게 해야 할
- `path('@<str:username>/')` 이런 식으로 하면 됨.
### Change Password API
- 자신의 password만 바꿀 수 있게, user에게서 기존 비밀번호와 새로운 비밀번호를 받아 기존의 비밀번호를 알고 있을 경우에만 바꿀 수 있게.
- 이때 old_password를 비교할 때는 hash를 비교해야 한다.
- `user.check_password(old_password)`로 비교한다.
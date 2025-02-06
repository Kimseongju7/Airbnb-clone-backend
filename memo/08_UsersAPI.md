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
### User Login API
- `from django.contrib.auth import authenticate, login`로 authenticate 함수를 import한다.
- `authenticate(request, username=username, password=password)`로 user를 찾아낸다.
- user가 없거나 password가 틀리면 None을 반환한다.
- user가 있으면 user object를 반환한다.
- user가 있으면 `login(request, user)`로 user를 login한다.
- `login(request, user)`로 user를 login한다. 필요한 cookie, token 중요한 거는 다 생성해준다.
- login 시 user 정보가 담긴 session이 생성된다.
- session은 django에서 제공하는 기능으로, user가 로그인 상태를 유지할 수 있게 해준다.
- session은 cookie에 저장된다.
### logout
- `from django.contrib.auth import logout`로 logout 함수를 import한다.
- `logout(request)`로 logout한다.
- logout 시 session이 삭제된다.
### Error의 사용
1. ParseError 
    - 클라이언트가 전송한 데이터 형식이 잘못되어 파싱(parsing)에 실패한 경우 사용
2. ValidationError
    - serializrer에서 validation에 실패한 경우 사용
3. Response(status=404)
   - 요청한 리소스가 존재하지 않는 경우 사용
   - 데이터베이스에서 특정 객체를 조회했으나 존재하지 않을 때
   - DRF의 기본 예외 처리(NotFound) 대신 커스텀 응답을 반환하고 싶을 때
   - 단. Response(status=404) 대신 DRF의 NotFound 예외를 사용하면 일관된 오류 형식을 유지할 수 있음.
4. Response(status=400) Bad Request
    - 클라이언트의 요청이 잘못되었음을 의미
    - DRF의 ValidationError 예외를 발생시키면 자동으로 400 Bad Request 응답을 반환
5. PermissionDenied : 권한 부족
    - 요청 자체의 문제가 아닌 권한 부족 문제
    - APIView.dispatch() 메서드에서 PermissionDenied 예외를 발생시키면 403 Forbidden 응답을 반환
    - PermissionDenied에 400 사용 금지. 보안 취약점 발생 가능 : 권한 문제를 데이터 문제로 오인 가능.공격자에게 불필요한 정보 제공
# Authentiacation
- Django Rest Framwork에서 Authentication strategy 구축하기
- 기본적으로 Django Rest Framework는 session-based authentication이 제공되고 이걸 Reaat frontend에서 사용할 거지만
- 직접 custom authentication을 구현하는 법을 배울 것임.
- 브라우저 외에서 사용할 때는 session-based authentication이 불가능하기 때문에 custom authentication이 필요함. ios, android, etc.
- token-based authentication이나 JWT(JSON Web Token) based authentication이 필요함.
- `request.user`는 쿠키를 이용해서 인식됨. 나중에는 token을 이용해서 인식할 것임.
- django가 request.user를 인식하는 방법이 바뀌는 거지 내가 만든 API가 바뀌는 건 아님.
- 우선 목표는 `user.me` 로 갔을 때 내 프로필이 보이는 것.
- `postman` 필요 - 브라우저 밖에서 API와 상호작용할 때 필요
- android, ios에서 보내는 simulation
## 1. Custom Authentication - 조금 멍청한 방법
- `settings.py`에서 `REST_FRAMEWORK` 설정을 바꿔줘야 함. 
- default authentication을 바꿔줘야 함.
- `settings.py`에서 `DEFAULT_AUTHENTICATION_CLASSES`를 바꿔줘야 함.
- `settings.py`에서 `DEFAULT_PERMISSION_CLASSES`를 바꿔줘야 함
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [ # restframework가 user를 인식하는 방법들이 들어있는 list. 원래는 'rest_framework.authentication.SessionAuthentication'이 들어있음.
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```
- `config.permissions` 폴더를 만들고 우리만의 authentication class 제작
- 마지막에 user만 반환해주면 됨 == view에서의 `request.user`
- 모든 authentication class는 `BaseAuthentication`을 상속받아야 함. (from rest_framework.authentication import BaseAuthentication)
- `authenticate` method를 override 해야 함. 이 method는 `request`를 받아서 `user`를 반환해야 함. 없다면 `None`을 반환해야 함.
- authentication class를 만든 뒤, postman에서 요청. postman은 cookie를 사용하지 않기 때문에 session-based authentication이 불가능함.
- 그래서 django framework `TrustMeAuthentication`을 통해 user를 찾으려고 할 것임.
- 둘 다에서 찾지 못하면 logout 된 것.
- postman에서 username을 보내주고 이 이 username으로 user를 찾을 것임.
- 이 인증방법은 절 대 사용하면 안 됨. 왜냐하면 username만으로 인증하기 때문에 보안에 취약함.
- 우리가 만든 건 user를 cookie에서 찾는 대신 "X-USERNAME"라는 header에서 찾는 것임.
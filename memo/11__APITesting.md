# API Test
- 우리가 만든 API를 테스트하는 방법
- 지금까지는 브라우저로 가서 코드를 실행하는 방법으로 직접 수동으로 테스트했음.
- 이번 section에서는 Test code를 작성하는 방법과 명령어 하나로 모든 것을 test하는 방법을 알아볼 것임.
- `python manage.py test`를 통해 모든 test를 실행할 수 있음.
- `from rest_framework.test import APITestCase`를 통해 API test를 할 수 있음.
- APITestCase class에는 method 명명 규칙이 있음. `test_`로 시작하는 method만 실행됨.
- self는 APITestCase class를 의미함.
- `Assertion` : 참이 되어야 하는 것.
- `self.assertEqual(a, b)` : 두 객체 혹은 값이 같아야 함.
- `self.client` : APITestCase class에 있는 client 객체. 이 객체를 통해 API를 test할 수 있음. API 서버로 request를 보낼 수 있게 해 줌
- `self.client.get(url)` : url로 get request를 보내는 method. 브라우저 주소창에 url을 입력하는 것과 같음.
- `self.client.post(url, data)` : url로 post request를 보내는 method. data는 dictionary 형태로 보내야 함.
- `self.client.put(url, data)` : url로 put request를 보내는 method. data는 dictionary 형태로 보내야 함.
- `self.client.delete(url)` : url로 delete request를 보내는 method.
- `self.client.login(username, password)` : login을 해야만 API를 test할 수 있음. 이 method를 사용하면 login이 됨.
- `self.client.logout()` : logout을 해야만 API를 test할 수 있음. 이 method를 사용하면 logout이 됨.
- `self.client.force_authenticate(user)` : user를 authenticate하고 API를 test할 수 있음.
- test를 할 때는 test database를 사용함. data를 생성하고 지우면서 test를 진행해야 하는데, 실제 database에 영향을 주지 않기 위해 test database를 사용함.
- 브라우저에서 보이는 data는 실제 database에 있는 데이터이기에, test code를 진행하면서 받는 값과는 다를 수 있음.

## setUp method
- test code를 작성할 때, 반복되는 코드를 줄이기 위해 setUp method를 사용함.
- setUp method는 test code를 실행하기 전에 실행됨.
- database를 설정할 수 있는 곳
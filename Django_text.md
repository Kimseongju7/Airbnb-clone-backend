# Django basic

### run server
manage.py : terminal에서 Django 명령어를 실행. 터미널에서 Django를 사용하기 위해 manage.py를 사용. 배포 단계에서는 사용하지 않음.

- `python manage.py runserver` : 서버를 실행하는 명령어. 서버를 실행하면 Django 프로젝트를 실행할 수 있음.
- `You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. Run 'python manage.py migrate' to apply them.` : 서버를 실행하면 이런 메시지가 뜸. 이 메시지는 데이터베이스에 적용되지 않은 변경 사항이 있다는 뜻. 이 메시지가 뜨면 `python manage.py migrate`를 실행하여 데이터베이스에 변경 사항을 적용해야 함.
- http://127.0.0.1:8000/admin : 서버를 실행하면 이 주소로 들어가면 관리자 페이지로 들어갈 수 있음. 관리자 페이지에서 데이터베이스를 관리할 수 있음.
---
- migrations : 데이터베이스의 모양을 변경할 때 사용. 데이터베이스의 모양을 변경할 때마다 migration 파일이 생성됨. migration 파일은 데이터베이스의 변경 사항을 기록한 파일. migration 파일을 데이터베이스에 적용하면 데이터베이스의 모양이 변경됨.
- 우리는 db에 django_session이라는 table을 생성하는 migration을 실행해야 함. 
- `You have 18 unapplied migration` : django는 이미 db의 state를 변경하는 18개의 migration(파이썬 코드)을 만들었지만, 아직 db에 적용하지 않았다는 뜻. 이 migration file들이 우리에게 필요한 table을 만들어줌.
---
### admin
- `python manage.py createsuperuser` : 관리자 계정을 생성하는 명령어. 이 명령어를 실행하면 username, email, password를 입력하면 관리자 계정이 생성됨. -> 관리자 계정을 database에 저장.
- django는 단순히 명령어만 실행 시켜도 admin 패널을 얻을 수 있음
- admin : 데이터베이스를 관리할 수 있는 페이지. 데이터베이스에 저장된 데이터를 추가, 수정, 삭제할 수 있음.
---
### Django 장점
1. user authentication, password hashing이 포함된 admin panel 제공
2. 모든 user listing, add new user, delete user, change user, serach user, filter user 등의 기능을 제공
이와 같은 기능을 직접 구현하는 것은 매우 어려움. Django는 이러한 기능을 제공해주기 때문에 개발 시간을 단축할 수 있음.
---
### library vs framework
- library : 개발자가 호출하는 것.
- framework : 개발자가 호출하는 것이 아닌 framework가 개발자가 작성한 코드를 호출하는 것. 개발자는 framework에 맞춰서 코드를 작성해야 함.
- `Note: You are 9 hours ahead of server time.` : 아마 서버 시간은 UTC. 이런 configuration은 어디서 했을까? -> settings.py에서 할 수 있음. time_zone을 통해 설정 가능.
  - setting 변경 후 저장 시 서버는 자동으로 재시작
---
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

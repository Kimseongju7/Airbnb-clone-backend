###Operation Error - no  such table
- Error message: `no such table: app_name_model_name`
- Error reason: table이 없기 때문에 발생하는 에러.
- 현재 database가 Django가 필요로 하는 database와 다르기 때문에 발생하는 에러.

###  SystemCheckError: System check identified some issues: <class 'houses.admin.HouseAdmin'>: (admin.E116) The value of 'list_filter[0]' refers to 'prive_per_night', which does not refer to a Field.
- 오타가 원인. model의 속성이 아닌 것을 작성함.
### ValueError: Dependency on app with no migrations: users
- custum user로 교체 시 기존 user들은 없애주어야 함.
- 사용자가 이미 있는 상태에서는 교체할 수 없음
### non_nullalbe field에 default 값이 없음
```text
It is impossible to add a non-nullable field 'is_host' to user without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option:
```
- is_host field를 추가할 때 default 값을 지정하지 않아서 발생하는 에러.
- 기존 데이터 베이스에 user가 이미 있기에 발생하는 에러, 기존 행에 새로운 열이 추가되는데 거기는 null로 둘 수 없어. 어떤 값 넣어둘까? 라고 물어보는 것.
- 일회성 default 값을 지정하거나 models.py에서 default 값을 지정해야 함.
- 아니만 null=True로 지정하든가.
- 기존에 user가 있었을 경우, 그 유저에게는 default 값이 없어 null 값이 들어가게 되는 것을 방지하기 위해.
### FieldError at /admin/users/user/1/change/
```text
'first_name' cannot be specified for User model form as it is a non-editable field. 
Check fields/fieldsets/exclude attributes of class CustomUserAdmin.
```
- first_name, last_name을 non_editable로 설정했지만 admin panel은 기존 UserAdmin을 사용하고 있기에 에러가 발생함.
- 기존 UserAdmin은 first_name, last_name의 editable을 True로 설정하고 있기 때문.
### IndentationError: unexpected indent
```text
 File "/Users/rlatjdwn/Documents/mine/personal/nomadcoder/Airbnb-clone-backend/common/apps.py", line 1
    from django.apps import AppConfig
IndentationError: unexpected indent
```
- 들여쓰기 에러. 들여쓰기가 잘못되어 있음.
- `from django.db import models` 앞에 띄어쓰기 하나 있었음.
### TypeError at /rooms/
```text
say_hello() takes 0 positional arguments but 1 was given
```
- 함수에 인자를 넣었는데 인자를 받지 않는 함수에 인자를 넣어서 발생하는 에러.
### AttributeError at /rooms/
```text
'str' object has no attribute 'get'
```
- str object에 get 메소드를 사용하려고 해서 발생하는 에러.
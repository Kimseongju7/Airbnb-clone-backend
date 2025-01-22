###Operation Error - no  such table
- Error message: `no such table: app_name_model_name`
- Error reason: table이 없기 때문에 발생하는 에러.
- 현재 database가 Django가 필요로 하는 database와 다르기 때문에 발생하는 에러.

###  SystemCheckError: System check identified some issues: <class 'houses.admin.HouseAdmin'>: (admin.E116) The value of 'list_filter[0]' refers to 'prive_per_night', which does not refer to a Field.
- 오타가 원인. model의 속성이 아닌 것을 작성함.
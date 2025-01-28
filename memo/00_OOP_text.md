## \_\_method\_\_
1. `__init__` :
2. `__str__` : class가 문자열로 어떻게 보일 지 커스텀. 문자열을 return해야함.
3. `__repr__` : 객체를 문자열로 어떻게 표현할 지 커스텀. 문자열을 return해야함.
4. `__add__` : + 연산자를 커스텀. return값이 있어야함. 매개변수로는 self, other가 들어감.
5. `__sub__` : - 연산자를 커스텀. return값이 있어야함. 매개변수로는 self, other가 들어감.
6. `__mul__` : * 연산자를 커스텀. return값이 있어야함. 매개변수로는 self, other가 들어감.
7. `__truediv__` : / 연산자를 커스텀. return값이 있어야함. 매개변수로는 self, other가 들어감.
8. `__eq__` : == 연산자를 커스텀. return값이 있어야함. 매개변수로는 self, other가 들어감.
9. `__ne__` : != 연산자를 커스텀. return값이 있어야함. 매개변수로는 self, other가 들어감.
10. `__lt__` : < 연산자를 커스텀. return값이 있어야함. 매개변수로는 self, other가 들어감.
11. `__le__` : <= 연산자를 커스텀. return값이 있어야함. 매개변수로는 self, other가 들어감.
12. `__gt__` : > 연산자를 커스텀. return값이 있어야함. 매개변수로는 self, other가 들어감.
13. `__ge__` : >= 연산자를 커스텀. return값이 있어야함. 매개변수로는 self, other가 들어감.
14. `__len__` : len() 함수를 커스텀. return값이 있어야함. 매개변수로는 self가 들어감.
15. `__getitem__` : 인덱싱을 커스텀. return값이 있어야함. 매개변수로는 self, key가 들어감.
16. `__setitem__` : 인덱싱을 커스텀. return값이 있어야함. 매개변수로는 self, key, value가 들어감.
17. `__getattribute__(self, atrtribute_name)` : 문자열 return. 속성 호출 시 어떻게 보일 지를 커스텀. 안 쓰는 것이 좋음.

- `__method__`를 찾는 방법. class의 dir 출력. 클래스의 속성과 메소드를 보여줌.
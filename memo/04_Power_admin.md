### reivew의 전체 row말고 rating만 가져오고 싶음
- `room.review.all().values('rating')` : room의 review 중 rating만 가져옴
- 이 경우에는 query set이 조금 바뀌어서 `review.raing`을 사용할 수 없음
- 해당 코드의 반환값은 dictionary의 list임.
- `room.review.all().values('rating')` : `{'rating': 5}` 이런 식으로 반환됨.
- 이 경우에는
```python
for review in room.review.all().values('rating'):
    tot_rating += review['rating']
```
- 이런 식으로 사용해야 함.
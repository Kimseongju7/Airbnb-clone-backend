from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("<int:pk>/", views.UserDetail.as_view()),
    path("<int:pk>/tweets", views.UserTweets.as_view()),
]
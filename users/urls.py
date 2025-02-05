from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me/", views.Me.as_view()),
    path("@<str:username>/", views.PublicUser.as_view()),
    path("@<str:username>/reviews/", views.UserReviews.as_view()),
    path("<int:pk>/", views.UserDetail.as_view()),
    path("<int:pk>/tweets", views.UserTweets.as_view()),
]
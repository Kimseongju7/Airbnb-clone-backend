from django.urls import path

from rooms.urls import urlpatterns
from . import views

urlpatterns = [
    path("photos/<int:pk>/", views.PhotoDetail.as_view()),
]
from rest_framework.urls import path
from .views import Perks, PerkDetail

urlpatterns = [
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>/", PerkDetail.as_view()),
]
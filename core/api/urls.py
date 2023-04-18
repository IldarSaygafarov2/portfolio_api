from django.urls import path
from api import views

urlpatterns = [
    path("members/", views.MemberList.as_view()),
    path("services/", views.ServiceList.as_view()),
]

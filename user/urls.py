from django.contrib.auth.views import LogoutView
from django.urls import path
from user import views

urlpatterns=[
    path('signup/',views.SignUp.as_view(),name="signup"),

]
from django.urls import path
from . import views

urlpatterns=[
     path('',views.blogs,name="Blog"),
     path('post/login',views.user_login,name="Login"),
     path('post/signup',views.signup,name="SignUp"),
]

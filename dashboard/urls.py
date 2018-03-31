from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import  AuthRegister,Profile
from rest_framework_jwt.views import verify_jwt_token


urlpatterns=[
  url(r'^login/',obtain_jwt_token),
  url(r'^register/$', AuthRegister.as_view()),
  url(r'^auth-jwt-verify/', verify_jwt_token),
  url(r'^viewprofile/(?P<username>[A-Za-z0-9]+)/$', Profile.as_view()),
  ]

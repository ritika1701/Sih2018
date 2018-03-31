from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import  AuthRegister,Profile,StudentRegister,OtpRegister



urlpatterns=[
  url(r'^login/',obtain_jwt_token),
  url(r'^register/$', AuthRegister.as_view()),

  url(r'^studentportal/',StudentRegister.as_view()),
  url(r'^otp/',OtpRegister.as_view()),
  url(r'^viewprofile/(?P<username>[A-Za-z0-9]+)/$', Profile.as_view()),
  ]

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import  AuthRegister,Profile

urlpatterns=[
  url(r'^login/',obtain_jwt_token),
  url(r'^register/$', AuthRegister.as_view()),
  url(r'^viewprofile/(?P<username>[A-Za-z0-9]+)/$', Profile.as_view()),
  ]

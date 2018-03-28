from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import  AuthRegister

urlpatterns=[
  url(r'^login/',obtain_jwt_token),
  url(r'^register/$', AuthRegister.as_view()),
  ]

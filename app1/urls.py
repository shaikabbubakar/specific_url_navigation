from django.urls import path
from app1.views import *
app_name='abbu'
urlpatterns=[
    path('a1/',a1,name='a1'),
]
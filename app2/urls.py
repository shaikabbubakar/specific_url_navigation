from django.urls import path
from app2.views import *
app_name='bakar'
urlpatterns=[
    path('a2/',a2,name='a2'),
]
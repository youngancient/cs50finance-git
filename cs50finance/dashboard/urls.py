from django.urls import path 
from .views import index,upload

urlpatterns =[
    path('',index, name='dashboard'),
    path('upload',upload, name='upload'),
]

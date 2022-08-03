from django.urls import path 
from .views import index,upload
app_name = 'dashboard'
urlpatterns =[
    path('',index, name='index'),
    path('upload',upload, name='upload'),
]

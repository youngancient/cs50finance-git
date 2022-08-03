from django.urls import path 
from .views import index,upload, download, favicon_list, delete_view
app_name = 'dashboard'
urlpatterns =[
    path('',index, name='index'),
    path('upload',upload, name='upload'),
    path('download/<zip_id>',download, name='download'),
    path('delete/<int:pk>',delete_view, name='delete'),
    path('favicon_list',favicon_list, name='favicon_list'),
]

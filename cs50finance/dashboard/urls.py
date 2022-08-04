from django.urls import path 
from .views import index,upload, output,download, favicon_list, delete_view, save_view
app_name = 'dashboard'
urlpatterns =[
    path('',index, name='index'),
    path('upload',upload, name='upload'),
    path('output/<zip_id>',output, name='output'),
    path('save/<zip_id>',save_view, name='save'),
    path('download/<zip_id>',download, name='download'),
    path('delete/<int:pk>',delete_view, name='delete'),
    path('favicon_list',favicon_list, name='favicon_list'),
]

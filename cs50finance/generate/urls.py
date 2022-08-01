from  django.urls import path
from .views import generate_all

urlpatterns = [
    path('<model_id>',generate_all,name='generate')
]

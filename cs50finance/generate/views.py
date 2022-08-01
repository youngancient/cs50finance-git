from django.shortcuts import render
from favicons import Favicons
from django.core.files.storage import FileSystemStorage
from dashboard.models import Photo
from django.conf import settings
import os
# Create your views here.

# this function generates the favicon and zip
def generate_all(request,model_id):
    current_user = request.user
    output_path = os.path.join(settings.MEDIA_ROOT,f"/output/user{current_user.id}")
    # if os.path.isdir(output_path):
    #     print(f"/user{current_user.id} is created already")
    # else:
    #     os.mkdir(output_path)
    print(output_path)
    ph = Photo.objects.get(id=model_id)
    # print(ph.name)

    return render(request,'generate/index.html', context={
        'ph':ph,
    })
from django.shortcuts import render
from favicons import Favicons
from django.core.files.storage import FileSystemStorage
from dashboard.models import Photo
# Create your views here.

fs = FileSystemStorage(location='/media/output')
# this function generates the favicon and zip
def generate_all(request,model_id):
    ph = Photo.objects.get(id=model_id)
    print(ph.name)

    return render(request,'generate/index.html', context={
        'ph':ph,
    })
from django.shortcuts import redirect, render
from django.contrib import messages
# from django.core.files.storage import FileSystemStorage
from .models import Photo
# Create your views here.

# normal dashboard view
def index(request):
    return render(request,'dashboard/index.html')

def upload(request):
    if request.method == "POST":
        uploaded = request.FILES['upload']
        if uploaded.size / 1024 / 1024 > 2:
            messages.error(request,f"{uploaded.name} exceeds 2mB, Reupload a lesser one!")
            return redirect('dashboard')
        else:
            img_type = uploaded.content_type.split("/")[1]
            accepted = ['jpeg','png', 'svg+xml','svg']
            if img_type in accepted:
                photo = Photo()
                photo.name = uploaded.name
                photo.uploader =request.user
                photo.img_file = uploaded
                photo.save();
                messages.success(request,f"{uploaded.name} was uploaded successfully!")
                return redirect('generate',photo.id)
            else:
                messages.error(request,f"{uploaded.name} has an unsupported extension")
            return redirect('dashboard')
    

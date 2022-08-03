from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.core.files.storage import FileSystemStorage
from .models import Photo
# Create your views here.

# normal dashboard view
@login_required(redirect_field_name="next", login_url="accounts:login")
def index(request):
    return render(request,'dashboard/index.html')

@login_required(redirect_field_name="next", login_url="accounts:login")
def upload(request):
    if request.method == "POST":
        uploaded = request.FILES['upload']
        if uploaded.size / 1024 / 1024 > 2:
            messages.error(request,f"{uploaded.name} exceeds 2mB, Reupload a lesser one!")
            return redirect('dashboard:index')
        else:
            img_type = uploaded.content_type.split("/")[1]
            accepted = ['jpeg','png', 'svg+xml','svg']
            if img_type in accepted:
                photo = Photo()
                uploaded.name = uploaded.name.replace(" ","_")
                print(uploaded.name)
                photo.name = uploaded.name
                na_me = photo.name.split(".")
                photo.zip_name = na_me[0]
                photo.uploader =request.user
                photo.img_file = uploaded
                photo.save();
                messages.success(request,f"{uploaded.name} was uploaded successfully!")
                return redirect('generate',photo.id)
            else:
                messages.error(request,f"{uploaded.name} has an unsupported extension")
            return redirect('dashboard:index')
    

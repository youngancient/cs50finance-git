from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
from .models import Photo, Zip
from django.utils.encoding import smart_str
# Create your views here.
# unsaved_favs = Zip.objects.filter(is_saved = False)
# for unsaved in unsaved_favs:
#     unsaved.delete();

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
                return redirect('generate:generate_all',photo.id)
            else:
                messages.error(request,f"{uploaded.name} has an unsupported extension")
            return redirect('dashboard:index')
    
@login_required(redirect_field_name="next", login_url="accounts:login")
def output(request, zip_id):
    zip_list = Zip.objects.filter(id=zip_id)
    if zip_list.exists():
        zip = zip_list[0]
        if 'download' in request.POST:
            return redirect('dashboard:download',zip.id)
        elif 'save' in request.POST:
            zip.is_saved = True
            zip.save();
            messages.success(request,f"{zip.name} was saved successfully !")
            return redirect('dashboard:favicon_list')
        return render(request, 'dashboard/output.html',{
            'zip':zip,
        })   
    return render(request,'404.html')

@login_required(redirect_field_name="next", login_url="accounts:login")
def favicon_list(request):
    zips = Zip.objects.filter(downloader=request.user, is_saved=True)
    return render(request,'dashboard/favicon_list.html', {
        'zips':zips,
    })

@login_required(redirect_field_name="next", login_url="accounts:login")
def delete_view(request,pk):
    if request.method == "POST":
        del_zip =Zip.objects.get(pk=pk)
        del_zip.delete();
    return redirect('dashboard:favicon_list')

@login_required(redirect_field_name="next", login_url="accounts:login")
def save_view(request,zip_id):
    if request.method == "POST":
        save_zip =Zip.objects.get(id=zip_id)
        save_zip.is_saved = True
        save_zip.save();
    return redirect('dashboard:favicon_list')

@login_required(redirect_field_name="next", login_url="accounts:login")
def download(request,zip_id):
    if request.method == "POST":
        download_zip = Zip.objects.get(id=zip_id)
        return FileResponse(download_zip.zip_file, as_attachment=True)
    return redirect('dashboard:index')

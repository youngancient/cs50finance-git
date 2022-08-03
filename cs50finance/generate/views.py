from django.shortcuts import render
from favicons import Favicons
from django.contrib.auth.decorators import login_required
from django.conf import settings
from dashboard.models import Photo, Zip
import random
import shutil
from time import sleep
import os
# Create your views here.

base = settings.BASE_DIR 
output = f"{base}/media/output"
upload_dir = f"{base}/media/uploads"

# makes the output folder once
if not os.path.isdir(output):
    os.mkdir(output)
# this function generates the favicon and zip
@login_required(redirect_field_name="next", login_url="accounts:login")
def generate_all(request,model_id):
    current_user = request.user
    pulled_img = Photo.objects.get(id=model_id)
    some = random.randint(0,10000)
    
    output_path = f"{output}/user{current_user.id}"
    if not os.path.isdir(output_path):
        os.mkdir(output_path)

    WEB_SERVER_ROOT = f"{output_path}/{some}"
    # makes the folder where the output for a specific user will be
    if not os.path.isdir(WEB_SERVER_ROOT):
        os.mkdir(WEB_SERVER_ROOT)
    YOUR_ICON = f"{upload_dir}/{pulled_img.name}"
    # from the favicons library this generates the favicon and html codes
    with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
        # generate favicon
        favicons.generate()
        # As generator
        html = favicons.html_gen()
        #  as tuple
        html = favicons.html() # this would be passed as context to the templates

    file_name = "html.txt" #this is the txt file to hold the html codes
    html_file = open(os.path.join(WEB_SERVER_ROOT,file_name),"w")   #we open the file

    html_file.writelines("Copy the required code snippet into your HTML file\n Update the href* to correctly reference the location\n\n") 
    
    #we write the codes generated
    for code in html:
        html_file.writelines(code+"\n")
    html_file.close()

    # using shutil
    zip = Zip()
    zip.name = pulled_img.zip_name
    zip.downloader = request.user
    zip.zip_file = shutil.make_archive(f"{WEB_SERVER_ROOT}",'zip',f"{output_path}",f"{some}")
    zip.save();
    # remove directory
    shutil.rmtree(WEB_SERVER_ROOT)
    return render(request,'generate/index.html', context={
        'pulled_img':pulled_img,
    })
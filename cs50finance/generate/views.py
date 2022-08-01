from django.shortcuts import render
from favicons import Favicons
import zipfile
from django.conf import settings
from dashboard.models import Photo
import random
from time import sleep
import os
# Create your views here.

base = settings.BASE_DIR 
output = f"{base}/media/output"
upload_dir = f"{base}/media/uploads"
if not os.path.isdir(output):
    os.mkdir(output)
# this function generates the favicon and zip
def generate_all(request,model_id):
    current_user = request.user
    pulled_img = Photo.objects.get(id=model_id)
    WEB_SERVER_ROOT = f"{output}/user{current_user.id}"
    if not os.path.isdir(WEB_SERVER_ROOT):
        os.mkdir(WEB_SERVER_ROOT)
    YOUR_ICON = f"{upload_dir}/{pulled_img.name}"
    # print(ph.name)
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

    all_files= os.listdir(WEB_SERVER_ROOT)
    # this exempts .zip files and grabs the generated favicons
    needed_files = [file for file in all_files if file.endswith('.png') or file.endswith('.ico') or file.endswith('.jpeg') or file.endswith('.txt') ]


    # creates a zipfile path
    zip_name = f"{WEB_SERVER_ROOT}/user{current_user.id}.zip"
    if os.path.isfile(zip_name):
    # this creates a random number to prevent conflicts in names
        any = random.randint(0,1000)
        zip_name = f"{WEB_SERVER_ROOT}/user{id+any}.zip"
    with zipfile.ZipFile(zip_name, mode="w") as archive:
        for icon in needed_files:
            archive.write(f"{WEB_SERVER_ROOT}/{icon}")
        archive.close()

        # waits for 5s before continuing the process of deleting
    sleep(1)
    # deletes the unneeded files
    for file in needed_files:
        os.remove(os.path.join(WEB_SERVER_ROOT,file)) 
        
    return render(request,'generate/index.html', context={
        'pulled_img':pulled_img,
    })
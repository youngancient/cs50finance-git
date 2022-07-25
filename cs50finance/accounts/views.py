from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'home/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password_two = request.POST['password2']
        if password == password_two:
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                messages.success(request,'Account created successfully')
                return redirect('login')
    return render(request,'accounts/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,f'Welcome on board {user.username}')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials!')
            return redirect('login')
    return render(request,'accounts/login.html')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

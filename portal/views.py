from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from portal.models import Inform
from .forms import Dataform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):

    if request.method == "POST" :
        
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['mobile']
        password = request.POST['password']
        copassword = request.POST['copassword']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if password != copassword:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
   
        myuser = User.objects.create_user(username, email, password)
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your Account has been created succesfully!!")
        return redirect('login')
    
    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            username = user.username
            return redirect(request, 'vault', {username: username})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')

    return redirect('vault')         


def upload(request) :
    if request.method == 'POST':

        form = Dataform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vault')
    else:
        form = Dataform()
    return render(request, 'app.html', {
        'form': form
    })


def vault(request) :
    posts = Inform.objects.all

    return render(request, 'vault.html', {
        'posts': posts
    })
    
def delete_post(request, pk):
    if request.method == 'POST':
        post = post.objects.get(pk=pk)
        post.delete()
    return redirect('vault')

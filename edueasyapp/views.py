from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as kick_user
from django.contrib.auth import login as auth_login
from django.views.decorators.cache import cache_control
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    return redirect('/login')

def about(request):
    return render(request, 'about.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def course(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, 'courses.html')
    return redirect('/login')

def contact(request):
    return render(request, 'contact.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def resource(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, 'resources.html')
    return redirect('/login')
    
def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def python(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, 'python.html')
    return redirect('/login')

def logout(request):
    kick_user(request)
    request.session.flush()
    return redirect('/login')

def loguser(request): 
    if request.method == 'POST':         
        loginname = request.POST['loginname']
        loginpassword = request.POST['loginpassword']
        user = authenticate(request, username=loginname, password=loginpassword)
        if len(loginname) == 0:
            messages.error(request, 'Username cannot be empty')
            return redirect('/signup')
        elif len(loginname) < 8:
            messages.error(request, "Username must of minimum 8 characters")
            return redirect('/signup')
        elif len(loginpassword) < 12:
            messages.error(request, "Password must of minimum 12 characters")
            return redirect('/signup')
        elif len(loginpassword) == 0:
            messages.error(request, "Password cannot be empty")
            return redirect('/signup')
        else:
            if user is not None:
                auth_login(request, user)
                return redirect('/edueasy')
            else:
                messages.error(request, 'Invalid Password or Username')
                return redirect('/login')
            
def sign(request):
    if request.method == 'POST':  
        name = request.POST.get('username')
        fname = request.POST.get('f-name')
        lname = request.POST.get('l-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repass = request.POST.get('repassword')
        if (len(fname) or len(lname)) == 0:
            messages.error(request, 'First or last name cannot be empty')
            return redirect('/signup')
        elif len(name) == 0:
            messages.error(request, "Username cannot be empty")
            return redirect('/signup')
        elif len(name) < 8:
            messages.error(request, "Username must of minimum 8 characters")
            return redirect('/signup')
        elif User.objects.filter(username=name).exists():
            messages.error(request, 'Username is not available.Please try another.')
            return redirect('/signup')
        elif ' ' in name:
            messages.error(request, "Username cannot contain whitespace.")
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('/signup')
        elif len(password) == 0:
            messages.error(request, "Password cannot be empty")
            return redirect('/signup')
        elif len(password) < 12:
            messages.error(request, "Password must be of minimum 12 characters")
            return redirect('/signup')
        elif password != repass:
            messages.error(request, "Confirm password does not match")
            return redirect('/signup')
        else:
            myuser = User.objects.create_user(username=name, email=email, password=password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Congratulations!!! Your Edu-Easy's account has been created.")
            return redirect('/signup')

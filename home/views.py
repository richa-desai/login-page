''' doc '''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def index(request):
    ''' doc '''
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def login_user(request):
    ''' doc '''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_user(request):
    ''' doc '''
    logout(request)
    return redirect("/login")

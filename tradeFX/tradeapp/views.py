from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Trader
from django.contrib.auth.decorators import login_required

def logIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist:
            messages.error(request, 'This user has not been registered.')
            return render(request, 'login.html', {"error": True})
            
        if user:
            login(request, user)
            messages.success(request, 'Login was successful')
            return redirect('home')
        else:
            messages.error(request, 'Username and password does not match')
            return render(request, 'login.html', {"error": True})

    return render(request, 'login.html', {"messages": messages})

def logOut(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Registration was Successful')
            messages.success(request, 'Login with the credentials you registered with')
            return redirect('login')
        else:
            messages.error(request, "Your registration could not be completed succesfully")
    else:
        form = UserCreationForm
    return render(request, 'register.html', {'form': form, "messages": messages})

def home(request):
    return render(request, 'home.html')

@login_required
def user_dashboard(request, pk):
    trader = Trader.objects.get(id=pk)
    return render(request, 'user-dashboard.html', {'trader': trader})

@login_required
def admin_dashboard(request):
    traders = Trader.objects.all()
    return render(request, 'admin-dashboard.html', {'traders': traders})

from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . forms import usercf
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views import View

# Create your views here.

def home(request):
    return render(request, 'home.html')


def usercform(request):
    if request.method == "POST":
        frm = usercf(request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponseRedirect('/login/')
    else:
            frm = usercf()
    return render(request, 'usercfrom.html', {'form':frm})

def login_form(request):
    if request.method == "POST":
        frm = AuthenticationForm(request = request, data = request.POST)
        if frm.is_valid():
            uname = frm.cleaned_data['username']
            upass = frm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/success')
    else:       
        frm = AuthenticationForm()
    return render(request, 'login.html', {'form':frm})

def slogin(request):
    return render(request, 'success.html')

def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/login/')
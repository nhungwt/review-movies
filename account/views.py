from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from .forms import UserCreateForm

# Create your views here.


def loginCustom(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.htm', {'form': form})
    elif request.method == 'POST':
        user = authenticate(request, 
                            username=request.POST['username'], 
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, 'listMovie.htm')
        else:
            return render(request, 'login.htm', {'form': AuthenticationForm(), 'error': 'Information is incorrect!'})


def logoutCutom(request):
    logout(request)
    return render(request, 'listMovie.htm')


def register(request):
    if request.method == 'GET':
        form = UserCreateForm()
        return render(request, 'register.htm', {'form': form})
    elif request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass_confirm = request.POST['password2']
        if pass1 == pass_confirm:
            try:
                user = User.objects.create_user(username,password=pass1) # password=: Cần có không thì nó lưu vào đâu ý chứ ko phải trường 'pass'
                user.save()
                login(request, user)
                return render(request, 'listMovie.htm')
            except IntegrityError:
                return render(request, 'register.htm', {'form': UserCreateForm(), 'error': 'OUPS, username has been taken!'})
        else:
            return render(request, 'register.htm', {'form': UserCreateForm(), 'error': 'Password dose not match!'})

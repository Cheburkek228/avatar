from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

def logout_view(request):
    logout(request)
    return redirect("/")

def login_view(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user  =authenticate(request, username=user_name, password=password)
        if user:
            login(request, user)
            return redirect("/")
    return render(request, 'profiles/form.html', {'form': login_form})

def register_view(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        user = User.objects.create_user(username=user_name, email=email, password=password, is_staff=False)
        user.save()
        return redirect("/")
    return render(request, 'profiles/form.html', {'form': register_form, 'registration': True})
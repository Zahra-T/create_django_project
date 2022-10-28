from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(request.POST.get('next'))
            else:
                messages.error(request, 'Information isn\'t correct. Please try again.')
                return redirect('accounts:login')   
        redirected_to=request.GET.get('next', '/') 
        context={'redirected_to':redirected_to}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')
    
"""
    if request.user.is_authenticated:
        msg=f'user {request.user.username} is authenticated'
    else:
        msg=f'user is not authenticated'
    return render(request, 'accounts/login.html', {'msg':msg})"""

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('accounts:login')
            else:
                return redirect('accounts:signup')
        return render(request, 'accounts/signup.html')
    return redirect('/')
    
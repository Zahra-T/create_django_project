from email import message
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


def http_test(request):
    return HttpResponse('hello i am http test in a app')


def json_test(request):
    return JsonResponse({"name": "Zahra", "friends": {"f1": "sara", "f2": "mobina", "f3": "ali"}})


def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.name='unkown'
            data.save()
            messages.add_message(request, messages.SUCCESS, 'Your message submitted successfully.')
        else:   
            messages.add_message(request, messages.ERROR, 'Your message didn\'t submit. please try again.')
        return HttpResponseRedirect('/contact')
    form=ContactForm()
    return render(request, 'contact.html', {'form':form})


def about(request):
    return render(request, 'about.html')

def newsletter(request):
    if request.method=='POST':
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def test(request):
    if request.method=='POST':
        print('yes')
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form=ContactForm()
    return render(request, 'formtest.html', {'form':form})

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'zahraeset@gmail.com' , [user.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')
                        
                    return redirect ("/password_reset/done/")
            messages.error(request, 'An invalid email has been entered.')
            return redirect('myApp:password_reset')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})
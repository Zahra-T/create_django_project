from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages

def launch_view(request):
    return render(request, 'launch.html')

"""
def test_view(request):
    context={'name':'zahra', 'family':'taghipour'}
    return render(request, 'test.html', context=context)"""

def message_view(request):
    messages.success(request, 'Welcome To Dashboard!')
    return render(request, 'message.html')


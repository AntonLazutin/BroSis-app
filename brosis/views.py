import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import *


def index(request):
    users = User.objects.all()
    try:
        latest_message = Message.objects.all().latest('date')
    except Message.DoesNotExist:
        latest_message = None
    bro_count = Message.objects.filter(text='Bro!').count()
    sis_count = Message.objects.filter(text='Sis!').count()
    context = {'users': users, 'latest_message': latest_message, 'bro_count': bro_count, 'sis_count': sis_count}
    return render(request, 'brosis/index.html', context)


def create_message(request):
    if request.method == 'POST':
        if 'bro' in request.POST:
            text = 'Bro!'
        else:
            text = 'Sis!'
        message = Message.objects.create(author=request.user, text=text)
        message.save()
    return redirect('index')


def signup(request):
    return render(request, 'brosis/signup.html')


def logout_view(request):
    logout(request)
    return redirect('index')

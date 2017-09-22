from django.shortcuts import render, redirect
from main.models import *
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def index(request):
    try:
        lottery = Lottery.objects.all()[0]
    except:
        raise Http404
    lottery_percent = int((lottery.now_count * 100) / lottery.total_count)
    free_space= lottery.total_count-lottery.now_count
    return render(request, 'index.html', {'title': lottery.name, 'total_count': lottery.total_count,
                                          'now_count': lottery.now_count, 'perc': lottery_percent,
                                          'name': lottery.merchandise.name,
                                          'pic': lottery.merchandise.pic.url, 'free': free_space})


def login_page(request):
    if request.method == 'POST' and request.POST['password'] != '':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login (request, user)
            return HttpResponseRedirect("/")
        else:
            # error message here
            return render(request, 'registration/login.html', {'name': 'I AM ERROR'})
    else:
        return render(request, 'registration/login.html', {'name': request.user})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")

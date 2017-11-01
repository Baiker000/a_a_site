from django.shortcuts import render, redirect
from main.models import *
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegForm


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
                                          'pic': lottery.merchandise.pic.url, 'free': free_space, 'uniq': lottery.random_int})


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


def register(request):
    if request.user.is_authenticated:
        return render(request, 'registration/registration.html', {'error': 'Ты уже один из нас'}) #redirect to user page
    form = RegForm()
    if request.method == 'POST':
        form = RegForm(request.POST, request.FILES)
        if form.is_valid():
            reg_user=form.save()
            login(request, reg_user)
            return HttpResponseRedirect('/') #redirect to user page
    return render(request, 'registration/registration.html', {'form': form})



def involve_to_lottery(request):
    if not request.user.is_authenticated: return HttpResponseRedirect("/")
    try:
        coins = int(request.POST['coins'])
    except ValueError:
        coins = 0
    coins = coins if coins > 0 else 0
    add_user_into_lottery(request.user, request.POST['lottery'], coins)

    ### for test
    all_users_here=Lottery.objects.get(random_int=request.POST['lottery']).users.all()
    #all_users_here = UserScore.objects.all()
    ###
    return render(request, 'add.html', {'coins': coins, 'lottery':request.POST['lottery'], 'all_users':all_users_here})


def profile(request):
    return render(request, 'registration/profile.html')

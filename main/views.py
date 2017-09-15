from django.shortcuts import render
from main.models import *
from django.http import Http404


# Create your views here.

def index(request):
    try:
        lottery = Lottery.objects.all()[0]
    except:
        raise Http404

    lottery_percent = int((lottery.now_count * 100) / lottery.total_count)
    return render(request, 'index.html', {'title': lottery.name, 'total_count': lottery.total_count,
                                          'now_count': lottery.now_count, 'perc': lottery_percent,
                                          'name': lottery.merchandise.name,
                                          'pic': lottery.merchandise.pic.url})

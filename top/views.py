#from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from lib.members import Login
from senryu.models import Senryu

from pprint import pprint


def index(request):
    context = {}

    '''if 'member' in request.session:
        print('セッションは存在します')
        pprint(vars(request.session['member']))
        pprint(request.session['member'].email)
    else:
        print('セッションは存在しません')'''

    # そん時フィーリング
    senryu_random = Senryu.objects.filter(delete_flag = 0).order_by('?')[:1]
    if senryu_random:
        context['senryu_random'] = senryu_random[0]

    # 新着
    senryu_new = Senryu.objects.filter(delete_flag = 0).order_by('-created')[:1]
    if senryu_new:
        context['senryu_new'] = senryu_new[0]

    return render(request, 'top/index.html', context)

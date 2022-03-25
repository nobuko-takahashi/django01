from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Senryu
from .forms import SenryuRegist

from django.utils import timezone

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

'''def index(request):
    name = 'Taro'
    age = 20

    senryu_list = Senryu.objects.filter(delete_flag__exact = False).order_by('-created')

    return render(request, 'senryu/index.html',
        context={'name' : name, 'age' : age, 'senryu_list' : senryu_list,}
    )'''

def index(request):
    name = 'Taro'
    age = 20

    list = Senryu.objects.filter(delete_flag__exact = False).order_by('-created')
    paginator = Paginator(list, 2)
    page = request.GET.get('page', 1)

    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)
    #context = {'pages': pages}

    return render(request, 'senryu/index.html',
        context={'name' : name, 'age' : age, 'pages' : pages,}
    )

def regist(request):
    if request.method != 'POST':
        #フォームを変数にセット
        form = SenryuRegist()
    else:
        # 確認から戻ってきた場合
        form = SenryuRegist(request.POST)

    context = {'senryu_obj':form,}
    return render(request, 'senryu/regist.html', context)

def regist_confirm(request):
    context = {}
    if request.method == 'POST':
        senryu_obj = SenryuRegist(request.POST)
        context = {'senryu_obj':senryu_obj,}

        if senryu_obj.is_valid():
            # バリデーションOK
            return render(request, 'senryu/regist_confirm.html', context)
        else:
            # バリデーションNG
            context['err_msg'] = '入力に間違いがあります'
            return render(request, 'senryu/regist.html', context)

    else:
        return render(request, 'senryu/index.html', context)

def regist_complete(request):
    context = {}
    if request.method == 'POST':
        senryu_obj = SenryuRegist(request.POST)
        context = {'senryu_obj':senryu_obj,}

        if senryu_obj.is_valid():
            # バリデーションOK
            Senryu.objects.create(
                #uid = '',
                name = senryu_obj.cleaned_data['name'],
                ku1 = senryu_obj.cleaned_data['ku1'],
                ku2 = senryu_obj.cleaned_data['ku2'],
                ku3 = senryu_obj.cleaned_data['ku3'],
                comment = senryu_obj.cleaned_data['comment'],
                delete_flag = False,
                created = timezone.now(),
                updated = timezone.now(),
            )

            return render(request, 'senryu/regist_complete.html', context)
        else:
            # バリデーションNG
            context['err_msg'] = '入力に間違いがあります'
            return render(request, 'senryu/regist.html', context)
    else:
        return render(request, 'senryu/index.html', context)

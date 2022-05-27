from django.shortcuts import render, redirect
from .models import Members
from .forms import MemberRegist, MemberLogin, MemberPassword
from django.utils import timezone
from lib.members import Login
import hashlib

from pprint import pprint

def login(request):
    context = {}
    url = '/'

    if 'url' in request.GET:
        if len(request.GET['url']) > 0:
            url = request.GET['url']

    if request.method == 'POST':
        form = MemberLogin(request.POST)
        context['form'] = form
        if form.is_valid():
            # バリデーションOK、セッション登録
            member = Members.objects.filter(email = request.POST['email'], status = 1)[0]
            request.session['member'] = member
            return redirect(url)
        else:
            # バリデーションNG
            context['err_msg'] = '入力に間違いがあります'
    else:
        form = MemberLogin()
        context['form'] = form
        context['url'] = url
    return render(request, 'members/login.html',
        context = context
    )

def logout(request):
    if 'member' in request.session:
        del request.session['member']
    return redirect('/')

def regist(request):
    if request.method == 'POST':
        form = MemberRegist(request.POST)
    else:
        form = MemberRegist()
    return render(request, 'members/regist.html',
        context = {'form': form,}
    )

def regist_confirm(request):
    context = {}
    if request.method == 'POST':
        form = MemberRegist(request.POST)
        context = {'form':form,}

        if form.is_valid():
            # バリデーションOK
            return render(request, 'members/regist_confirm.html', context)
        else:
            # バリデーションNG
            context['err_msg'] = '入力に間違いがあります'
            return render(request, 'members/regist.html', context)

    else:
        return render(request, 'members/regist.html', context)

def regist_complete(request):
    context = {}
    if request.method == 'POST':
        form = MemberRegist(request.POST)
        context = {'form':form,}

        if form.is_valid():
            # バリデーションOK
            Members.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                password = hashlib.sha256(form.cleaned_data['password'].encode()).hexdigest(),
                status = 1,
                created = timezone.now(),
                updated = timezone.now(),
            )
            return render(request, 'members/regist_complete.html', context)
        else:
            # バリデーションNG
            context['err_msg'] = '入力に間違いがあります'
            return render(request, 'members/regist.html', context)

    else:
        return render(request, 'members/regist.html', context)

def edit(request):
    url = Login.get_login_url(request)
    if url:
        return redirect(url)

    context = {}
    if 'edit' in request.GET:
        edit = request.GET['edit']
        if edit == 'password':
            context = {'edit':'パスワードを変更しました'}
        if edit == 'email':
            context = {'edit':'メールアドレスを変更しました'}

    return render(request, 'members/edit.html', context)

def edit_password(request):
    url = Login.get_login_url(request)
    if url:
        return redirect(url)
    context = {}
    if request.method == 'POST':
        form = MemberPassword(request.POST)
        if form.is_valid():
            # バリデーションOK
            member = Members.objects.get(id = request.session['member'].id, status = 1)
            pprint(vars(member))
            member.password = hashlib.sha256(form.cleaned_data['password'].encode()).hexdigest()
            member.updated = timezone.now()
            member.save()

            request.session['member'] = member

            return redirect('/members/edit?edit=password')
        else:
            # バリデーションNG
            context['err_msg'] = '入力に間違いがあります'
    else:
        form = MemberPassword()

    context['form'] = form
    return render(request, 'members/edit_password.html', context)

def edit_email(request):
    url = Login.get_login_url(request)
    if url:
        return redirect(url)

    context = {}
    if request.method == 'POST':
        form = MemberEmail(request.POST)
        if form.is_valid():
            # バリデーションOK
            member = Members.objects.get(id = request.session['member'].id, status = 1)

            member.email = form.cleaned_data['email']
            member.updated = timezone.now()
            member.save()
            request.session['member'] = member

            return redirect('/members/edit?edit=email')
        else:
            # バリデーションNG
            context['err_msg'] = '入力に間違いがあります'
    else:
        form = MemberEmail()

    context['form'] = form
    return render(request, 'members/edit_email.html', context)

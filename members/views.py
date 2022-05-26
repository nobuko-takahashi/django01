from django.shortcuts import render
from .forms import MemberEdit

def login(request):
    return render(request, 'members/login.html',
        #context={'name' : name, 'age' : age, 'pages' : pages,}
    )

def edit(request):
    form = MemberEdit()
    '''context = {'form': form,}'''
    return render(request, 'members/edit.html',
        context={'form': form,}
    )

def edit_confirm(request):
    return render(request, 'members/edit_confirm.html',
        #context={'name' : name, 'age' : age, 'pages' : pages,}
    )

def edit_complated(request):
    return render(request, 'members/edit_confirm.html',
        #context={'name' : name, 'age' : age, 'pages' : pages,}
    )
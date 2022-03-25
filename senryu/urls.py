from django.urls import path
from . import views

app_name = "senryu"
urlpatterns = [
    path('', views.index, name='index'),
    path('regist', views.regist, name='regist'),
    path('regist_confirm', views.regist_confirm, name='regist_confirm'),
    path('regist_complete', views.regist_complete, name='regist_complete'),
]
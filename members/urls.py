from django.urls import path
from . import views

app_name = "members"
urlpatterns = [
    #path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('regist', views.regist, name='regist'),
    path('regist_confirm', views.regist_confirm, name='regist_confirm'),
    path('regist_complete', views.regist_complete, name='regist_complete'),
    path('edit', views.edit, name='edit'),
    path('edit_password', views.edit_password, name='edit_password'),
    path('edit_email', views.edit_email, name='edit_email'),
]
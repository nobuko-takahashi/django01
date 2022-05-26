from django.urls import path
from . import views

app_name = "members"
urlpatterns = [
    #path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('edit', views.edit, name='edit'),
    #path('edit_confirm', views.edit_confirm, name='edit_confirm'),
    #path('edit_complete', views.edit_complete, name='edit_complete'),
]
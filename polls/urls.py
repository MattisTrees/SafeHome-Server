from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('query_user_pwd', views.query_user_pwd, name='query_user_pwd'),
    path('add_device', views.add_device, name='add_device'),
]

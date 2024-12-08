from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('slogin', views.slogin, name='slogin'),
    path('login', views.llogin, name='login'),
    path('signin', views.signin, name='signin'),
    path('subSign', views.signIn, name='subSign'),
    path('amazon', views.amazon, name='affiliate'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product'),
    path('fContact', views.fContact, name='fContact'),
    path('cyber', views.cyber, name='cyber'),
    path('programe', views.code, name='code'),
	
]
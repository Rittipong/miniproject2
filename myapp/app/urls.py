from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('form',views.form),
    path('log', views.login),
    path('sign', views.signup),
    path('ne', views.news),
    path('re', views.reviews),
    path('m', views.mk),
    path('mi', views.minecraft),
    path('do', views.doomm),
    path('c', views.cy),
    path('s', views.si),
    path('remine', views.remine),
    path('red', views.redoom),
    path('recy', views.recy),
    path('resi', views.resi),
    path('remk', views.remk),
    path('addu', views.adduser),
    path('ulogin', views.custom_login),
    path('home', views.home),
    path('commine', views.commine),
    path('comdoom', views.comdoom),
    path('comspider', views.comspider),
    path('comcyber', views.comcyber),
    path('comblack', views.comblackmyt),
    path('re-minecraf', views.Reminecraf),
    path('re-doom', views.Redoom),
    path('re-spider', views.Respiderman),
    path('re-cyber', views.Recyberpunk),
    path('re-black', views.Reblackmyt),
    path('repas', views.repassword),

]
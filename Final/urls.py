"""
URL configuration for Final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Final.views import *
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls), path('home/',home,name='home'), path('aboutme',about_me,name='about_me'), path('abandonados/',abandonados,name='abandonados'), path('leidos/',leidos,name='leidos'),
    path('leyendo/',leyendo,name='leyendo'), path('porleer/',por_leer,name='por_leer'), path('borrar_leido/<libro_titulo>',borrar_leido,name='borrar_leido'), path('borrar_leyendo/<libro_titulo>',borrar_leyendo,name='borrar_leyendo'),
    path('borrar_por_leer/<libro_titulo>',borrar_porleer,name='borrar_por_leer'), path('borrar_abandonado/<libro_titulo>',borrar_abandonado,name='borrar_abandonado'),
    path('busqueda/',busqueda,name='busqueda'), path('resultado/',resultado_busqueda,name='resultado'), path('editar_abandonado/<libro_titulo>',editar_abandonado,name='editar_abandonado'),
    path('editar_leido/<libro_titulo>',editar_leido,name='editar_leido'), path('editar_leyendo/<libro_titulo>',editar_leyendo,name='editar_leyendo'), path('editar_por_leer/<libro_titulo>',editar_porleer,name='editar_por_leer'),
    path('login/',login_request,name='login'), path('registro/',register,name='registro'), path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'), path('editar_user',editar_user,name='editar_user'),
    path('cambiar_contraseña',cambiar_contraseña.as_view(),name='cambiar_contraseña')
]

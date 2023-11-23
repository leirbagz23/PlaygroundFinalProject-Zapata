#Para mostrar las vistas
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
#Para acceder a los modelos y formularios
from Lectura.models import *
from Lectura.forms import *
#Para login-logout-registro y edicion de usuarios
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
#Para limitar el acceso a los usuarios logeados
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#Pagina de inicio
def home(request):
    title='Home'
    leidos=Leidos.objects.all
    leyendo=Leyendo.objects.all
    por_leer=Por_Leer.objects.all
    abandonados=Abandonados.objects.all
    return render(request,'home.html',{'title':title,'abandonados':abandonados,'leidos':leidos,'leyendo':leyendo,'por_leer':por_leer})
#Pagina con informacion acerca del autor
def about_me(request):
    title='Acerca del autor'
    return render (request,'aboutme.html',{'title':title})
#Pagina que contiene el formulario para registrar objetos en el modelo abandonados
@login_required
def abandonados(request):
    title='Abandonados'
    abandonados=Abandonados.objects.all
    if request.method=="POST":
        abandonados_formulario=AbandonadosFormulario(request.POST)
        print(abandonados_formulario)
        if abandonados_formulario.is_valid():
            informacion=abandonados_formulario.cleaned_data
            abandonado=Abandonados(titulo=informacion["titulo"], autor=informacion["autor"], año_publicacion=informacion["año_publicacion"])
            abandonado.save()
            return render(request,'abandonados.html',{'title':title,'abandonados':abandonados})
    else:
        abandonados_formulario=Abandonados()
        return render(request,'abandonados.html',{'title':title,"abandonados_formulario":abandonados_formulario, 'abandonados':abandonados})
#Pagina que contiene el formulario para registrar objetos en el modelo por_leer
@login_required
def por_leer(request):
    title='Por leer'
    porleer=Por_Leer.objects.all
    if request.method=="POST":
        por_leer_formulario=PorLeerFormulario(request.POST)
        print(por_leer_formulario)
        if por_leer_formulario.is_valid():
            informacion=por_leer_formulario.cleaned_data
            por_leer=Por_Leer(titulo=informacion["titulo"], autor=informacion["autor"], año_publicacion=informacion["año_publicacion"])
            por_leer.save()
            return render(request,'porleer.html',{'title':title,'por_leer':porleer})
    else:
        por_leer_formulario=Por_Leer()
        return render(request,'porleer.html',{'title':title,"por_leer_formulario":por_leer_formulario,'por_leer':porleer})
#Pagina que contiene el formulario para registrar objetos en el modelo leidos
@login_required
def leidos(request):
    title='Leidos'
    leido=Leidos.objects.all
    if request.method=="POST":
        leidos_formulario=LeidosFormulario(request.POST)
        print(leidos_formulario)
        if leidos_formulario.is_valid():
            informacion=leidos_formulario.cleaned_data
            leidos=Leidos(titulo=informacion["titulo"], autor=informacion["autor"], año_publicacion=informacion["año_publicacion"])
            leidos.save()
            return render(request,'leidos.html',{'title':title,'leidos':leido})
    else:
        leidos_formulario=Leidos()
        return render(request,'leidos.html',{'title':title,"leidos_formulario":leidos_formulario, 'leidos':leido})
#Pagina que contiene el formulario para registrar objetos en el modelo leyendo
@login_required
def leyendo(request):
    title='Leyendo'
    leyendos=Leyendo.objects.all
    if request.method=="POST":
        leyendo_formulario=LeyendoFormulario(request.POST)
        print(leyendo_formulario)
        if leyendo_formulario.is_valid():
            informacion=leyendo_formulario.cleaned_data
            leyendo=Leyendo(titulo=informacion["titulo"], autor=informacion["autor"], año_publicacion=informacion["año_publicacion"])
            leyendo.save()
            return render(request,'leyendo.html',{'title':title, 'leyendo':leyendos})
    else:
        leyendo_formulario=Leyendo()
        return render(request,'leyendo.html',{'title':title,"leyendo_formulario":leyendo_formulario, 'leyendo':leyendos})
#Pagina utilizada para borrar un registro del modelo Abandonados
@login_required
def borrar_abandonado(request,libro_titulo):
    libro=Abandonados.objects.get(titulo=libro_titulo)
    libro.delete()
    abandonados=Leidos.objects.all
    leidos=Leidos.objects.all
    leyendo=Leyendo.objects.all
    por_leer=Por_Leer.objects.all
    return render(request,'home.html',{'abandonados':abandonados,'leidos':leidos,'leyendo':leyendo,'por_leer':por_leer})
#Pagina utilizada para borrar un registro del modelo Leidos
@login_required
def borrar_leido(request,libro_titulo):
    libro=Leidos.objects.get(titulo=libro_titulo)
    libro.delete()
    abandonados=Leidos.objects.all
    leidos=Leidos.objects.all
    leyendo=Leyendo.objects.all
    por_leer=Por_Leer.objects.all
    return render(request,'home.html',{'abandonados':abandonados,'leidos':leidos,'leyendo':leyendo,'por_leer':por_leer})
#Pagina utilizada para borrar un registro del modelo Leyendo
@login_required
def borrar_leyendo(request,libro_titulo):
    libro=Leyendo.objects.get(titulo=libro_titulo)
    libro.delete()
    abandonados=Leidos.objects.all
    leidos=Leidos.objects.all
    leyendo=Leyendo.objects.all
    por_leer=Por_Leer.objects.all
    return render(request,'home.html',{'abandonados':abandonados,'leidos':leidos,'leyendo':leyendo,'por_leer':por_leer})
#Pagina utilizada para borrar un registro del modelo Por_Leer
@login_required
def borrar_porleer(request,libro_titulo):
    libro=Por_Leer.objects.get(titulo=libro_titulo)
    libro.delete()
    abandonados=Leidos.objects.all
    leidos=Leidos.objects.all
    leyendo=Leyendo.objects.all
    por_leer=Por_Leer.objects.all
    return render(request,'home.html',{'abandonados':abandonados,'leidos':leidos,'leyendo':leyendo,'por_leer':por_leer})
#Pagina que contiene el formulario para realizar busquedas en las bases de datos, pudiendo buscar por autor, por titulo de libro o por año de publicación
@login_required
def busqueda(request):
    title='Busqueda en las bases de datos'
    return render(request,'busqueda.html',{'title':title})
#Pagina que muestra los resultados obtenidos de acuerdo a la búsqueda realizada en la página busqueda
@login_required
def resultado_busqueda(request):
    title='Resultados de la búsqueda'
    if request.GET["titulo"]:
        busqueda=request.GET["titulo"]
        resultado1=Leidos.objects.filter(titulo__icontains=busqueda)
        resultado2=Leyendo.objects.filter(titulo__icontains=busqueda)
        resultado3=Por_Leer.objects.filter(titulo__icontains=busqueda)
        resultado4=Abandonados.objects.filter(titulo__icontains=busqueda)
        return render(request,'resultado.html',{'title':title, 'busqueda':busqueda,'resultado1':resultado1,'resultado2':resultado2,'resultado3':resultado3, 'resultado4':resultado4})
    elif request.GET["autor"]:
        busqueda=request.GET["autor"]
        resultado1=Leidos.objects.filter(autor__icontains=busqueda)
        resultado2=Leyendo.objects.filter(autor__icontains=busqueda)
        resultado3=Por_Leer.objects.filter(autor__icontains=busqueda)
        resultado4=Abandonados.objects.filter(autor__icontains=busqueda)
        return render(request,'resultado.html',{'title':title,'busqueda':busqueda,'resultado1':resultado1,'resultado2':resultado2,'resultado3':resultado3, 'resultado4':resultado4 })
    elif request.GET["año_publicacion"]:
        busqueda=request.GET["año_publicacion"]
        resultado1=Leidos.objects.filter(año_publicacion__icontains=busqueda)
        resultado2=Leyendo.objects.filter(año_publicacion__icontains=busqueda)
        resultado3=Por_Leer.objects.filter(año_publicacion__icontains=busqueda)
        resultado4=Abandonados.objects.filter(año_publicacion__icontains=busqueda)
        return render(request,'resultado.html',{'title':title,'busqueda':busqueda,'resultado1':resultado1,'resultado2':resultado2,'resultado3':resultado3, 'resultado4': resultado4})
    else:
        return HttpResponse('No se realizó ninguna búsqueda')
#Pagina utilizada para editar algun registro del modelo Abandonados
@login_required
def editar_abandonado(request,libro_titulo):
    title='Editar libro abandonado'
    abandonado=Abandonados.objects.get(titulo=libro_titulo)
    if request.method=='POST':
        formulario=AbandonadosFormulario(request.POST)
        print(formulario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            abandonado.titulo=informacion['titulo']
            abandonado.autor=informacion['autor']
            abandonado.año_publicacion=informacion['año_publicacion']
            abandonado.save()
            return render(request,'abandonados.html',{'title':title})
    else:
        formulario=AbandonadosFormulario(initial={'titulo':abandonado.titulo,'autor':abandonado.autor,'año_publicacion':abandonado.año_publicacion})
        return render(request,'editarabandonado.html',{'title':title,'formulario':formulario,})
#Pagina utilizada para editar algun registro del modelo Leidos
@login_required
def editar_leido(request,libro_titulo):
    title='Editar libro leido'
    leido=Leidos.objects.get(titulo=libro_titulo)
    if request.method=='POST':
        formulario=LeidosFormulario(request.POST)
        print(formulario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            leido.titulo=informacion['titulo']
            leido.autor=informacion['autor']
            leido.año_publicacion=informacion['año_publicacion']
            leido.save()
            return render(request,'leidos.html',{'title':title})
    else:
        formulario=LeidosFormulario(initial={'titulo':leido.titulo,'autor':leido.autor,'año_publicacion':leido.año_publicacion})
        return render(request,'editarleido.html',{'title':title,'formulario':formulario,})
#Pagina utilizada para editar algun registro del modelo Leyendo
@login_required
def editar_leyendo(request,libro_titulo):
    title='Editar libro en lectura actual'
    leyendo=Leyendo.objects.get(titulo=libro_titulo)
    if request.method=='POST':
        formulario=LeyendoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            leyendo.titulo=informacion['titulo']
            leyendo.autor=informacion['autor']
            leyendo.año_publicacion=informacion['año_publicacion']
            leyendo.save()
            return render(request,'leyendo.html',{'title':title})
    else:
        formulario=LeyendoFormulario(initial={'titulo':leyendo.titulo,'autor':leyendo.autor,'año_publicacion':leyendo.año_publicacion})
        return render(request,'editarleyendo.html',{'title':title,'formulario':formulario,})
#Pagina utilizada para editar algun registro del modelo Por_Leer
@login_required
def editar_porleer(request,libro_titulo):
    title='Editar libro por leer'
    porleer=Por_Leer.objects.get(titulo=libro_titulo)
    if request.method=='POST':
        formulario=PorLeerFormulario(request.POST)
        print(formulario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            porleer.titulo=informacion['titulo']
            porleer.autor=informacion['autor']
            porleer.año_publicacion=informacion['año_publicacion']
            porleer.save()
            return render(request,'porleer.html',{'title':title})
    else:
        formulario=LeyendoFormulario(initial={'titulo':porleer.titulo,'autor':porleer.autor,'año_publicacion':porleer.año_publicacion})
        return render(request,'editarporleer.html',{'title':title,'formulario':formulario,})
#Pagina utilizada para hacer login al sitio
def login_request(request):
    title='Iniciar Sesión'
    if request.method=='POST':
        form=AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password')
            user=authenticate(username=usuario,password=contraseña)
            login(request,user)
            message='Bienvenido/a {}'.format(user.username)
            return render(request,'home.html',{'message':message})
    else:
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form,'title':title})
    return HttpResponse('Login fallido, intentar de vuelta')
#Pagina para hacer el registro en el sitio
def register(request):
    title='Registro de usuario nuevo'
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            message='Usuario creado con éxito'
            return render(request,'home.html',{'title':title,'message':message})
    else:
        form=UserCreationForm()
        return render(request,'registro.html',{'title':title,'form':form})
    return HttpResponse('Registro fallido, intentar de vuelta')
#Pagina para editar datos de usuario registrado
def editar_user(request):
    title='Editar usuario'
    if request.method=='POST':
        form=UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            message='Usuario editado con éxito'
            return render(request,'home.html',{'title':title,'message':message})
    else:
        form=UserEditForm(request.POST, instance=request.user)
        return render(request,'editaruser.html',{'title':title,'form':form})
    return HttpResponse('Editado fallido, intentar de vuelta')
#Pagina para cambiar contraseña
class cambiar_contraseña(LoginRequiredMixin,PasswordChangeView):
    template_name='cambiarcontraseña.html'
    success_url=reverse_lazy('editar_user')






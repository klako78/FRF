from functools import total_ordering
from reprlib import recursive_repr
from turtle import position
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render 
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,View,CreateView
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import *
import os
from django.conf import settings
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .generar_acta import render_to_pdf
# Create your views here.
def inicio(request):
    return render(request, 'paginas/base.html')

def listas(request):
    return render(request, 'paginas/listados.html')

def participantes(request):
   formularion=participanteform(request.POST or None, request.FILES or None)
   if formularion.is_valid and request.POST:
        formularion.save()
        return redirect('participantes')
   return render(request,'paginas/Participantes.html',{'formulario':formularion})

def datos_acordeonero(request,id):
    busqueda=request.GET.get("busqueda")
    participante=concursante.objects.filter(
        Q(categoria='ACORDEONERO')&
        Q(ronda=id))
    if busqueda:
        participante=concursante.objects.filter(
            Q(nombre__icontains=busqueda)

        ).distinct()
    return render(request,'paginas/califiaciones.html', {'suscriptor': participante})
pass

def datos_piqueria(request,id):
    busqueda=request.GET.get("busqueda")
    participante=concursante.objects.filter(Q(categoria='PIQUERIA')&
        Q(ronda=id))
    if busqueda:
        participante=concursante.objects.filter(
            Q(nombre__icontains=busqueda)

        ).distinct()
    return render(request,'paginas/califiaciones_piqueria.html', {'suscriptor': participante})
pass

def datos_piqueria_infantil(request,id):
    busqueda=request.GET.get("busqueda")
    participante=concursante.objects.filter(Q(categoria='PIQUERIA INFANTIL')&
        Q(ronda=id))
    if busqueda:
        participante=concursante.objects.filter(
            Q(nombre__icontains=busqueda)

        ).distinct()
    return render(request,'paginas/califiaciones_piqueria.html', {'suscriptor': participante})
pass

def datos_inedita(request,id):
    busqueda=request.GET.get("busqueda")
    participante=concursante.objects.filter(Q(categoria='CANCION INEDITA')&
        Q(ronda=id))
    if busqueda:
        participante=concursante.objects.filter(
            Q(cancion__icontains=busqueda)

        ).distinct()
    return render(request,'paginas/cancion_inedita.html', {'suscriptor': participante})
pass

def enviar(request,id):
    cedula=int(id)
    total=float(request.POST['total'])
    try:
        ron=1 
        concursante.objects.filter(cedula=cedula).update(puntaje=total) 
        return redirect('acordeonero',{ 'id':ron })
    except Exception as e:
          return HttpResponse(e)
pass

def listado_acordeonero(request,id):
    busqueda='ACORDEONERO'
    suscriptor=concursante.objects.filter(
            Q(categoria=busqueda)&
        Q(ronda=id)).order_by('-puntaje')

        
    
    return render(request,'paginas/listado.html', {'suscriptor': suscriptor})
pass
        
def listado_piqueria(request,id):
    busqueda='PIQUERIA'
    suscriptor=concursante.objects.filter(
            Q(categoria=busqueda)&
        Q(ronda=id)).order_by('-puntaje')

        
    
    return render(request,'paginas/listado.html', {'suscriptor': suscriptor})
pass 

def listado_piqueria_infantil(request,id):
    busqueda='PIQUERIA INFANTIL'
    suscriptor=concursante.objects.filter(
            Q(categoria=busqueda)&
        Q(ronda=id)).order_by('-puntaje')

        
    
    return render(request,'paginas/listado.html', {'suscriptor': suscriptor})
pass

def listado_cancion_inedita(request,id):
    busqueda='CANCION INEDITA'
    suscriptor=concursante.objects.filter(
            Q(categoria=busqueda)&
        Q(ronda=id)).order_by('-puntaje')

        
    
    return render(request,'paginas/listado_cancion.html', {'suscriptor': suscriptor})
pass


def acta(request,id):
    busqueda='ACORDEONERO'
    suscriptor=concursante.objects.filter(
            Q(categoria=busqueda)&
        Q(ronda=id)).order_by('-puntaje')

        
    
    return render(request,'paginas/actas.html', {'suscriptor': suscriptor})
pass

class acta(View):
    model=concursante
    template_name='paginas/actas.html'
    context_object_name='concursante'

def generar_acta_acordeonero(request,ron,cat):
        busqueda=cat
        fase=ron
        suscriptor=concursante.objects.filter(
            Q(categoria=busqueda)&
        Q(ronda=fase)).order_by('-puntaje')
        limite=suscriptor.count()/2
        pocicion=1
        for i in suscriptor:
            concursante.objects.filter(cedula=i.cedula).update(puntaje=0)
            concursante.objects.filter(cedula=i.cedula).update(ronda=str(2))  
            if pocicion>=limite:
                break  
            pocicion+=1
        acta=concursante.objects.filter(
            Q(categoria=busqueda)&
            Q(ronda='2')).order_by('-puntaje')

        data={
            'suscriptor': acta

        } 
        pdf=render_to_pdf('paginas/actas.html',data) 
        return HttpResponse(pdf,content_type='application/pdf')
        
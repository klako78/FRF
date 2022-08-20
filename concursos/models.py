from asyncio.proactor_events import _ProactorSocketTransport
from collections import UserList, UserString
from sre_constants import CATEGORY_LINEBREAK
from django.db import models
from django import forms
from django.db.models.enums import Choices, IntegerChoices
from django.db.models.fields import IntegerField
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import request
from django.utils import timezone
from django.conf import settings 
from django.contrib.auth import get_user_model
from pkg_resources import to_filename
import uuid
from .choices import *
# Create your models here.
class categoria(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.TextField(max_length=100,verbose_name="Nombre")
    def nombre(self):
        return self.nombre
    
    def __str__(self):
        return self.nombre()

class participantes(models.Model):
    cedula=models.IntegerField(primary_key=True,verbose_name="Cedula")
    nombre=models.CharField(max_length=100,verbose_name="Nombre")
    cancion=models.CharField(max_length=100,verbose_name="Nombre de la cancion si aplica" ,null=True,blank=True)
    categoria=models.CharField(verbose_name='Categoria',choices=categorias,max_length=100)


class concursante(models.Model):
    cedula=models.IntegerField(primary_key=True,verbose_name="Cedula")
    nombre=models.CharField(max_length=100,verbose_name="Nombre")
    cancion=models.CharField(max_length=100,verbose_name="Nombre de la cancion si aplica" ,null=True,blank=True)
    categoria=models.CharField(verbose_name='Categoria',choices=categorias,max_length=100)
    ronda=models.CharField(max_length=100,verbose_name="Ronda" ,default="1")
    puntaje=models.DecimalField(max_digits = 5, decimal_places = 2,verbose_name="Puntaje",default="0.0")
    
        
    def __str__(self):
        fila= 'Cedula'+ self.cedula + '-' + 'Nombre' + self.nombre 
        + '-' + 'Cancion'+ self.cancion 
        
        
        return super().__str__()




class calificacion_acordeonero(models.Model):
    cedula=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100,verbose_name='Tipo')
    total=models.DecimalField(max_digits = 5, decimal_places = 2,verbose_name="Puntaje")
    ronda=models.CharField(max_length=100,verbose_name="Ronda" ,null=True,blank=True)
    

class calificacion_cancion(models.Model):
    id=models.AutoField(primary_key=True)
    cancion=models.CharField(max_length=100,verbose_name='Tipo')
    fecha=models.DateField(auto_now_add=True)
    total_1=models.IntegerField(verbose_name="Juez 1")
    total_2=models.IntegerField(verbose_name="Juez 2")
    total_3=models.IntegerField(verbose_name="Juez 3")

class calificacion_piqueria(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,verbose_name='Tipo')
    fecha=models.DateField(auto_now_add=True)
    total_1=models.IntegerField(verbose_name="Juez 1")
    total_2=models.IntegerField(verbose_name="Juez 2")
    total_3=models.IntegerField(verbose_name="Juez 3")
    

from dataclasses import field, fields
from logging import PlaceHolder
from typing import Sequence, Tuple
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django import forms
from django.db.models.fields import TextField
from django.forms import widgets
from django.forms.fields import ChoiceField
from django.utils.regex_helper import Choice
from .models import *


class participanteform(forms.ModelForm):
    class Meta:
        model=concursante
        fields= '__all__'
        exclude=['ronda','puntaje']


           

       
        

from ast import pattern

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('listados', views.listas, name='listados'),
    path('participantes', views.participantes, name='participantes'),
    path('acordeonero/<id>',views.datos_acordeonero,name='acordeonero'),
    path('piqueria1/<id>',views.datos_piqueria,name='piqueria1'),
    path('piqueria_infantil1/<id>',views.datos_piqueria_infantil,name='piqueria_infantil1'),
    path('inedita1/<id>',views.datos_inedita,name='inedita1'),
    path('enviar/<int:id>',views.enviar,name='enviar'),
    path('listado_acordeonero/<id>',views.listado_acordeonero,name='listado_acordeonero'),
    path('listado_piqueria/<id>',views.listado_piqueria,name='listado_piqueria'),
    path('listado_piqueria_infantil/<id>',views.listado_piqueria_infantil,name='listado_piqueria_infantil'),
    path('listado_cancion_inedita/<id>',views.listado_cancion_inedita,name='listado_cancion_inedita'),
    path('generar_acta_acordeonero/<ron>/<cat>',views.generar_acta_acordeonero,name='generar_acta_acordeonero'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_citas, name='listar_cita'),
    path('nueva/', views.nueva_cita, name='nueva_cita'),
    path('editar/<int:id>/', views.editar_cita, name='editar_cita'),
    path('cancelar/<int:id>/', views.cancelar_cita, name='cancelar_cita'),
    path('eliminar/<int:id>/', views.eliminar_cita, name='eliminar_cita'),
]


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cita
from .forms import CitaForm

# Listar citas
def listar_citas(request):
    citas = Cita.objects.all()
    return render(request, 'citas/listar_cita.html', {'citas': citas})

# Crear nueva cita
def nueva_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cita agregada correctamente")
            return redirect('listar_cita')
    else:
        form = CitaForm()
    return render(request, 'citas/nueva_cita.html', {'form': form})

# Editar cita
def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request, "Cita editada correctamente")
            return redirect('listar_cita')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'citas/editar_cita.html', {'form': form})

# Cancelar cita
def cancelar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    cita.estado = "Cancelada"
    cita.save()
    messages.success(request, "Cita cancelada correctamente")
    return redirect('listar_cita')

# Eliminar cita
def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    cita.delete()
    messages.success(request, "Cita eliminada correctamente")
    return redirect('listar_cita')

import re
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages
from django.forms import ValidationError
from django.contrib.auth.decorators import permission_required
from .forms import CustomUserCreationForm,ContactoForm, FlanForm
from .models import Flan

# Create your views here.

def home(request):
    flanes = Flan.objects.all()
    data = {
        'flanes': flanes
    }
    return render(request,'app/index.html',data)

def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request,user)
            return redirect(to='home')
        data['form'] = formulario
    return render(request,'registration/registro.html',data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Solicitud de Contacto Generada."
        else:
            data['form'] = formulario
    return render(request,'app/contacto.html',data)

def agregar_producto(request):
    data = {
        'form':FlanForm()
    }
    if request.method == 'POST':
        formulario = FlanForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Flan Registrado")
            return redirect(to='listar_productos')
        else:
            data['form'] = formulario

    return render(request,'app/producto/agregar.html',data)

def listar_productos(request):
    flanes = Flan.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(flanes,4)
        flanes = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity':flanes,
        'paginator':paginator
    }
    return render(request,'app/producto/listar.html',data)

def modificar_producto(request,id):
    producto = get_object_or_404(Flan,id=id)
    data = {
        'form':FlanForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = FlanForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"flan modificado correctamente")
            return redirect(to="listar_productos")
        data['form'] = formulario

    return render(request, 'app/producto/modificar.html',data)

@permission_required('app.delete_flan')
def eliminar_producto(request,id):
    flan = get_object_or_404(Flan,id = id)
    flan.delete()
    messages.success(request,"Flan eliminado correctamente")

    return redirect(to="listar_productos")
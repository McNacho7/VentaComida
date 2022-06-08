from gc import get_objects
from django.shortcuts import render
from .models import comidagatos, comidaperro
from .forms import comidagatoform

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def gatos(request):
    return render(request, 'core/gatos.html')

def accesorios(request):
    return render(request, 'core/accesorios.html')

def formulariocontacto(request):
    return render(request, 'core/formulariocontacto.html')

def login(request):
    return render(request, 'core/login.html')

def mostrarperros(request):
    return render(request, 'core/mostrarperros.html')

def perros(request):
    return render(request, 'core/perros.html')

def carro(request):
    return render(request, 'core/carro.html')

def listarproductos(request):
    comidaGA = comidagatos.objects.all()
    datos ={
        'comida': comidaGA
    }
    return render(request, 'core/listarproductos.html',datos)

def formagregar(request):
    data ={
        'form': comidagatoform()
    }
    if request.method =='POST':
        formulario = comidagatoform(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"]= formulario
    
    return render(request, 'core/formagregar.html', data)

def formModificar(request,id):
        comida = comidagatos.objects.get(codigo=id)
        datos={
            'form': comidagatoform(instance=comida)
        }
        return render(request, 'core/formModificar.html',datos)





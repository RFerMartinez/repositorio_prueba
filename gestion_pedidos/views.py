from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestion_pedidos.models import Articulos


# Create your views here.

def busqueda_productos(request):
    return render(request, 'busqueda_producto.html')

def buscar(request):

    if request.GET['prd']:
        #mensaje = 'Art buscado: %r' %request.GET['prd']

        producto = request.GET['prd'] #aqui se almacena el nombre del producto que he insertado en el campo de busqueda

        articulos = Articulos.objects.filter(nombre__icontains = producto)

        return render(request, 'resultados_busqueda.html', {'articulos': articulos, 'query': producto})
    
    else:
        mensaje = 'No has introducido nada'
        return HttpResponse(mensaje)


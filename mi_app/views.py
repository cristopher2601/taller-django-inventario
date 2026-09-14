from django.shortcuts import render, redirect
from django.db.models import Sum, Count
from .models import Repuesto

def ingresar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')

        # Guardar en la base de datos
        Repuesto.objects.create(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            cantidad=cantidad,
            precio=precio
        )
        return redirect('inventario')

    return render(request, 'mi_app/ingresar.html')

def inventario(request):
    # 1. Obtener todos los repuestos
    productos = Repuesto.objects.all()

    # 2. Calcular los datos para las tarjetas métricas (Widgets)
    total_unidades = Repuesto.objects.aggregate(total=Sum('cantidad'))['total'] or 0
    total_critico = Repuesto.objects.filter(cantidad__lte=3).count() # Cuenta repuestos con stock <= 3
    total_categorias = Repuesto.objects.values('categoria').distinct().count()

    context = {
        'productos': productos,
        'total_unidades': total_unidades,
        'total_critico': total_critico,
        'total_categorias': total_categorias,
    }

    # CAMBIO IMPORTANTE: Renderizar 'inventario.html', NO 'base.html'
    return render(request, 'mi_app/inventario.html', context)

def alertas(request):
    return render(request, 'mi_app/alerta_Stock.html')

def proveedores(request):
    return render(request, 'mi_app/proveedores.html')

# Create your views here.

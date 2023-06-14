from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404

# Create your views here.

def all_products(request):
    """A view to show all products,
    including sorting and searching queries"""  

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show the details of thte product"""  

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

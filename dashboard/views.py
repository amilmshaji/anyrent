from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from products.models import House_Product, Car_Product



def myproducts(request, category_slug=None):

    # if request.user.is_authenticated:
    h_products = House_Product.objects.all().filter(is_available=True,).order_by('id')
    c_products = Car_Product.objects.all().filter(is_available=True,).order_by('id')



    context = {
        'h_products' : h_products,
        'c_products': c_products,


    }
    return render(request, 'myproducts.html', context)
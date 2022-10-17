from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from .models import House_Product, All_Products
from .models import Car_Product



def Category(request):

    return render(request, 'category.html')

@login_required(login_url='login')

def add_house(request):
    if request.method=="POST":
        type=request.POST.get('type')
        furnish=request.POST.get('furnish')
        bedroom=request.POST.get('bedroom')
        bathroom=request.POST.get('bathroom')

        builtup = request.POST.get('builtup')
        capacity = request.POST.get('capacity')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        house=House_Product(type=type,furnish=furnish,bedroom=bedroom,bathroom=bathroom,
                            builtup=builtup,capacity=capacity,rent=rent,ad_title=ad_title,add_info=add_info,images=images)
        house.save()
        return redirect('/')
    return render(request, 'add_house.html')




@login_required(login_url='login')

def add_car(request):
    if request.method=="POST":
        brand=request.POST.get('brand')
        fuel=request.POST.get('fuel')
        driven=request.POST.get('driven')
        own=request.POST.get('own')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        car=Car_Product(brand=brand,fuel=fuel,driven=driven,own=own,
                            rent=rent,ad_title=ad_title,add_info=add_info,images=images)
        car.save()
        return redirect('/')
    return render(request, 'add_car.html')


from django.shortcuts import render, redirect

# Create your views here.
from .models import  Bike_Product


def add_bike(request):
    if request.method=="POST":
        brand=request.POST.get('brand')
        # year=request.POST.get('year')
        driven=request.POST.get('driven')
        own=request.POST.get('own')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        bike=Bike_Product(brand=brand,driven=driven,own=own,
                            rent=rent,ad_title=ad_title,add_info=add_info,images=images)
        bike.save()
        return redirect('/')
    return render(request, 'add_bike.html')

from .models import Furn_Product


def add_furn(request):
    if request.method=="POST":
        type = request.POST.get('type')

        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        car=Furn_Product(type=type,rent=rent,ad_title=ad_title,add_info=add_info,images=images)
        car.save()
        return redirect('/')
    return render(request, 'add_furn.html')


from .models import Other_Product


def add_other(request):
    if request.method=="POST":
        type = request.POST.get('type')

        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        car=Other_Product(type=type,rent=rent,ad_title=ad_title,add_info=add_info,images=images)
        car.save()
        return redirect('/')
    return render(request, 'add_other.html')


# def all_products(request, total=0, quantity=0, cart_item=None, cart_items=None):
#     try:
#         tax = 0
#         grand_total = 0
#         if request.user.is_authenticated:
#             p_items = All_Products.objects.filter(
#                 user=request.user, is_active=True)
#
#         for p_item in p_items:
#             total += (p_item.product.price * p_item.quantity)
#             quantity += p_item.quantity
#         tax = (2 * total) / 100
#         grand_total = total + tax
#     except ObjectDoesNotExist:
#         pass
#
#     context = {
#         'total': total,
#         'quantity': quantity,
#         'p_items': p_items,
#         'tax': tax,
#         'grand_total': grand_total
#     }
#
#     return render(request, 'myproducts.html', context)

def all_products(request):
    if request.user.is_authenticated:
        allproducts = All_Products.objects.all().filter(user=request.user).order_by('id')
    context = {
        'allproducts': allproducts

    }
    return render(request, 'myproducts.html', context)

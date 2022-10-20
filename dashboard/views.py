from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from accounts.models import Account
from products.models import House_Product, Car_Product






@login_required(login_url='login')
def dashboard(request):
    # orders = Order.objects.order_by(
    #     '-created_at').filter(user_id=request.user.id, is_ordered=True)
    # order_count = orders.count()
    userprofile=Account.objects.get(id=request.user.id)
    context = {
        # 'orders_count': order_count,
        'userprofile':userprofile,
    }
    return render(request, 'dashboard/dash-my-profile.html', context)

def editprofile(request):
    # orders = Order.objects.order_by(
    #     '-created_at').filter(user_id=request.user.id, is_ordered=True)
    # order_count = orders.count()
    userprofile=Account.objects.get(id=request.user.id)
    context = {
        # 'orders_count': order_count,
        'userprofile':userprofile,
    }
    return render(request, 'dashboard/dash-edit-profile.html', context)

def myproducts(request, category_slug=None):

    # if request.user.is_authenticated:
    h_products = House_Product.objects.all().filter(is_available=True,id=request.user.id).order_by('id')
    c_products = Car_Product.objects.all().filter(is_available=True,id=request.user.id).order_by('id')



    context = {
        'h_products' : h_products,
        'c_products': c_products,


    }
    return render(request, 'dashboard/myproducts.html', context)
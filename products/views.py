from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import House_Product, Interested_Product, Interested_Car, Interested_Bike, Interested_Furn, \
    Interested_Other
from .models import Car_Product

def Category(request):

    return render(request, 'category.html')

@login_required(login_url='login')
def add_house(request):
    current_user = request.user
    if request.method == "POST":
        house_type = request.POST.get('type')
        furnish = request.POST.get('furnish')
        bedroom = request.POST.get('bedroom')
        bathroom = request.POST.get('bathroom')

        builtup = request.POST.get('builtup')
        capacity = request.POST.get('capacity')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images = request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
        house = House_Product(user=current_user,type=house_type, furnish=furnish, bedroom=bedroom, bathroom=bathroom,
                               builtup=builtup, capacity=capacity, rent=rent, state=state, city=city, location=location,
                               ad_title=ad_title, add_info=add_info, images=images,)
        house.save()
        messages.success(request, 'Your product is kept for rent!')

        # Pass House_Product ID through URL when redirecting
        return redirect('boosthouse', house_id=house.id)

    return render(request, 'add_house.html')






@login_required(login_url='login')
def add_car(request):
    current_user = request.user
    if request.method=="POST":
        brand=request.POST.get('brand')
        fuel=request.POST.get('fuel')
        driven=request.POST.get('driven')
        own=request.POST.get('own')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
        car=Car_Product(user=current_user,brand=brand,fuel=fuel,driven=driven,own=own,
                            rent=rent,ad_title=ad_title,add_info=add_info,images=images,state=state,city=city,location=location)
        car.save()
        messages.success(request, 'Your product is kept for rent!')

        return redirect('boostcar', car_id=car.id)

    return render(request, 'add_car.html')


from django.shortcuts import render, redirect

# Create your views here.
from .models import  Bike_Product

@login_required(login_url='login')
def add_bike(request):
    current_user = request.user
    if request.method=="POST":
        brand=request.POST.get('brand')
        driven=request.POST.get('driven')
        own=request.POST.get('own')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
        bike=Bike_Product(user=current_user,brand=brand,driven=driven,own=own,
                            rent=rent,ad_title=ad_title,add_info=add_info,images=images,state=state,city=city,location=location)
        bike.save()
        messages.success(request, 'Your product is kept for rent!')

        return redirect('boostbike', bike_id=bike.id)
    return render(request, 'add_bike.html')

from .models import Furn_Product


@login_required(login_url='login')
def add_furn(request):
    current_user = request.user
    if request.method=="POST":
        type = request.POST.get('type')

        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
        furniture=Furn_Product(user=current_user,type=type,rent=rent,ad_title=ad_title,add_info=add_info,images=images,
                               state=state,city=city,location=location)
        furniture.save()
        messages.success(request, 'Your product is kept for rent!')

        return redirect('boostfurn', furn_id=furniture.id)
    return render(request, 'add_furn.html')


from .models import Other_Product


@login_required(login_url='login')
def add_other(request):
    current_user = request.user
    if request.method=="POST":
        type = request.POST.get('type')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')
        other=Other_Product(user=current_user,type=type,rent=rent,ad_title=ad_title,add_info=add_info,images=images,
                            state=state,city=city,location=location)
        other.save()
        messages.success(request, 'Your product is kept for rent!')

        return redirect('boostother', other_id=other.id)
    return render(request, 'add_other.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from .models import Interested_Product

def product_interested(request, pk):
    url = request.META.get('HTTP_REFERER')

    product = get_object_or_404(House_Product, pk=pk)
    Interested_Product.objects.create(user=request.user, h_product=product,interest_status=True)
    send_mail(
            'Your product has been marked as interested',
            f'Your product {product.ad_title} has been marked as interested by {request.user.fname}{request.user.lname}.Redirect to that product  http://127.0.0.1:8000/category/{product.category.slug}/{product.slug}',
            'anyrentplatform@gmail.com',
            [product.user.email],
            fail_silently=False,
        )

    messages.success(request, 'Product marked as interested')
    return redirect(url)


def car_interested(request, pk):
    url = request.META.get('HTTP_REFERER')

    product = get_object_or_404(Car_Product, pk=pk)
    Interested_Car.objects.create(user=request.user, c_product=product,interest_status=True)
    send_mail(
            'Your product has been marked as interested',
            f'Your product {product.ad_title} has been marked as interested by {request.user.fname}{request.user.lname}.Redirect to that product  http://127.0.0.1:8000/category/{product.category.slug}/{product.slug}',
            'anyrentplatform@gmail.com',
            [product.user.email],
            fail_silently=False,
        )

    messages.success(request, 'Product marked as interested')
    return redirect(url)

def bike_interested(request, pk):
    url = request.META.get('HTTP_REFERER')

    product = get_object_or_404(Bike_Product, pk=pk)
    Interested_Bike.objects.create(user=request.user, b_product=product,interest_status=True)
    send_mail(
            'Your product has been marked as interested',
            f'Your product {product.ad_title} has been marked as interested by {request.user.fname}{request.user.lname}.Redirect to that product  http://127.0.0.1:8000/category/{product.category.slug}/{product.slug}',
            'anyrentplatform@gmail.com',
            [product.user.email],
            fail_silently=False,
        )

    messages.success(request, 'Product marked as interested')
    return redirect(url)

def furn_interested(request, pk):
    url = request.META.get('HTTP_REFERER')

    product = get_object_or_404(Furn_Product, pk=pk)
    Interested_Furn.objects.create(user=request.user, f_product=product,interest_status=True)
    send_mail(
            'Your product has been marked as interested',
            f'Your product {product.ad_title} has been marked as interested by {request.user.fname}{request.user.lname}.Redirect to that product  http://127.0.0.1:8000/category/{product.category.slug}/{product.slug}',
            'anyrentplatform@gmail.com',
            [product.user.email],
            fail_silently=False,
        )

    messages.success(request, 'Product marked as interested')
    return redirect(url)

def other_interested(request, pk):
    url = request.META.get('HTTP_REFERER')

    product = get_object_or_404(Other_Product, pk=pk)
    Interested_Other.objects.create(user=request.user, o_product=product,interest_status=True)
    send_mail(
            'Your product has been marked as interested',
            f'Your product {product.ad_title} has been marked as interested by {request.user.fname}{request.user.lname}.Redirect to that product  http://127.0.0.1:8000/category/{product.category.slug}/{product.slug}',
            'anyrentplatform@gmail.com',
            [product.user.email],
            fail_silently=False,
        )

    messages.success(request, 'Product marked as interested')
    return redirect(url)

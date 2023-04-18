from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Account
from anyrent_pjct import settings
from dashboard.form import ProductgalleryForm
from dashboard.models import Productgallery, Payment, OrderPlaced, OrderPlacedCar
from products.models import House_Product, Car_Product, Bike_Product, Furn_Product,Other_Product






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

@login_required(login_url='login')
def editprofile(request):
    # orders = Order.objects.order_by(
    #     '-created_at').filter(user_id=request.user.id, is_ordered=True)
    # order_count = orders.count()
    userprofile=Account.objects.get(id=request.user.id)



    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone_number = request.POST.get("tel")

        userprofile.fname=fname
        userprofile.lname=lname
        userprofile.phone_number=phone_number
        userprofile.save()
        messages.success(request, 'your profile details is updated...!')

        return redirect('myprofile')

    context = {
        # 'orders_count': order_count,
        'userprofile':userprofile,
    }
    return render(request, 'dashboard/dash-edit-profile.html', context)


@login_required(login_url='login')
def changePassword(request):
    if request.method == 'POST':
        current_password=request.POST['current_password']
        new_password=request.POST['new_password']
        confirm_password=request.POST['confirm_password']

        user=Account.objects.get(email__exact=request.user.email)

        if new_password == confirm_password:
            success=user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                # auth.logout(request)
                messages.success(request, 'Password change Successfully')
                return redirect('changePassword')
            else:
                messages.success(request, 'Please enter valid current password')
                return redirect('changePassword')
        else:
            messages.error(request, 'Password does not match')
            return redirect('changePassword')
    return render(request, 'dashboard/change_password.html')



@login_required(login_url='login')
def myproducts(request, category_slug=None):

    # if request.user.is_authenticated:
    c_products = Car_Product.objects.all().filter(user=request.user.id)
    h_products = House_Product.objects.all().filter(user=request.user.id)
    b_products = Bike_Product.objects.all().filter(user=request.user.id)
    f_products = Furn_Product.objects.all().filter(user=request.user.id)
    o_products = Other_Product.objects.all().filter(user=request.user.id)



    context = {
        'h_products' : h_products,
        'c_products': c_products,
        'b_products' : b_products,
        'f_products' : f_products,
        'o_products' : o_products,


    }
    return render(request, 'dashboard/myproducts.html', context)

@login_required(login_url='login')
def managehouse(request,house_id):
    h_product = House_Product.objects.get(id=house_id)
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
        images=request.FILES.get('images')
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')

        h_product.type=type
        h_product.furnish=furnish
        h_product.bedroom=bedroom
        h_product.bathroom=bathroom
        h_product.builtup=builtup
        h_product.capacity=capacity
        h_product.rent=rent
        h_product.ad_title=ad_title
        h_product.add_info=add_info
        h_product.images=images
        h_product.state=state
        h_product.city=city
        h_product.location=location
        h_product.save()
        messages.success(request, 'your product details is updated...!')
        return redirect('myproducts')




    context = {
        'h_product': h_product,

    }
    return render(request, 'dashboard/dash-edit-house-products.html', context)

@login_required(login_url='login')
def managecar(request,car_id):
    c_product = Car_Product.objects.get(id=car_id)
    if request.method=="POST":
        brand = request.POST.get('brand')
        fuel = request.POST.get('fuel')
        driven = request.POST.get('driven')
        own = request.POST.get('own')
        rent = request.POST.get('rent')
        images=request.FILES.get('images')

        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')

        c_product.fuel=fuel
        c_product.brand=brand
        c_product.driven=driven
        c_product.own=own
        c_product.rent=rent
        c_product.images=images

        c_product.ad_title=ad_title
        c_product.add_info=add_info
        c_product.state=state
        c_product.city=city
        c_product.location=location
        c_product.save()
        messages.success(request, 'your product details is updated...!')
        return redirect('myproducts')


    context = {
        'c_product': c_product,

    }
    return render(request, 'dashboard/dash-edit-car-products.html', context)

@login_required(login_url='login')
def managebike(request,bike_id):
    b_product = Bike_Product.objects.get(id=bike_id)
    if request.method=="POST":

        brand = request.POST.get('brand')
        driven = request.POST.get('driven')
        own = request.POST.get('own')
        rent = request.POST.get('rent')
        images = request.FILES.get('images')

        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')

        b_product.brand = brand
        b_product.driven = driven
        b_product.own = own
        b_product.rent = rent
        b_product.images = images

        b_product.ad_title = ad_title
        b_product.add_info = add_info
        b_product.state = state
        b_product.city = city
        b_product.location = location
        b_product.save()
        messages.success(request, 'your product details is updated...!')
        return redirect('myproducts')



    context = {
        'b_product': b_product,

    }
    return render(request, 'dashboard/dash-edit-bike-products.html', context)


@login_required(login_url='login')
def managefurniture(request,furniture_id):
    f_product = Furn_Product.objects.get(id=furniture_id)
    if request.method=="POST":
        type = request.POST.get('type')

        rent = request.POST.get('rent')
        images = request.FILES.get('images')

        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')

        f_product.type = type

        f_product.rent = rent
        f_product.images = images

        f_product.ad_title = ad_title
        f_product.add_info = add_info
        f_product.state = state
        f_product.city = city
        f_product.location = location
        f_product.save()
        messages.success(request, 'your product details is updated...!')
        return redirect('myproducts')



    context = {
        'f_product': f_product,

    }
    return render(request, 'dashboard/dash-edit-furniture-products.html', context)

@login_required(login_url='login')
def manageother(request,other_id):
    o_product = Other_Product.objects.get(id=other_id)
    if request.method=="POST":
        type = request.POST.get('type')

        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images = request.FILES['images']
        state = request.POST.get('state')
        city = request.POST.get('city')
        location = request.POST.get('location')

        o_product.type=type
        o_product.rent=rent
        o_product.ad_title=ad_title
        o_product.add_info=add_info
        o_product.images=images
        o_product.state=state
        o_product.city=city
        o_product.location=location
        o_product.save()
        messages.success(request, 'your product details is updated...!')
        return redirect('myproducts')



    context = {
        'o_product': o_product,

    }
    return render(request, 'dashboard/dash-edit-other-products.html', context)

@login_required(login_url='login')
def deletehouse(request,house_id):
    h_product = House_Product.objects.get(id=house_id)
    h_product.delete()

    return redirect('myproducts')


@login_required(login_url='login')
def deletecar(request,car_id):
    c_product = Car_Product.objects.get(id=car_id)
    c_product.delete()

    return redirect('myproducts')

@login_required(login_url='login')
def deletebike(request,bike_id):
    h_product = Bike_Product.objects.get(id=bike_id)
    h_product.delete()

    return redirect('myproducts')

@login_required(login_url='login')
def deletefurn(request,furn_id):
    h_product = Furn_Product.objects.get(id=furn_id)
    h_product.delete()

    return redirect('myproducts')

@login_required(login_url='login')
def deleteother(request,other_id):
    h_product = Other_Product.objects.get(id=other_id)
    h_product.delete()

    return redirect('myproducts')

@login_required(login_url='login')
def archive_house(request,house_id):
    h_product = House_Product.objects.get(id=house_id)
    if h_product.is_available==True:
        h_product.is_available=False
        h_product.save()
    else:
        h_product.is_available = True
        h_product.save()

    return redirect('myproducts')

@login_required(login_url='login')
def archive_car(request,car_id):
    c_product = Car_Product.objects.get(id=car_id)
    if c_product.is_available==True:
        c_product.is_available=False
        c_product.save()
    else:
        c_product.is_available = True
        c_product.save()

    return redirect('myproducts')

@login_required(login_url='login')
def archive_bike(request,bike_id):
    b_product = Bike_Product.objects.get(id=bike_id)
    if b_product.is_available==True:
        b_product.is_available=False
        b_product.save()
    else:
        b_product.is_available = True
        b_product.save()

    return redirect('myproducts')

@login_required(login_url='login')
def archive_furn(request,furn_id):
    f_product = Furn_Product.objects.get(id=furn_id)
    if f_product.is_available==True:
        f_product.is_available=False
        f_product.save()
    else:
        f_product.is_available = True
        f_product.save()

    return redirect('myproducts')

@login_required(login_url='login')
def archive_other(request,other_id):
    o_product = Other_Product.objects.get(id=other_id)
    if o_product.is_available==True:
        o_product.is_available=False
        o_product.save()
    else:
        o_product.is_available = True
        o_product.save()

    return redirect('myproducts')



def add_product_images(request, pk):
    product = get_object_or_404(House_Product, pk=pk)

    if request.method == 'POST':
        form = ProductgalleryForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            productgallery = Productgallery.objects.create(product=product, image=image)
            productgallery.save()
    else:
        form = ProductgalleryForm()

    return render(request, 'dashboard/add_product_images.html', {'form': form, 'product': product})

import razorpay

def Boost_house(request,house_id):
    # house_id=request.GET.get('id')
    print(house_id)
    h_products=House_Product.objects.get(id=house_id)
    total=300
    razoramount = total * 100
    quantity=1

    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))

    data = {
        "amount": total,
        "currency": "INR",
        "receipt": "order_rcptid_11"

    }
    print(data)
    payment_response = client.order.create(data=data)

    order_id = payment_response['id']
    request.session['order_id'] = order_id
    request.session['house_id'] = house_id
    request.session['quantity'] = quantity


    order_status = payment_response['status']
    if order_status == 'created':
        payment = Payment(user=request.user,
                          amount=total,
                          razorpay_order_id=order_id,
                          razorpay_payment_status=order_status)
        payment.save()

    context = {
        'razoramount': razoramount,
        'h_products': h_products,
        'total': total,
        'quantity': quantity,

    }
    return render(request, 'dashboard/boost.html', context)

from django.core.mail import send_mail
from django.conf import settings

def payment_done(request):
    order_id=request.session['order_id']
    house_id = request.session['house_id']
    quantity = request.session['quantity']
    print(quantity)
    print(house_id)
    payment_id = request.GET.get('payment_id')
    h_products=House_Product.objects.get(id=house_id)

    payment=Payment.objects.get(razorpay_order_id = order_id)
    email=payment.user.email


    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    OrderPlaced(user=request.user,product=h_products,quantity=quantity,payment=payment,is_ordered=True).save()
    h_products.payment_status=True
    h_products.save()
    message = f"The advertisment of {h_products.ad_title} is made as featured product" \
              f"You have paid 500 rupees for advertisment boosting"
    send_mail(
        'Advertisement Boosting',
        message,
        'anyrentplatfrom@gmail.com',
        [email],
        fail_silently=False,
    )

    messages.success(request, 'Thank You for boosting...!')
    return redirect('home')

def Boost_car(request,car_id):
    # house_id=request.GET.get('id')

    h_products=Car_Product.objects.get(id=car_id)
    total=300
    razoramount = total * 100
    quantity=1

    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))

    data = {
        "amount": total,
        "currency": "INR",
        "receipt": "order_rcptid_11"

    }
    print(data)
    payment_response = client.order.create(data=data)

    order_id = payment_response['id']
    request.session['order_id'] = order_id
    request.session['car_id'] = car_id
    request.session['quantity'] = quantity


    order_status = payment_response['status']
    if order_status == 'created':
        payment = Payment(user=request.user,
                          amount=total,
                          razorpay_order_id=order_id,
                          razorpay_payment_status=order_status)
        payment.save()

    context = {
        'razoramount': razoramount,
        'h_products': h_products,
        'total': total,
        'quantity': quantity,

    }
    return render(request, 'dashboard/boost_car.html', context)

def payment_done_car(request):
    order_id=request.session['order_id']
    car_id = request.session['car_id']
    quantity = request.session['quantity']
    print(quantity)

    payment_id = request.GET.get('payment_id')
    h_products=Car_Product.objects.get(id=car_id)

    payment=Payment.objects.get(razorpay_order_id = order_id)
    email=payment.user.email


    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    OrderPlacedCar(user=request.user,product=h_products,quantity=quantity,payment=payment,is_ordered=True).save()
    h_products.payment_status=True
    h_products.save()
    message = f"The advertisment of {h_products.ad_title} is made as featured product" \
              f"You have paid 500 rupees for advertisment boosting"
    send_mail(
        'Advertisement Boosting',
        message,
        'anyrentplatfrom@gmail.com',
        [email],
        fail_silently=False,
    )

    return redirect('home')
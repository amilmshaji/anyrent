from django.shortcuts import get_object_or_404, redirect, render
import pandas as pd
import folium
from products.models import Car_Product, House_Product, Bike_Product, Furn_Product, Other_Product, Category
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ReviewForm
# Create your views here.
from .models import ReviewRating, Location


def Home(request):

    return render(request,"index.html")

def shop(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:

        categories = get_object_or_404(Category, slug=category_slug)
        h_products = House_Product.objects.filter(category=categories, is_available=True)
        c_products = Car_Product.objects.filter(category=categories, is_available=True)
        b_products = Bike_Product.objects.filter(category=categories, is_available=True)
        f_products = Furn_Product.objects.filter(category=categories, is_available=True)
        o_products = Other_Product.objects.filter(category=categories, is_available=True)
    else:

        h_products = House_Product.objects.all().filter(is_available=True).order_by('id')
        c_products = Car_Product.objects.all().filter(is_available=True).order_by('id')
        b_products = Bike_Product.objects.all().filter(is_available=True).order_by('id')
        f_products = Furn_Product.objects.all().filter(is_available=True).order_by('id')
        o_products = Other_Product.objects.all().filter(is_available=True).order_by('id')

    context = {
        'h_products' : h_products,
        'c_products': c_products,
        'b_products': b_products,
        'f_products': f_products,
        'o_products': o_products,

        'categories':categories,
        # 'h_products': paged_products,
    }
    return render(request, 'shop.html', context)



def product_detail(request,  category_slug, product_slug):
    if category_slug == "House-and-Appartments":
        single_product = House_Product.objects.get(category__slug=category_slug, slug=product_slug)

    elif category_slug == "Cars":
        single_product = Car_Product.objects.get(category__slug=category_slug, slug=product_slug)

    elif category_slug =="Bikes":
        single_product = Bike_Product.objects.get(category__slug=category_slug, slug=product_slug)

    elif category_slug =="Furniture":
        single_product = Furn_Product.objects.get(category__slug=category_slug, slug=product_slug)

    elif category_slug =="Others":
        single_product = Other_Product.objects.get(category__slug=category_slug, slug=product_slug)


    reviews = ReviewRating.objects.filter(
        product_id=single_product.id, status=True)


    context = {
        'single_product': single_product,
        'reviews': reviews,

    }
    return render(request, 'product-detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            h_products = House_Product.objects.order_by(
                'created_date').filter(Q(ad_title__icontains=keyword) | Q(type__icontains=keyword) | Q(add_info__icontains=keyword))
            c_products = Car_Product.objects.order_by(
                'created_date').filter(Q(ad_title__icontains=keyword) | Q(brand__icontains=keyword) | Q(add_info__icontains=keyword))
            b_products = Bike_Product.objects.order_by(
                'created_date').filter(Q(ad_title__icontains=keyword) | Q(brand__icontains=keyword) | Q(add_info__icontains=keyword))
            f_products = Furn_Product.objects.order_by(
                'created_date').filter(Q(ad_title__icontains=keyword) | Q(type__icontains=keyword) | Q(add_info__icontains=keyword))
            o_products = Other_Product.objects.order_by(
                'created_date').filter(Q(ad_title__icontains=keyword) | Q(type__icontains=keyword) | Q(add_info__icontains=keyword))
            product_count = h_products.count()
    context = {
        'h_products': h_products,
        'c_products': c_products,
        'f_products': f_products,
        'b_products': b_products,
        'o_products': o_products,
        'product_count': product_count,
    }
    return render(request, 'shop.html', context)

def location_search(request):
    if 'location' in request.GET:
        keyword = request.GET['location']
        if keyword:
            h_products = House_Product.objects.order_by(
                'created_date').filter(Q(state__icontains=keyword) | Q(city__icontains=keyword) | Q(location__icontains=keyword))
            c_products = Car_Product.objects.order_by(
                'created_date').filter(Q(state__icontains=keyword) | Q(city__icontains=keyword) | Q(location__icontains=keyword))
            b_products = Bike_Product.objects.order_by(
                'created_date').filter(Q(state__icontains=keyword) | Q(city__icontains=keyword) | Q(location__icontains=keyword))
            f_products = Furn_Product.objects.order_by(
                'created_date').filter(Q(state__icontains=keyword) | Q(city__icontains=keyword) | Q(location__icontains=keyword))
            o_products = Other_Product.objects.order_by(
                'created_date').filter(Q(state__icontains=keyword) | Q(city__icontains=keyword) | Q(location__icontains=keyword))

            product_count = h_products.count()
    context = {
        'h_products': h_products,
        'c_products': c_products,
        'f_products': f_products,
        'b_products': b_products,
        'o_products': o_products,

        'product_count': product_count,
    }
    return render(request, 'shop.html', context)


@login_required(login_url='login')
def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:

            reviews = ReviewRating.objects.get(
                user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you ! Your Review is Updated')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']



                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(
                    request, 'Thank You ! Your Review Has Been Submitted')
                return redirect(url)


def map_view(request):
    locations = Location.objects.all()

    # Create the map
    m = folium.Map(location=[9.939093, 76.270523], zoom_start=8)

    # Add markers to the map
    for location in locations:
        folium.Marker([location.latitude, location.longitude], popup=location.name).add_to(m)

    # Render the map
    m = m._repr_html_()
    return render(request, 'map.html', {'map': m})


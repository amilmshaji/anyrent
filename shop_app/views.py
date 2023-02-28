from django.shortcuts import get_object_or_404, redirect, render
import pandas as pd
import geocoder
from geopy.geocoders import Nominatim

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
    h_products = House_Product.objects.all()
    b_products = Bike_Product.objects.all()
    c_products = Car_Product.objects.all()
    f_products = Furn_Product.objects.all()
    o_products = Other_Product.objects.all()
    # Create the map
    m = folium.Map(location=[9.939093, 76.270523], zoom_start=8) #initial state the map

    geolocator = Nominatim(user_agent="my_app")
    for h_product in h_products:
        location = geolocator.geocode(h_product.location)
        if h_product.images:
            popup_html = f'<img src="{h_product.images.url}" width="200"><br>{h_product.location}<br>{h_product.ad_title} '
        else:
            popup_html = h_product.location
        folium.Marker(
            [location.latitude, location.longitude],
            popup=folium.Popup(popup_html, max_width=300)
            ).add_to(m)


    for b_product in b_products:
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.geocode(b_product.location)
        if b_product.images:
            popup_html = f'<img src="{b_product.images.url}" width="200"><br>{b_product.location}<br>{b_product.ad_title} '
        else:
            popup_html = b_product.location
        folium.Marker(
            [location.latitude, location.longitude],
            popup=folium.Popup(popup_html, max_width=300)
        ).add_to(m)

    for c_product in c_products:
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.geocode(c_product.location)
        if c_product.images:
            popup_html = f'<img src="{c_product.images.url}" width="200"><br>{c_product.location}<br>{c_product.ad_title} '
        else:
            popup_html = c_product.location
        folium.Marker(
            [location.latitude, location.longitude],
            popup=folium.Popup(popup_html, max_width=300)
        ).add_to(m)

    for f_product in f_products:
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.geocode(f_product.location)
        if f_product.images:
            popup_html = f'<img src="{f_product.images.url}" width="200"><br>{f_product.location}<br>{f_product.ad_title} '
        else:
            popup_html = f_product.location
        folium.Marker(
            [location.latitude, location.longitude],
            popup=folium.Popup(popup_html, max_width=300)
        ).add_to(m)

    for o_product in o_products:
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.geocode(o_product.location)
        if o_product.images:
            popup_html = f'<img src="{o_product.images.url}" width="200"><br>{o_product.location}<br>{o_product.ad_title} '
        else:
            popup_html = o_product.location
        folium.Marker(
            [location.latitude, location.longitude],
            popup=folium.Popup(popup_html, max_width=300)
        ).add_to(m)


    # Render the map
    m = m._repr_html_()
    return render(request, 'map.html', {'map': m})












##taking longitiude and latitude from location table
 # locations = Location.objects.all()
# for h_product in h_products:
#     for location in locations:
#         if h_product.location == location.name:
#             if h_product.images:
#                 popup_html = f'<img src="{h_product.images.url}" width="200"><br>{h_product.location}'
#             else:
#                 popup_html = h_product.location
#             folium.Marker(
#                 [location.latitude, location.longitude],
#                 popup=folium.Popup(popup_html, max_width=300)
#             ).add_to(m)
#
# for b_product in b_products:
#     for location in locations:
#         if b_product.location == location.name:
#             if b_product.images:
#                 popup_html = f'<img src="{b_product.images.url}" width="200"><br>{b_product.location}'
#             else:
#                 popup_html = b_product.location
#             folium.Marker(
#                 [location.latitude, location.longitude],
#                 popup=folium.Popup(popup_html, max_width=300)
#             ).add_to(m)

    #
    # # Add markers to the map
    # for location in locations:
    #     if location.images:
    #         popup_html = f'<img src="{location.images.url}" width="200"><br>{location.name}'
    #     else:
    #         popup_html = location.name
    #     folium.Marker(
    #         [location.latitude, location.longitude],
    #         popup=folium.Popup(popup_html, max_width=300)
    #     ).add_to(m)
from django.core.paginator import Paginator
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
# from .models import ReviewRating, Location
from .models import ReviewRating, Location, CarReview, BikeReview, FurnReview, OtherReview


def Home(request):

    h_products = House_Product.objects.all().filter(is_available=True,is_featured=True).order_by('id')
    c_products = Car_Product.objects.all().filter(is_available=True,is_featured=True).order_by('id')
    b_products = Bike_Product.objects.all().filter(is_available=True,is_featured=True).order_by('id')
    f_products = Furn_Product.objects.all().filter(is_available=True,is_featured=True).order_by('id')
    o_products = Other_Product.objects.all().filter(is_available=True,is_featured=True).order_by('id')

    context = {
        'h_products' : h_products,
        'c_products': c_products,
        'b_products': b_products,
        'f_products': f_products,
        'o_products': o_products,
    }

    return render(request,'index.html', context)

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
        # 'products': paged_products,
        # 'product_count': product_count,
    }
    return render(request, 'shop.html', context)



def product_detail(request,  category_slug, product_slug):
    if category_slug == "House-and-Appartments":
        single_product = House_Product.objects.get(category__slug=category_slug, slug=product_slug)
        reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)


    elif category_slug == "Cars":
        single_product = Car_Product.objects.get(category__slug=category_slug, slug=product_slug)
        reviews = CarReview.objects.filter(product_id=single_product.id, status=True)


    elif category_slug =="Bikes":
        single_product = Bike_Product.objects.get(category__slug=category_slug, slug=product_slug)
        reviews = BikeReview.objects.filter(product_id=single_product.id, status=True)


    elif category_slug =="Furniture":
        single_product = Furn_Product.objects.get(category__slug=category_slug, slug=product_slug)
        reviews = FurnReview.objects.filter(product_id=single_product.id, status=True)


    elif category_slug =="Others":
        single_product = Other_Product.objects.get(category__slug=category_slug, slug=product_slug)
        reviews = OtherReview.objects.filter(product_id=single_product.id, status=True)





    context = {
        'single_product': single_product,
        'reviews': reviews,

    }
    return render(request, 'product-detail.html', context)


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

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            h_products = House_Product.objects.order_by(
                'created_date').filter(Q(ad_title__icontains=keyword) | Q(category__category_name__icontains=keyword))
            c_products = Car_Product.objects.order_by(
                'created_date').filter(Q(ad_title__icontains=keyword) | Q(category__category_name__icontains=keyword))
            b_products = Bike_Product.objects.order_by(
                'created_date').filter(Q(ad_title__icontains=keyword) | Q(category__category_name__icontains=keyword))
            f_products = Furn_Product.objects.order_by(
                'created_date').filter(Q(ad_title__icontains=keyword) | Q(category__category_name__icontains=keyword))
            o_products = Other_Product.objects.order_by(
                'created_date').filter(Q(ad_title__icontains=keyword) | Q(category__category_name__icontains=keyword))
            product_count = h_products.count()
    context = {
        'h_products': h_products,
        'c_products': c_products,
        'b_products': b_products,
        'f_products': f_products,
        'o_products': o_products,

        'product_count': product_count,
    }
    return render(request, 'shop.html', context)
from django.http import JsonResponse
from django.db.models import Q

def search_suggestions(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = House_Product.objects.filter(Q(ad_title__icontains=keyword) | Q(category__category_name__icontains=keyword))
            c_products = Car_Product.objects.filter(Q(ad_title__icontains=keyword) | Q(category__category_name__icontains=keyword))
            b_products = Bike_Product.objects.filter(Q(ad_title__icontains=keyword) | Q(category__category_name__icontains=keyword))
            f_products = Furn_Product.objects.filter(Q(ad_title__icontains=keyword) | Q(category__category_name__icontains=keyword))
            o_products = Other_Product.objects.filter(Q(ad_title__icontains=keyword) | Q(category__category_name__icontains=keyword))

            suggestions = []
            for product in products:
                suggestion = {
                    'name': product.ad_title,
                    'url': product.get_url()
                }
                suggestions.append(suggestion)
            for c_product in c_products:
                suggestion = {
                    'name': c_product.ad_title,
                    'url': c_product.get_url()
                }
                suggestions.append(suggestion)
            for b_product in b_products:
                suggestion = {
                    'name': b_product.ad_title,
                    'url': b_product.get_url()
                }
                suggestions.append(suggestion)
            for f_product in f_products:
                suggestion = {
                    'name': f_product.ad_title,
                    'url': f_product.get_url()
                }
                suggestions.append(suggestion)
            for o_product in o_products:
                suggestion = {
                    'name': o_product.ad_title,
                    'url': o_product.get_url()
                }
                suggestions.append(suggestion)
            return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)

@login_required(login_url='login')
def House_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        image = request.FILES['images']
        try:
            reviews = ReviewRating.objects.get(
                user__id=request.user.id, product__id=product_id)
            reviews.review = review
            review.rating = rating
            review.image = image
            review.save()
            messages.success(request, 'Thank you ! Your Review is Updated')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            ip = request.META.get('REMOTE_ADDR')
            reviews=ReviewRating(review=review,rating=rating,image=image,ip=ip,product_id=product_id,user_id=request.user.id)
            reviews.save()
            messages.success(
                request, 'Thank You ! Your Review Has Been Submitted')
            return redirect(url)

@login_required(login_url='login')
def Car_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        image = request.FILES['images']
        try:
            reviews = CarReview.objects.get(
                user__id=request.user.id, product__id=product_id)
            reviews.review = review
            review.rating = rating
            review.image = image
            review.save()
            messages.success(request, 'Thank you ! Your Review is Updated')
            return redirect(url)
        except CarReview.DoesNotExist:
            ip = request.META.get('REMOTE_ADDR')
            reviews = CarReview(review=review, rating=rating, image=image, ip=ip, product_id=product_id,
                                user_id=request.user.id)
            reviews.save()
            messages.success(
                request, 'Thank You ! Your Review Has Been Submitted')
            return redirect(url)

@login_required(login_url='login')
def Bike_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        image = request.FILES['images']
        try:
            reviews = BikeReview.objects.get(
                user__id=request.user.id, product__id=product_id)
            reviews.review = review
            review.rating = rating
            review.image = image
            review.save()
            messages.success(request, 'Thank you ! Your Review is Updated')
            return redirect(url)
        except BikeReview.DoesNotExist:
            ip = request.META.get('REMOTE_ADDR')
            reviews = BikeReview(review=review, rating=rating, image=image, ip=ip, product_id=product_id,
                                user_id=request.user.id)
            reviews.save()
            messages.success(
                request, 'Thank You ! Your Review Has Been Submitted')
            return redirect(url)

@login_required(login_url='login')
def Furn_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        image = request.FILES['images']
        try:
            reviews = FurnReview.objects.get(
                user__id=request.user.id, product__id=product_id)
            reviews.review = review
            review.rating = rating
            review.image = image
            review.save()
            messages.success(request, 'Thank you ! Your Review is Updated')
            return redirect(url)
        except FurnReview.DoesNotExist:
            ip = request.META.get('REMOTE_ADDR')
            reviews = FurnReview(review=review, rating=rating, image=image, ip=ip, product_id=product_id,
                                user_id=request.user.id)
            reviews.save()
            messages.success(
                request, 'Thank You ! Your Review Has Been Submitted')
            return redirect(url)

@login_required(login_url='login')
def Other_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        image = request.FILES['images']
        try:
            reviews = OtherReview.objects.get(
                user__id=request.user.id, product__id=product_id)
            reviews.review = review
            review.rating = rating
            review.image = image
            review.save()
            messages.success(request, 'Thank you ! Your Review is Updated')
            return redirect(url)
        except OtherReview.DoesNotExist:
            ip = request.META.get('REMOTE_ADDR')
            reviews = OtherReview(review=review, rating=rating, image=image, ip=ip, product_id=product_id,
                                user_id=request.user.id)
            reviews.save()
            messages.success(
                request, 'Thank You ! Your Review Has Been Submitted')
            return redirect(url)



def map_view(request):
    h_products = House_Product.objects.all()
    b_products = Bike_Product.objects.all()
    c_products = Car_Product.objects.all()
    f_products = Furn_Product.objects.all()
    o_products = Other_Product.objects.all()
    locs=Location.objects.all()
    # Create the map
    m = folium.Map(location=[9.939093, 76.270523], zoom_start=8) #initial state the map

    geolocator = Nominatim(user_agent="my_app")
    for h_product in h_products:
        results = Location.objects.filter(name=h_product.location)
        if results.exists():
            for result in results:
                if h_product.location == result.name:
                    if h_product.images:
                        popup_html = f'<a href="{h_product.get_url()}" target="_blank"><img src="{h_product.images.url}" width="200"><br>{h_product.ad_title}<br>{h_product.location}</a>'
                    else:
                        popup_html = f'<a href="{h_product.get_url()}" target="_blank">{h_product.location}</a>'

                    # Check if there are multiple house products with the same location
                    same_loc = House_Product.objects.filter(location=h_product.location).exclude(id=h_product.id)
                    if same_loc.exists():
                        # Offset the latitude and longitude by 0.004 degrees
                        result.latitude += 0.004
                        result.longitude += 0.004
                    folium.Marker(
                        [result.latitude, result.longitude],
                        popup=folium.Popup(popup_html, max_width=300)
                    ).add_to(m)

        else:
            geoloc = geolocator.geocode(h_product.location)
            l = Location(name=h_product.location, latitude=geoloc.latitude, longitude=geoloc.longitude)
            l.save()
            if h_product.images:
                popup_html = f'<a href="{h_product.get_url()}" target="_blank"><img src="{h_product.images.url}" width="200"><br>{h_product.ad_title}<br>{h_product.location}</a>'
            else:
                popup_html = f'<a href="{h_product.get_url()}" target="_blank">{h_product.location}</a>'
            folium.Marker(
                [geoloc.latitude, geoloc.longitude],
                popup=folium.Popup(popup_html, max_width=300)
            ).add_to(m)

    for c_product in c_products:
        results = Location.objects.filter(name=c_product.location)
        if results.exists():
            for result in results:
                if c_product.location == result.name:
                    if c_product.images:
                        popup_html = f'<a href="{c_product.get_url()}" target="_blank"><img src="{c_product.images.url}" width="200"><br>{c_product.ad_title}<br>{c_product.location}</a>'
                    else:
                        popup_html = c_product.location

                    # Check if there are multiple house products with the same location
                    same_loc = Car_Product.objects.filter(location=c_product.location).exclude(id=c_product.id)
                    if same_loc.exists():
                        # Offset the latitude and longitude by 0.004 degrees
                        result.latitude += 0.004
                        result.longitude += 0.004
                    folium.Marker(
                        [result.latitude, result.longitude],
                        popup=folium.Popup(popup_html, max_width=300)
                    ).add_to(m)

        else:
            geoloc = geolocator.geocode(c_product.location)
            l = Location(name=c_product.location, latitude=geoloc.latitude, longitude=geoloc.longitude)
            l.save()
            if c_product.images:
                popup_html = f'<a href="{c_product.get_url()}" target="_blank"><img src="{c_product.images.url}" width="200"><br>{c_product.ad_title}<br>{c_product.location}</a>'
            else:
                popup_html = f'<a href="{c_product.get_url()}" target="_blank">{c_product.location}</a>'
            folium.Marker(
                [geoloc.latitude, geoloc.longitude],
                popup=folium.Popup(popup_html, max_width=300)
            ).add_to(m)

    for b_product in b_products:
        results = Location.objects.filter(name=b_product.location)
        if results.exists():
            for result in results:
                if b_product.location == result.name:
                    if b_product.images:
                        popup_html = f'<a href="{b_product.get_url()}" target="_blank"><img src="{b_product.images.url}" width="200"><br>{b_product.ad_title}<br>{b_product.location}</a>'
                    else:
                        popup_html = f'<a href="{b_product.get_url()}" target="_blank">{b_product.location}</a>'

                    # Check if there are multiple house products with the same location
                    same_loc = Bike_Product.objects.filter(location=b_product.location).exclude(id=b_product.id)
                    if same_loc.exists():
                        # Offset the latitude and longitude by 0.004 degrees
                        result.latitude += 0.004
                        result.longitude += 0.004
                    folium.Marker(
                        [result.latitude, result.longitude],
                        popup=folium.Popup(popup_html, max_width=300)
                    ).add_to(m)

        else:
            geoloc = geolocator.geocode(b_product.location)
            l = Location(name=b_product.location, latitude=geoloc.latitude, longitude=geoloc.longitude)
            l.save()
            if b_product.images:
                popup_html = f'<a href="{b_product.get_url()}" target="_blank"><img src="{b_product.images.url}" width="200"><br>{b_product.ad_title}<br>{b_product.location}</a>'
            else:
                popup_html = f'<a href="{b_product.get_url()}" target="_blank">{b_product.location}</a>'
            folium.Marker(
                [geoloc.latitude, geoloc.longitude],
                popup=folium.Popup(popup_html, max_width=300)
            ).add_to(m)

    for f_product in f_products:
        results = Location.objects.filter(name=f_product.location)
        if results.exists():
            for result in results:
                if f_product.location == result.name:
                    if f_product.images:
                        popup_html = f'<a href="{f_product.get_url()}" target="_blank"><img src="{f_product.images.url}" width="200"><br>{f_product.ad_title}<br>{f_product.location}</a>'
                    else:
                        popup_html = f'<a href="{f_product.get_url()}" target="_blank">{f_product.location}<br>{f_product.ad_title}</a>'

                    # Check if there are multiple house products with the same location
                    same_loc = Furn_Product.objects.filter(location=f_product.location).exclude(id=f_product.id)
                    if same_loc.exists():
                        # Offset the latitude and longitude by 0.004 degrees
                        result.latitude += 0.004
                        result.longitude += 0.004
                    folium.Marker(
                        [result.latitude, result.longitude],
                        popup=folium.Popup(popup_html, max_width=300)
                    ).add_to(m)

        else:
            geoloc = geolocator.geocode(f_product.location)
            l = Location(name=f_product.location, latitude=geoloc.latitude, longitude=geoloc.longitude)
            l.save()
            if f_product.images:
                popup_html = f'<a href="{f_product.get_url()}" target="_blank"><img src="{f_product.images.url}" width="200"><br>{f_product.ad_title}<br>{f_product.location}</a>'
            else:
                popup_html = f'<a href="{f_product.get_url()}" target="_blank">{f_product.location}<br>{f_product.ad_title}</a>'
            folium.Marker(
                [geoloc.latitude, geoloc.longitude],
                popup=folium.Popup(popup_html, max_width=300)
            ).add_to(m)

    for o_product in o_products:
        results = Location.objects.filter(name=o_product.location)
        if results.exists():
            for result in results:
                if o_product.location == result.name:
                    if o_product.images:
                        popup_html = f'<a href="{o_product.get_url()}" target="_blank"><img src="{o_product.images.url}" width="200"><br>{o_product.ad_title}<br>{o_product.location}</a>'
                    else:
                        popup_html = f'<a href="{o_product.get_url()}" target="_blank">{o_product.location}<br>{o_product.ad_title}</a>'

                    # Check if there are multiple house products with the same location
                    same_loc = Other_Product.objects.filter(location=o_product.location).exclude(id=o_product.id)
                    if same_loc.exists():
                        # Offset the latitude and longitude by 0.004 degrees
                        result.latitude += 0.004
                        result.longitude += 0.004
                    folium.Marker(
                        [result.latitude, result.longitude],
                        popup=folium.Popup(popup_html, max_width=300)
                    ).add_to(m)

        else:
            geoloc = geolocator.geocode(o_product.location)
            l = Location(name=o_product.location, latitude=geoloc.latitude, longitude=geoloc.longitude)
            l.save()
            if o_product.images:
                popup_html = f'<a href="{o_product.get_url()}" target="_blank"><img src="{o_product.images.url}" width="200"><br>{o_product.ad_title}<br>{o_product.location}</a>'
            else:
                popup_html = f'<a href="{o_product.get_url()}" target="_blank">{o_product.location}<br>{o_product.ad_title}</a>'
            folium.Marker(
                [geoloc.latitude, geoloc.longitude],
                popup=folium.Popup(popup_html, max_width=300)
            ).add_to(m)


    # Render the map
    m = m._repr_html_()
    return render(request, 'map.html', {'map': m})



def prod_map_view(request,location):
    h_products = House_Product.objects.all()
    b_products = Bike_Product.objects.all()
    c_products = Car_Product.objects.all()
    f_products = Furn_Product.objects.all()
    o_products = Other_Product.objects.all()
    locs=Location.objects.all()
    r = Location.objects.filter(name=location)
    if r.exists():

        res = Location.objects.get(name=location)
        m = folium.Map(location=[res.latitude, res.longitude], zoom_start=15)  # initial state the map
    else:
        m = folium.Map(location=[9.939093, 76.270523], zoom_start=8)  # initial state the map

    # Create the map

    geolocator = Nominatim(user_agent="my_app")
    for h_product in h_products:
        results = Location.objects.filter(name=h_product.location)
        if results.exists():
            for result in results:
                if h_product.location == result.name:
                    if h_product.images:
                        popup_html = f'<a href="{h_product.get_url()}" target="_blank"><img src="{h_product.images.url}" width="200"><br>{h_product.location}</a>'
                    else:
                        popup_html = f'<a href="{h_product.get_url()}" target="_blank">{h_product.location}</a>'

                    # Check if there are multiple house products with the same location
                    same_loc = House_Product.objects.filter(location=h_product.location).exclude(id=h_product.id)
                    if same_loc.exists():
                        # Offset the latitude and longitude by 0.004 degrees
                        result.latitude += 0.004
                        result.longitude += 0.004
                    folium.Marker(
                        [result.latitude, result.longitude],
                        popup=folium.Popup(popup_html, max_width=300)
                    ).add_to(m)

        else:
            geoloc = geolocator.geocode(h_product.location)
            l = Location(name=h_product.location, latitude=geoloc.latitude, longitude=geoloc.longitude)
            l.save()
            if h_product.images:
                popup_html = f'<a href="{h_product.get_url()}" target="_blank"><img src="{h_product.images.url}" width="200"><br>{h_product.location}</a>'
            else:
                popup_html = f'<a href="{h_product.get_url()}" target="_blank">{h_product.location}</a>'
            folium.Marker(
                [geoloc.latitude, geoloc.longitude],
                popup=folium.Popup(popup_html, max_width=300)
            ).add_to(m)

    for c_product in c_products:
        results = Location.objects.filter(name=c_product.location)
        if results.exists():
            for result in results:
                if c_product.location == result.name:
                    if c_product.images:
                        popup_html = f'<a href="{c_product.get_url()}" target="_blank"><img src="{c_product.images.url}" width="200"><br>{c_product.location}</a>'
                    else:
                        popup_html = c_product.location

                    # Check if there are multiple house products with the same location
                    same_loc = Car_Product.objects.filter(location=c_product.location).exclude(id=c_product.id)
                    if same_loc.exists():
                        # Offset the latitude and longitude by 0.004 degrees
                        result.latitude += 0.004
                        result.longitude += 0.004
                    folium.Marker(
                        [result.latitude, result.longitude],
                        popup=folium.Popup(popup_html, max_width=300)
                    ).add_to(m)

        else:
            geoloc = geolocator.geocode(c_product.location)
            l = Location(name=c_product.location, latitude=geoloc.latitude, longitude=geoloc.longitude)
            l.save()
            if c_product.images:
                popup_html = f'<a href="{c_product.get_url()}" target="_blank"><img src="{c_product.images.url}" width="200"><br>{c_product.location}</a>'
            else:
                popup_html = f'<a href="{c_product.get_url()}" target="_blank">{c_product.location}</a>'
            folium.Marker(
                [geoloc.latitude, geoloc.longitude],
                popup=folium.Popup(popup_html, max_width=300)
            ).add_to(m)

    for b_product in b_products:
        results = Location.objects.filter(name=b_product.location)
        if results.exists():
            for result in results:
                if b_product.location == result.name:
                    if b_product.images:
                        popup_html = f'<a href="{b_product.get_url()}" target="_blank"><img src="{b_product.images.url}" width="200"><br>{b_product.location}</a>'
                    else:
                        popup_html = f'<a href="{b_product.get_url()}" target="_blank">{b_product.location}</a>'

                    # Check if there are multiple house products with the same location
                    same_loc = Bike_Product.objects.filter(location=b_product.location).exclude(id=b_product.id)
                    if same_loc.exists():
                        # Offset the latitude and longitude by 0.004 degrees
                        result.latitude += 0.004
                        result.longitude += 0.004
                    folium.Marker(
                        [result.latitude, result.longitude],
                        popup=folium.Popup(popup_html, max_width=300)
                    ).add_to(m)

        else:
            geoloc = geolocator.geocode(b_product.location)
            l = Location(name=b_product.location, latitude=geoloc.latitude, longitude=geoloc.longitude)
            l.save()
            if b_product.images:
                popup_html = f'<a href="{b_product.get_url()}" target="_blank"><img src="{b_product.images.url}" width="200"><br>{b_product.location}</a>'
            else:
                popup_html = f'<a href="{b_product.get_url()}" target="_blank">{b_product.location}</a>'
            folium.Marker(
                [geoloc.latitude, geoloc.longitude],
                popup=folium.Popup(popup_html, max_width=300)
            ).add_to(m)

    for f_product in f_products:
        results = Location.objects.filter(name=f_product.location)
        if results.exists():
            for result in results:
                if f_product.location == result.name:
                    if f_product.images:
                        popup_html = f'<a href="{f_product.get_url()}" target="_blank"><img src="{f_product.images.url}" width="200"><br>{f_product.location}</a>'
                    else:
                        popup_html = f'<a href="{f_product.get_url()}" target="_blank">{f_product.location}</a>'

                    # Check if there are multiple house products with the same location
                    same_loc = Furn_Product.objects.filter(location=f_product.location).exclude(id=f_product.id)
                    if same_loc.exists():
                        # Offset the latitude and longitude by 0.004 degrees
                        result.latitude += 0.004
                        result.longitude += 0.004
                    folium.Marker(
                        [result.latitude, result.longitude],
                        popup=folium.Popup(popup_html, max_width=300)
                    ).add_to(m)

        else:
            geoloc = geolocator.geocode(f_product.location)
            l = Location(name=f_product.location, latitude=geoloc.latitude, longitude=geoloc.longitude)
            l.save()
            if f_product.images:
                popup_html = f'<img src="{f_product.images.url}" width="200"><br>{f_product.location}<br>{f_product.ad_title} '
            else:
                popup_html = f'<a href="{f_product.get_url()}" target="_blank">{f_product.location}</a>'
            folium.Marker(
                [geoloc.latitude, geoloc.longitude],
                popup=folium.Popup(popup_html, max_width=300)
            ).add_to(m)

    for o_product in o_products:
        results = Location.objects.filter(name=o_product.location)
        if results.exists():
            for result in results:
                if o_product.location == result.name:
                    if o_product.images:
                        popup_html = f'<a href="{o_product.get_url()}" target="_blank"><img src="{o_product.images.url}" width="200"><br>{o_product.location}</a>'
                    else:
                        popup_html = f'<a href="{o_product.get_url()}" target="_blank">{o_product.location}</a>'

                    # Check if there are multiple house products with the same location
                    same_loc = Other_Product.objects.filter(location=o_product.location).exclude(id=o_product.id)
                    if same_loc.exists():
                        # Offset the latitude and longitude by 0.004 degrees
                        result.latitude += 0.004
                        result.longitude += 0.004
                    folium.Marker(
                        [result.latitude, result.longitude],
                        popup=folium.Popup(popup_html, max_width=300)
                    ).add_to(m)

        else:
            geoloc = geolocator.geocode(o_product.location)
            l = Location(name=o_product.location, latitude=geoloc.latitude, longitude=geoloc.longitude)
            l.save()
            if o_product.images:
                popup_html = f'<a href="{o_product.get_url()}" target="_blank"><img src="{o_product.images.url}" width="200"><br>{o_product.location}</a>'
            else:
                popup_html = f'<a href="{o_product.get_url()}" target="_blank">{o_product.location}</a>'
            folium.Marker(
                [geoloc.latitude, geoloc.longitude],
                popup=folium.Popup(popup_html, max_width=300)
            ).add_to(m)


    # Render the map
    m = m._repr_html_()
    return render(request, 'map.html', {'map': m})
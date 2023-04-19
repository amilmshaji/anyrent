from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.Category, name='category'),
    path('add_house/', views.add_house, name='add_house'),
    path('add_car/', views.add_car, name='add_car'),
    path('add_bike/', views.add_bike, name='add_bike'),
    path('add_furn/', views.add_furn, name='add_furn'),
    path('add_other/', views.add_other, name='add_other'),

    # path('interested/<int:id>/', views.interested, name='interested'),
    path('product/<int:pk>/interested/', views.product_interested, name='product_interested'),
    path('product_car/<int:pk>/interested/', views.car_interested, name='car_interested'),
    path('product_bike/<int:pk>/interested/', views.bike_interested, name='bike_interested'),
    path('product_furn/<int:pk>/interested/', views.furn_interested, name='furn_interested'),
    path('product_other/<int:pk>/interested/', views.other_interested, name='other_interested'),

]
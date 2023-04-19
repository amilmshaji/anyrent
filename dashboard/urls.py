from django.urls import path
from . import views

urlpatterns = [
    path('myprofile/', views.dashboard, name='myprofile'),
    path('editprofile/', views.editprofile, name='edit_profile'),
    path('changePassword/', views.changePassword, name='changePassword'),

    path('myproducts/', views.myproducts, name='myproducts'),
    path('managehouse/<int:house_id>/', views.managehouse, name='managehouse'),
    path('managecar/<int:car_id>/', views.managecar, name='managecar'),
    path('managebike/<int:bike_id>/', views.managebike, name='managebike'),
    path('managefurniture/<int:furniture_id>/', views.managefurniture, name='managefurniture'),
    path('manageother/<int:other_id>/', views.manageother, name='manageother'),

    #url for deleting each products
    path('deletehouse/<int:house_id>/', views.deletehouse, name='deletehouse'),
    path('deletecar/<int:car_id>/', views.deletecar, name='deletecar'),
    path('deletebike/<int:bike_id>/', views.deletebike, name='deletebike'),
    path('deletefurn/<int:furn_id>/', views.deletefurn, name='deletefurn'),
    path('deleteother/<int:other_id>/', views.deleteother, name='deleteother'),

    #url for archiving the products
    path('archivehouse/<int:house_id>/', views.archive_house, name='archive_house'),
    path('archivecar/<int:car_id>/', views.archive_car, name='archive_car'),
    path('archivebike/<int:bike_id>/', views.archive_bike, name='archive_bike'),
    path('archivefurn/<int:furn_id>/', views.archive_furn, name='archive_furn'),
    path('archiveother/<int:other_id>/', views.archive_other, name='archive_other'),
    path('add_product_images/<int:pk>/', views.add_product_images, name='add_product_images'),

    #url for product booosting
    path('boosthouse/<slug:house_id>/', views.Boost_house, name='boosthouse'),
    path('boostcar/<slug:car_id>/', views.Boost_car, name='boostcar'),
    path('boostbike/<slug:bike_id>/', views.Boost_Bike, name='boostbike'),
    path('boostfurn/<slug:furn_id>/', views.Boost_Furn, name='boostfurn'),
    path('boostother/<slug:other_id>/', views.Boost_Other, name='boostother'),

    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('paymentdonecar/', views.payment_done_car, name='paymentdonecar'),
    path('paymentdonebike/', views.payment_done_bike, name='paymentdonecar'),
    path('paymentdonefurn/', views.payment_done_furn, name='paymentdonefurn'),
    path('paymentdoneother/', views.payment_done_other, name='paymentdoneother'),

]
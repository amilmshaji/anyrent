
from django.db import models
from django.urls.base import reverse
from django.db.models.signals import pre_save
from django.utils.html import mark_safe


from accounts.models import Account
from anyrent_pjct.utils import unique_slug_generator


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name  #shows the name


    @property
    def thumbnail_preview5(self):    #funtion to show image preview in admin panel side
        if self.cat_image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.cat_image.url))
        return ""


#house product table
class House_Product(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,editable=False)
    ad_title = models.CharField(max_length=200, unique=True,editable=False)
    slug = models.SlugField(max_length=200, unique=True,editable=False)
    add_info = models.TextField(max_length=500, blank=True,editable=False)
    rent = models.IntegerField(editable=False)
    bedroom = models.IntegerField(editable=False)
    bathroom = models.IntegerField(editable=False)
    builtup= models.IntegerField(editable=False)
    capacity= models.IntegerField(editable=False)
    type = models.CharField(max_length=200,blank=True,editable=False)
    furnish = models.CharField(max_length=200,blank=True,editable=False)
    location = models.CharField(max_length=200,blank=True,null=True,editable=False)
    city = models.CharField(max_length=200,blank=True,null=True,editable=False)
    state = models.CharField(max_length=200,blank=True,null=True,editable=False)
    images = models.ImageField(upload_to='photos/house',editable=False,null=True)
    payment_status=models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1,editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):    #function for product detail page
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def get_urll(self):
        return reverse('products_by_category', args=[self.category.slug])

    def __str__(self):
        return self.ad_title

    @property
    def thumbnail_preview(self):    #funtion to show image preview in admin panel side
        if self.images:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.images.url))
        return ""



def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=House_Product)



class Car_Product(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,editable=False)
    ad_title = models.CharField(max_length=200, unique=True,editable=False)
    slug = models.SlugField(max_length=200, unique=True,editable=False )
    add_info = models.TextField(max_length=500, blank=True,editable=False )
    rent = models.IntegerField(editable=False)
    brand = models.CharField(max_length=200,blank=True,editable=False)
    driven = models.IntegerField(editable=False )
    own = models.CharField(max_length=200,blank=True,editable=False)
    fuel = models.CharField(max_length=200,blank=True,editable=False)
    location = models.CharField(max_length=200,blank=True,null=True,editable=False)
    city = models.CharField(max_length=200,blank=True,null=True,editable=False)
    state = models.CharField(max_length=200,blank=True,null=True,editable=False)
    images = models.ImageField(upload_to='photos/house',editable=False )
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    payment_status=models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=2,editable=False )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.ad_title


    @property
    def thumbnail_preview1(self):    #funtion to show image preview in admin panel side
        if self.images:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.images.url))
        return ""

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Car_Product)


class Bike_Product(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,editable=False)
    ad_title = models.CharField(max_length=200, unique=True,null=True,editable=False)
    slug = models.SlugField(max_length=200, unique=True,editable=False,)
    add_info = models.TextField(max_length=500, blank=True,null=True,editable=False)
    rent = models.IntegerField(null=True,editable=False)
    brand = models.CharField(max_length=200,blank=True,null=True,editable=False)
    driven = models.IntegerField(null=True,editable=False)
    own = models.CharField(max_length=200,blank=True,null=True,editable=False)
    images = models.ImageField(upload_to='photos/house',null=True,editable=False)
    location = models.CharField(max_length=200,blank=True,null=True,editable=False)
    city = models.CharField(max_length=200,blank=True,null=True,editable=False)
    state = models.CharField(max_length=200,blank=True,null=True,editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=3,editable=False,null=True)

    is_available = models.BooleanField(default=True)
    payment_status=models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.ad_title

    @property
    def thumbnail_preview2(self):    #funtion to show image preview in admin panel side
        if self.images:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.images.url))
        return ""


def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Bike_Product)


class Furn_Product(models.Model):      #Furniture table product adding table
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,editable=False)
    ad_title = models.CharField(max_length=200, unique=True,editable=False)
    slug = models.SlugField(max_length=200, unique=True,editable=False)
    add_info = models.TextField(max_length=500, blank=True,editable=False)
    rent = models.IntegerField(editable=False)
    images = models.ImageField(upload_to='photos/house',editable=False)
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    payment_status=models.BooleanField(default=False)

    type = models.CharField(max_length=200,blank=True,editable=False)
    location = models.CharField(max_length=200,blank=True,null=True,editable=False)
    city = models.CharField(max_length=200,blank=True,null=True,editable=False)
    state = models.CharField(max_length=200,blank=True,null=True,editable=False)


    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=4,editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.ad_title

    @property
    def thumbnail_preview3(self):    #funtion to show image preview in admin panel side
        if self.images:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.images.url))
        return ""

def slug_generator(sender,instance,*args,**kwargs):   #To make slug in the table when vendor add products
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Furn_Product)



class Other_Product(models.Model):                #Other table product adding table
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,editable=False)
    ad_title = models.CharField(max_length=200, unique=True, editable=False)
    slug = models.SlugField(max_length=200, unique=True,editable=False)
    add_info = models.TextField(max_length=500, blank=True,editable=False)
    rent = models.IntegerField(editable=False)
    images = models.ImageField(upload_to='photos/house',editable=False)
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    payment_status=models.BooleanField(default=False)

    type = models.CharField(max_length=200,blank=True,editable=False)
    location = models.CharField(max_length=200,blank=True,null=True,editable=False)
    city = models.CharField(max_length=200,blank=True,null=True,editable=False)
    state = models.CharField(max_length=200,blank=True,null=True,editable=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=5,editable=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.ad_title

    @property
    def thumbnail_preview4(self):    #funtion to show image preview in admin panel side
        if self.images:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.images.url))
        return ""

def slug_generator(sender,instance,*args,**kwargs):   #To make slug in the table when vendor add products
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Other_Product)





class Interested_Product(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,editable=False)
    h_product=models.ForeignKey(House_Product, on_delete=models.CASCADE, null=True,editable=False)
    interest_status=models.BooleanField(default=False)

class Interested_Car(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,editable=False)
    c_product=models.ForeignKey(Car_Product, on_delete=models.CASCADE, null=True,editable=False)
    interest_status=models.BooleanField(default=False)

class Interested_Bike(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,editable=False)
    b_product=models.ForeignKey(Bike_Product, on_delete=models.CASCADE, null=True,editable=False)
    interest_status=models.BooleanField(default=False)

class Interested_Furn(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,editable=False)
    f_product=models.ForeignKey(Furn_Product, on_delete=models.CASCADE, null=True,editable=False)
    interest_status=models.BooleanField(default=False)

class Interested_Other(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,editable=False)
    o_product=models.ForeignKey(Other_Product, on_delete=models.CASCADE, null=True,editable=False)
    interest_status=models.BooleanField(default=False)


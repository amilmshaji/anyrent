from django.contrib import admin
from .models import Account

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    exclude =('password','Groups')

admin.site.register(Account,UserAdmin)

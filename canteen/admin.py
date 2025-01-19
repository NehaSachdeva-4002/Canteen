from django.contrib import admin
from .models import canteen, Order

# Register your models here.
class canteenAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    
admin.site.register(canteen, canteenAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'created_at')
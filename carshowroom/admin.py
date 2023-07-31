from django.contrib import admin
from .models import *


# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display=("street", "city", "state", "zipcode")
admin.site.register(Address, AddressAdmin)


class ShowRoomAdmin(admin.ModelAdmin):
    list_display=("name", "location", "address")
admin.site.register(ShowRoom, ShowRoomAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display=("name", "designation", "showroom")
admin.site.register(Staff, StaffAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display=("name","showroom")
admin.site.register(Brand, BrandAdmin)


class ModelAdmin(admin.ModelAdmin):
    list_display=("name", "brand", "showroom")
admin.site.register(Model, ModelAdmin)


class EngineAdmin(admin.ModelAdmin):
    list_display=("name", "model")
admin.site.register(Engine, EngineAdmin)


class FeatureAdmin(admin.ModelAdmin):
    list_display=("name",)
admin.site.register(Feature, FeatureAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display=("VIN","model", "price", "year", "pic","showroom_purchased" )
admin.site.register(Car, CarAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display=("name","email" )
admin.site.register(Customer, CustomerAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display=("customer","car","purchase_date" )
admin.site.register(Purchase, PurchaseAdmin)


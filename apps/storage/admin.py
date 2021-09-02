from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class resourceProduct (resources.ModelResource):
    class Meta:
        model = product

class adminProduct(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'description']
    resource_class = resourceProduct

admin.site.register(product, adminProduct)

class resourcePurchase (resources.ModelResource):
    class Meta:
        model = purchase

class adminPurchase(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_purchase']
    list_display = ['pk_purchase', 'date_purchase', 'fk_product']
    resource_class = resourcePurchase

admin.site.register(purchase, adminPurchase)

class resourceClient (resources.ModelResource):
    class Meta:
        model = client

class adminClient(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'apellido', 'telefono']
    resource_class = resourceClient

admin.site.register(client, adminClient)

class resourceSale (resources.ModelResource):
    class Meta:
        model = sale

class adminSale(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_sale']
    list_display = ['pk_sale', 'state', 'fk_client', 'fk_product']
    resource_class = resourceSale

admin.site.register(sale, adminSale)

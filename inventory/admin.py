from django.contrib import admin
from .models import ProductInventory, PosmInventory

admin.site.register(ProductInventory)
admin.site.register(PosmInventory)
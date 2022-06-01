from django.contrib import admin
from clothing_store.models import *

from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Category_Shirt)
class Category_Shirt(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [f.name for f in Category_Shirt._meta.fields]

@admin.register(Plain_Color)
class Plain_Color(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [f.name for f in Plain_Color._meta.fields]

@admin.register(Pattern)
class Pattern(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [f.name for f in Pattern._meta.fields]
    
@admin.register(Product_List)
class Product_List(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [f.name for f in Product_List._meta.fields]
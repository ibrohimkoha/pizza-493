from django.contrib import admin
from .models import (ScrollModel,
 ImageModel,
  DrinksModel,
   PizzaModel,
    FricesModel,
    BurgerModel,
     SaladModel,
     UserModel)
# Register your models here.
@admin.register(ScrollModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discount', 'creat_at']
    ordering = ['-creat_at']

@admin.register(ImageModel)
class ImageFieldAdmin(admin.ModelAdmin):
    list_display = ['id']
    ordering = ['-creat_at']

@admin.register(SaladModel)
class SaladModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','price', 'creat_at']
    search_fields = ['title','price']
    ordering = ['-creat_at']


@admin.register(DrinksModel)
class DrinksModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','price', 'creat_at']
    search_fields = ['title','price']
    ordering = ['-creat_at']

@admin.register(PizzaModel)
class PizzaModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','price', 'creat_at']
    search_fields = ['title','price']
    ordering = ['-creat_at']

@admin.register(FricesModel)
class FricesModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','price', 'creat_at']
    search_fields = ['title','price']
    ordering = ['-creat_at']

@admin.register(BurgerModel)
class BurgerModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','price', 'creat_at']
    search_fields = ['title','price']
    ordering = ['-creat_at']

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email', 'phone', 'date', 'time','message']

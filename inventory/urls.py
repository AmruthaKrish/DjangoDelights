from django.urls import path
from . import views

urlpatterns = [
    path('add_ingredient/', views.add_ingredient, name = 'add_ingredient'),
    path('add_menu_item/', views.add_menu_item, name = 'add_menu_item'),
    path('add_recipe_requirement/', views.add_recipe_requirement, name='add_recipe_requirement'),
    path('record_purchase/', views.record_purchase, name='record_purchase'),
    path('view_inventory/', views.view_inventory, name='view_inventory'),
    path('view_menu/', views.view_menu, name='view_menu'),
    path('view_purchases/', views.view_purchases, name='view_purchases'),
]
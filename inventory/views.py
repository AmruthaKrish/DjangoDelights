from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm, IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("login")
    else:
        form = SignupForm()
    return render(request,'inventory/signup.html', {'form':form}) 


    
def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_inventory')
    else:
        form = IngredientForm()
    return render(request, 'inventory/add_ingredient.html', {'form':form})

def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_menu')
    else:
        form = MenuItemForm()
    return render(request,'inventory/add_menu_item.html',{'form':form})
    
def add_recipe_requirement(request):
    if request.method == 'POST':
        form = RecipeRequirementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_menu')
    else:
        form = RecipeRequirementForm()
    return render(request,'inventory/add_recipe_requirement.html', {'form':form})
        
def record_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit = False)
            purchase.user = request.user
            purchase.save()

            requirements = RecipeRequirement.objects.filter(menu_item=purchase.menu_item)
            for req in requirements:
                ingredient = req.ingredient
                ingredient.quantity_available -= req.quantity_required 
                ingredient.save()
            return redirect('view_purchases')
    else:
        form = PurchaseForm()
    return render(request,'inventory/record_purchase.html',{'form':form})

def view_inventory(request):
    ingredients = Ingredient.objects.all() 
    return render(request, 'inventory/view_inventory.html', {'ingredients': ingredients})

def view_menu(request):
    menu_items = MenuItem.objects.all()
    return render(request,'inventory/view_menu.html',{'menu_items':menu_items})

def view_purchases(request):
    purchases = Purchase.objects.all()
    return render(request, 'inventory/view_purchases.html', {'purchases': purchases})
     

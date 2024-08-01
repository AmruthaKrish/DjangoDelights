from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_default_user():
    return User.objects.get(username='chuchu')

class Ingredient(models.Model):
    name= models.CharField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available= models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places = 2)
    
    def __str__(self):
        return self.name
    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_required = models.PositiveIntegerField()

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)


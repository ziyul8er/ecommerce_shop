from django.db import models
from items.models import Item
    
class CartItem(models.Model):
    item = models.ForeignKey(Item, related_name = "cart_items", on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def get_total_price(self):
        return self.item.price * self.quantity

class Cart(models.Model):
    id = models.AutoField(primary_key = True)
    created_at = models.DateTimeField(auto_now_add = True)
    items = models.ManyToManyField(CartItem)
    
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())
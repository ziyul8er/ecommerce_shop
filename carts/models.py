from django.db import models
from django.urls import reverse
from users.models import User
from items.models import Item

hola = {
    "id":1,
    "userId":1,
    "date":"2020-03-02T00:00:00.000Z",
    "products":[
        {"productId":1,"quantity":4},
        {"productId":2,"quantity":1},
        {"productId":3,"quantity":6}
    ]
}
    
class CartItem(models.Model):
    item = models.ForeignKey(Item, related_name="cart_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def get_total_price(self):
        return self.item.price * self.quantity

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(CartItem)
    
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())
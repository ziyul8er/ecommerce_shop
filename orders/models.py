from django.db import models
from users.models import Address, User
from items.models import Item

class OrderItem(models.Model):
    item = models.ForeignKey(Item, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self) -> str:
        return f"{self.quantity} of {self.item.title}"

    def get_total(self):
        return self.price * self.quantity

class Order(models.Model):
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    address = models.ForeignKey(Address, related_name='order_address', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


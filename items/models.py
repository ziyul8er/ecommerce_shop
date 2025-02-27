from django.db import models
from django.urls import reverse

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.TextField(max_length=250)
    image = models.ImageField(upload_to='items', blank=True, null=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    count = models.IntegerField()
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('items:item_detail', kwargs={'id':self.id, 'slug': self.slug})
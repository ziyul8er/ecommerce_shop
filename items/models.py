from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items', blank=True, null=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    count = models.IntegerField()
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('items:item_detail', kwargs={'id':self.id, 'slug': self.slug})
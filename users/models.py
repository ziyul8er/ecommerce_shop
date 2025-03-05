from django.db import models
from django.urls import reverse

class Address(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    zip_code = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'addresses'
    
    def __str__(self) -> str:
        return self.city


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    address = models.ForeignKey(Address, related_name='users', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.username
    
    def get_absolute_url(self):
        return reverse('users:user', kwargs={'id':self.id})
from django.urls import path
from .views import cart_add, cart_details, cart_remove

app_name = 'carts'

urlpatterns = [
    path('add/<int:item_id>/', cart_add, name='cart_add'),
    path('', cart_details, name='cart_details'),
    path('remove/<int:item_id>/', cart_remove, name='remove_item')
]
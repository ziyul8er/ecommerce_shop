from django.shortcuts import render, get_object_or_404
from .models import Item

def item_list(request):
    items = Item.objects.all()
    
    return render(request, 'items/item/list', {'items':items})

def item_detail(request, id, slug):
    item = get_object_or_404(Item, id=id, slug=slug)
    return render(request, 'items/item/detail', {'item':item})
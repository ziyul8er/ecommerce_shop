from django.shortcuts import render, get_object_or_404
from .models import Item, Category

def item_list(request, category_slug):
    category = None
    items = Item.objects
    categories = Category.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)
    
    return render(request, 'items/item/list', {'category':category, 'items':items, 'categories': categories})

def item_detail(request, id, slug):
    item = get_object_or_404(Item, id=id, slug=slug)
    return render(request, 'items/item/detail', {'item':item})
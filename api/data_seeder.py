import requests
import json
from items.models import Item


url = 'https://fakestoreapi.com/products'
items = requests.get(url).json()

# factory section 🏭

for item in items:
    print(item['rating']['rate'])
    Item.objects.create(
        title= item['title'],
        price= item['price'],
        description = item['description'],
        category = item['category'],
        image = item['image'],
        rate = item['rating']['rate'],
        count = item['rating']['count'],
        slug=item['id']
    )

print('done')
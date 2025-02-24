from ninja import ModelSchema
from items.models import Item

class ItemSchema(ModelSchema):
    class Meta:
        model = Item
        fields = ['id', 'title','price', 'description', 'category', 'image', 'rate', 'count']
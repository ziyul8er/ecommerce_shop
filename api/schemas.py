from ninja import ModelSchema
from .models import Item

class ItemSchema(ModelSchema):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description']
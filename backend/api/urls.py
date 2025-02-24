from ninja import ModelSchema
from .models import Item

class ItemSchema(ModelSchema):
    class Meta:
        model = Item
        model_fields = ['id', 'name', 'description']

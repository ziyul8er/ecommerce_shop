from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<slug:category_slug>/', views.item_list, name='item_list_by_category'),
    path('item/<id:id>/<slug:slug>/', views.item_detail, name='item_detail'),
]
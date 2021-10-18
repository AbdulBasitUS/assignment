from django.urls import path
from .views import (
    pizzaTypeList, 
    pizzaTypeDetail,
    pizzaSizeList, 
    pizzaSizeDetail,
    pizzaToppingList, 
    pizzaToppingDetail,
)

urlpatterns = [
    path('types', pizzaTypeList),
    path('types/<int:typeId>', pizzaTypeDetail),

    path('sizes', pizzaSizeList),
    path('sizes/<int:id>', pizzaSizeDetail),

    path('toppings', pizzaToppingList),
    path('toppings/<int:id>', pizzaToppingDetail),
]
from django.urls import path
from .views import (
    pizzaTypeList, 
    pizzaTypeDetail,
    pizzaSizeList, 
    pizzaSizeDetail,
    pizzaToppingList, 
    pizzaToppingDetail,
    pizzaList, 
    pizzaDetail,
)

urlpatterns = [
    path('types', pizzaTypeList),
    path('types/<int:typeId>', pizzaTypeDetail),

    path('sizes', pizzaSizeList),
    path('sizes/<int:id>', pizzaSizeDetail),

    path('toppings', pizzaToppingList),
    path('toppings/<int:id>', pizzaToppingDetail),

    path('pizzas', pizzaList),
    path('pizzas/<int:id>', pizzaDetail)
]
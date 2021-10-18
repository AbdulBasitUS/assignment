from django.urls import path
from .views import (
    pizzaTypeList, 
    pizzaTypeDetail,
)

urlpatterns = [
    path('types', pizzaTypeList),
    path('types/<int:typeId>', pizzaTypeDetail),
]
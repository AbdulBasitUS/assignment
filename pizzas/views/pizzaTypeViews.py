from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from pizzas.models import PizzaType
from ..serializers import PizzaTypeSerializer


@api_view(['GET', 'POST'])
def pizzaTypeList(request):
    if request.method == 'GET':
        pizzas = PizzaType.objects.all()
        serializer = PizzaTypeSerializer(pizzas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data 
        serializer = PizzaTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def pizzaTypeDetail(request, typeId):
    try:
        pizza_type = PizzaType.objects.get(id=typeId)
    except PizzaType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PizzaTypeSerializer(pizza_type, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = PizzaTypeSerializer(pizza_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pizza_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
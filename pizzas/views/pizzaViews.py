from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from pizzas.models import Pizza
from pizzas.serializers import PizzaSerializer

@api_view(['GET', 'POST'])
def pizzaList(request):
    if request.method == 'GET':
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data 
        serializer = PizzaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def pizzaDetail(request, id):
    try:
        pizza = Pizza.objects.get(id=id)
    except Pizza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PizzaSerializer(pizza, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = PizzaSerializer(pizza, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

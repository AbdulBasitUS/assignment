from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import PizzaSize
from ..serializers import PizzaSizeSerializer

@swagger_auto_schema(method='GET', responses={200: PizzaSizeSerializer(many=True)})
@swagger_auto_schema(methods=['POST'], request_body=PizzaSizeSerializer)
@api_view(['GET', 'POST'])
def pizzaSizeList(request):
    if request.method == 'GET':
        pizzas = PizzaSize.objects.all()
        serializer = PizzaSizeSerializer(pizzas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data 
        serializer = PizzaSizeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['PUT'], request_body=PizzaSizeSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
def pizzaSizeDetail(request, id):
    try:
        pizza_size = PizzaSize.objects.get(id=id)
    except PizzaSize.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PizzaSizeSerializer(pizza_size, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = PizzaSizeSerializer(pizza_size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pizza_size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

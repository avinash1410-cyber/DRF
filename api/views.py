from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from product.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def api_response(request):
    if request.method == 'GET':
        # Handle GET request to retrieve data
        model_data = Product.objects.all().first()
        if model_data is not None:
            serializer = ProductSerializer(model_data)
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)  # OK status
        else:
            return Response({'error': 'No product found'}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'POST':
        # Handle POST request to create or update data
        print(request.data)
        serializer = ProductSerializer(data=request.data)        
        if serializer.is_valid():
            # Save the validated data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Created
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Bad Request

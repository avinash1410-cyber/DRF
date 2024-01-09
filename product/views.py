from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



# class RetrieveProductView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field='pk'



# class CreateProductView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

    # def create(self, request, *args, **kwargs):
    #     print("The data through te request is ")
    #     print(request.data)
        
    #     serializer = self.get_serializer(data=request.data)
    #     print(serializer)


    #     serializer.is_valid(raise_exception=True)
        
    #     # The actual saving to the database happens in the perform_create method
    #     self.perform_create(serializer)
        
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     # This is where the data is saved to the database
    #     print(serializer.validated_data)
    #     name=serializer.validated_data.get('name')
    #     price=serializer.validated_data.get('price')
        
    #     serializer.save(name=price,price=400,description="The descriptionn has been delted for it ")




# class CreateListProductView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# @api_view(['GET', 'POST'])
# def alt_view(request, pk=None):
#     if request.method == "GET":
#         if pk:
#             product_instance = Product.objects.filter(pk=pk).first()
#             if product_instance:
#                 serializer = ProductSerializer(product_instance)
#                 return Response(serializer.data)
#             return Response({"Message": "Product not found"}, status=404)

#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response({"Message": "The data is invalid"}, status=400)






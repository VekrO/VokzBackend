from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Serializer
from .serializer import ProductSerializer

# Model
from .models import Product

class ProductView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        products = Product.objects.filter(user=self.request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCreate(APIView):

    def post(self, request):

        try:

            product = Product.objects.create(
                user=self.request.user,
                name=request.data.get('name'),
                description=request.data.get('description'),
                price=request.data.get('price'),
                quantity=request.data.get('quantity'),
            )

            return Response({'message': 'Produto criado com sucesso!'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Falha na criação do produto!'}, status=status.HTTP_400_BAD_REQUEST)

class ProductUpdate(APIView):

    def patch(self, request):

        product = Product.objects.get(id=request.data.get('id'))
        serializer = ProductSerializer(product, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Você atualizou o produto com sucesso!'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Erro na atualização do produto!', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProductDelete(APIView):

    def delete(self, request):
        id = request.data.get('id')
        try:
            Product.objects.get(id=id).delete()
            return Response({'message': 'Produto excluído com sucesso!'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message': 'Não foi possível excluir o produto!'}, status=status.HTTP_400_BAD_REQUEST)

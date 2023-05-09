from django.shortcuts import render
# from rest_framework import views as api_views
from rest_framework import generics as api_views
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import mixins as api_mixins
from rest_framework import permissions

from django_rest_framework_demos.api.models import Product, Category


class CategoryForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ('id', 'name',)
        fields = '__all__'


class IdAndNameProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name',)


class FullCategorySerializer(serializers.ModelSerializer):
    # product_set = serializers.StringRelatedField(many=True)
    product_set = IdAndNameProductSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class CategoryListView(api_views.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = FullCategorySerializer


class SingleCategoryView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryForProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False)
    category = CategoryForProductSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ManualProductsListView(api_views.views.APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(status=400)


class ProductsListView(api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def list(self, request, *args, **kwargs):
        print(self.request.user)
        return super(ProductsListView, self).list(request, *args, **kwargs)


class SingleProductView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ExampleView(api_views.ListAPIView, api_mixins.DestroyModelMixin):
    pass

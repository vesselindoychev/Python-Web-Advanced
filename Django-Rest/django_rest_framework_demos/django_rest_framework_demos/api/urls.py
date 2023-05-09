from django.urls import path

from django_rest_framework_demos.api.views import ProductsListView, SingleProductView, CategoryListView, \
    SingleCategoryView

urlpatterns = (
    path('products/', ProductsListView.as_view(), name='products list'),
    path('products/<int:pk>/', SingleProductView.as_view(), name='single product'),
    path('categories/', CategoryListView.as_view(), name='category list'),
    path('category/<int:pk>/', SingleCategoryView.as_view(), name='single category'),
)
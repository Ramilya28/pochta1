from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    #path('', views.product_list, name='product_list'),  # Список товаров
    path('', ProductListView.as_view(), name='product_list'),  # Список товаров
    # path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('post/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    #path('product/create/', views.create_product, name='create_product'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    #path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    #path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
]
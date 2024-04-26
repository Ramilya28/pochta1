from django.urls import path
from . import views
from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),  # Список товаров
    # path('product/<int:pk>/', views.product_detail, name='product_detail'),
    # path('product/create/', views.create_product, name='create_product'),
    # path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    # path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
]

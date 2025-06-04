from django.urls import path
from . import views

urlpatterns = [
    # Supplier URLs
    path('', views.SupplierListView.as_view(), name='supplier-list'),
    path('supplier/add/', views.SupplierCreateView.as_view(), name='supplier-create'),
    path('supplier/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier-detail'),
    path('supplier/<int:pk>/edit/', views.SupplierUpdateView.as_view(), name='supplier-update'),
    path('supplier/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier-delete'),

    # Product URLs 
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('product/add/', views.ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),

    # Order URLs
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('order/add/', views.OrderCreateView.as_view(), name='order-add'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),
]

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Supplier, Product, Order
from .forms import SupplierForm, ProductForm, OrderForm

# Create your views here.
# Supplier Views
class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplychain/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'supplychain/supplier_detail.html'
    context_object_name = 'supplier'

class SupplierCreateView(SuccessMessageMixin, CreateView):
    
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplychain/supplier_form.html'
    success_url = reverse_lazy('supplier-list')
    success_message = "Supplier was created successfully"

class SupplierUpdateView(SuccessMessageMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplychain/supplier_form.html'
    success_url = reverse_lazy('supplier-list')
    success_message = "Supplier was updated successfully"

class SupplierDeleteView(SuccessMessageMixin, DeleteView):
    model = Supplier
    template_name = 'supplychain/supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier-list')
    success_message = "Supplier was deleted successfully"

# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'supplychain/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'supplychain/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'supplychain/product_form.html'
    success_url = reverse_lazy('product-list')
    success_message = "Product was created successfully"

class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'supplychain/product_form.html'
    success_url = reverse_lazy('product-list')
    success_message = "Product was updated successfully"

class ProductDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'supplychain/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')
    success_message = "Product was deleted successfully"

# Order Views
class OrderListView(ListView):
    model = Order
    template_name = 'supplychain/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'supplychain/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(SuccessMessageMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'supplychain/order_form.html'
    success_url = reverse_lazy('order-list')
    success_message = "Order was created successfully"

    def form_valid(self, form):
        # Calculate total price before saving
        order = form.save(commit=False)
        order.total_price = order.quantity * order.product.price
        return super().form_valid(form)

class OrderUpdateView(SuccessMessageMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'supplychain/order_form.html'
    success_url = reverse_lazy('order-list')
    success_message = "Order was updated successfully"

class OrderDeleteView(SuccessMessageMixin, DeleteView):
    model = Order
    template_name = 'supplychain/order_confirm_delete.html'
    success_url = reverse_lazy('order-list')
    success_message = "Order was deleted successfully"

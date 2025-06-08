from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Supplier, Product, Order
from .forms import SupplierForm, ProductForm, OrderForm

# Create your views here.
# Supplier Views
class Homeview(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'home.html'

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplychain/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    template_name = 'supplychain/supplier_detail.html'
    context_object_name = 'supplier'

class SupplierCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplychain/supplier_form.html'
    success_url = reverse_lazy('supplier-list')
    success_message = "Supplier was created successfully"

class SupplierUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplychain/supplier_form.html'
    success_url = reverse_lazy('supplier-list')
    success_message = "Supplier was updated successfully"

class SupplierDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Supplier
    template_name = 'supplychain/supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier-list')
    success_message = "Supplier was deleted successfully"

# Product Views
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'supplychain/product_list.html'
    context_object_name = 'products'

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'supplychain/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'supplychain/product_form.html'
    success_url = reverse_lazy('product-list')
    success_message = "Product was created successfully"

class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'supplychain/product_form.html'
    success_url = reverse_lazy('product-list')
    success_message = "Product was updated successfully"

class ProductDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'supplychain/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')
    success_message = "Product was deleted successfully"

# Order Views
class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'supplychain/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'supplychain/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
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

class OrderUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'supplychain/order_form.html'
    success_url = reverse_lazy('order-list')
    success_message = "Order was updated successfully"

class OrderDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Order
    template_name = 'supplychain/order_confirm_delete.html'
    success_url = reverse_lazy('order-list')
    success_message = "Order was deleted successfully"

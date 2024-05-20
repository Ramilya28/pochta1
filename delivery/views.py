
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm

from datetime import datetime

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        current_day_of_week = datetime.now().strftime('%A')
        return render(request, 'product_list.html', {'products': products, 'current_day_of_week': current_day_of_week})


# class ProductListView(View):
#     def get(self, request):
#         latest_products = Product.objects.order_by('-id')[:5]
#         current_day_of_week = datetime.now().strftime('%A')
#         return render(request, 'product_list.html', {'products': latest_products, 'current_day_of_week': current_day_of_week})



class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product_detail.html', {'product': product})


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('product_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit_product.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('product_list')
    

# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.mixins import LoginRequiredMixin

# class ProductDetailView(LoginRequiredMixin, View):
#     login_url = '/login/'  # URL для перенаправления неавторизованных пользователей

#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         return render(request, 'product_detail.html', {'product': product})

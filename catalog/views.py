from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from catalog.models import Product, Category
from django.http import HttpResponse
from django.views import View
from catalog.forms import ProductForm, ProductModeratorForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

from catalog.services import get_product_from_cache, get_products_by_category


class CatalogHomeView(ListView):
    model = Product
    template_name = "catalog/base.html"
    context_object_name = "productS"


class CatalogContactsView(View):
    def get(self, request):
        return render(request, "catalog/contacts.html")

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо,{name}, ваше сообщение получено!")


class CatalogListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "product_list"
    def get_queryset(self):
        return get_product_from_cache()


class CatalogDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:product_list")


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:home")
    permission_required = "catalog.can_unpublish_product"

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied("Нет прав для редактирования продукта")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if self.request.user != product.owner and not self.request.user.has_perm("catalog.can_unpublish_product"):
            raise PermissionDenied("Нет прав для редактирования продукта")
        return product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if self.request.user != product.owner and not self.request.user.has_perm("can_delete_product"):
            raise PermissionDenied("Нет прав для удаления продукта")
        return product

    def handle_no_permission(self):
        return redirect("catalog:category_list")


class ProductsByCategoryView(ListView):
    template_name = 'catalog/products_by_category.html'  # укажи путь к нужному шаблону
    context_object_name = 'products'  # имя переменной, под которым будет передан список в шаблон

    def get_queryset(self):
        category_id = self.kwargs['pk']  # получаем ID категории из URL
        return get_products_by_category(category_id)


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"
    context_object_name = "categories"


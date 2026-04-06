from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from catalog.models import Product
from django.http import HttpResponse
from django.views import View
from catalog.forms import ProductForm, ProductModeratorForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied


class CatalogHomeView(ListView):
    model = Product
    template_name = "catalog/base.html"
    context_object_name = "products"


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


class CatalogDetailView(DetailView):
    model = Product


def contact(request):
    return render(request, "catalog/contacts.html")

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:product_list")


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
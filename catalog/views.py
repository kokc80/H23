from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def index(request):
    return render(request, "base.html")


def product_list(request):
    """контроллер для отображения страницы с подробной информацией о товаре."""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def contact(request):
    return render(request, "contacts.html")


def product_detail(request, product_id):
    # prod = Product.objects.get(id=product_id)
    prod = get_object_or_404(Product, id=product_id)
    context = {"prod": prod}
    return render(request, "product_detail.html", context)

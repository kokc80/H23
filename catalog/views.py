from django.shortcuts import render

from catalog.models import Product


def product_list(request):
    """контроллер для отображения страницы с подробной информацией о товаре."""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_list.html', context)


def contact(request):
    return render(request, "contacts.html")


#def product_detail(request)
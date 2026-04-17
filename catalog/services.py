from config.settings import CACHE_ENABLED
from catalog.models import Product
from django.core.cache import cache


def get_product_from_cache():
    """Функция получения данных из кеша"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    product_val = cache.get(key)
    if product_val is not None:
        return product_val
    product_val= Product.objects.all()
    cache.set(key,product_val)
    return product_val


def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)
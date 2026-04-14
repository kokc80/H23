from config.settings import CACHE_ENABLED
from catalog.models import Product
from django.core.cache import cache


def get_product_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    product_val = cache.get(key)
    if product_val is not None:
        return product_val
    product_val = Product.objects.all()
    cache.set(key, product_val)
    return product_val
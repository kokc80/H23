# catalog\urls.py
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import product_list, contact, index

app_name = CatalogConfig.name

urlpatterns = [
    path("", index),
    path("product/", product_list, name="product_list"),
    path("contact/", contact, name="contact"),
]

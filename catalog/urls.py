# catalog\urls.py
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import product_list, contact, index, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", index),
    path("product_list/", product_list, name="product_list"),
    path("product/<int:product_id>/", product_detail, name="product_list"),
    path("contact/", contact, name="contact"),
]

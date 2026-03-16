# catalog\urls.py
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import (
    CatalogHomeView,
    CatalogDetailView,
    CatalogContactsView,
    CatalogListView,
    ProductCreateView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogHomeView.as_view(), name="base"),
    path("contacts/", CatalogContactsView.as_view(), name="contacts"),
    path("product_list/", CatalogListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>/", CatalogDetailView.as_view(), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
]

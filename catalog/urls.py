# catalog\urls.py
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import (
    CatalogHomeView,
    CatalogDetailView,
    CatalogContactsView,
    CatalogListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView

)

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogHomeView.as_view(), name="base"),
    path("home/", CatalogHomeView.as_view(), name="home"),
    path("contacts/", CatalogContactsView.as_view(), name="contacts"),
    path("product_list/", CatalogListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>/", CatalogDetailView.as_view(), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_edit/<int:pk>/", ProductUpdateView.as_view(), name="product_edit"),
    path("product_delete/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]

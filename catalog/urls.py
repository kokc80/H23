# catalog\urls.py
from django.urls import path, include
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    CatalogHomeView,
    CatalogDetailView,
    CatalogContactsView,
    CatalogListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, ProductsByCategoryView, CategoryListView

)

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogHomeView.as_view(), name="base"),
    path("home/", CatalogHomeView.as_view(), name="home"),
    path("contacts/", CatalogContactsView.as_view(), name="contacts"),
    path("product_list/", cache_page(60)(CatalogListView.as_view()), name="product_list"),
    path("product_detail/<int:pk>/", cache_page(60)(CatalogDetailView.as_view()), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_edit/<int:pk>/", ProductUpdateView.as_view(), name="product_edit"),
    path("product_delete/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path('category/<int:pk>/', ProductsByCategoryView.as_view(), name='products_by_category'),
    path("category_list/", CategoryListView.as_view(), name="category_list"),
]

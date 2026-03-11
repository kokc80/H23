# catalog\urls.py
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import CatalogHomeView, CatalogDetailView, CatalogContactsView, CatalogListView

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogHomeView.as_view(), name="base"),
    path("contacts/", CatalogContactsView.as_view(), name="contacts"),
    path("product_list/", CatalogListView.as_view(), name="product_list"),
    path("product_detail/<int:product_id>/", CatalogDetailView.as_view(), name="product_detail"),
]

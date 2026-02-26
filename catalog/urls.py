from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import catalog, catalog_con

app_name = CatalogConfig.name

urlpatterns = [
    path("", catalog, name="home"),
    path("contacts/", catalog_con, name="contacts"),
]

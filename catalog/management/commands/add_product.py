from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление тестовых продуктов"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        categ, _ = Category.objects.get_or_create(name_cat="Категория 1")

        products = [
            {
                "name_prod": "Продукт1",
                "descr_prod": "Описание продукта 1",
                "category": categ,
                "price": 1000,
                "date_created_at": "2026-01-01",
                "date_updated_at": "2026-10-01",
            },
            {
                "name_prod": "Продукт1",
                "descr_prod": "Описание продукта 1",
                "category": categ,
                "price": 1000,
                "date_created_at": "2026-02-02",
                "date_updated_at": "2026-10-01",
            },
            {
                "name_prod": "Продукт1",
                "descr_prod": "Описание продукта 1",
                "category": categ,
                "price": 1000,
                "date_created_at": "2026-03-03",
                "date_updated_at": "2026-10-01",
            },
        ]

        for prod_data in products:
            product, created = Product.objects.get_or_create(**prod_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully added student: {prod_data["name_prod"]} '
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Product already exists: {prod_data["name_prod"]} '
                    )
                )

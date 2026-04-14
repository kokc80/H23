from django.db import models
from django.db.models import SET_NULL
from users.models import CustomUser


class Category(models.Model):
    name_cat = models.CharField(max_length=50, verbose_name="Категория")
    descr_cat = models.CharField(max_length=100, verbose_name="Описание")

    def __str__(self):
        return f"{self.name_cat}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name_cat"]


class Product(models.Model):
    name_prod = models.CharField(max_length=50, verbose_name="Продукт")
    descr_prod = models.CharField(max_length=100, verbose_name="Описание")
    image = models.ImageField(upload_to="image/catalog/")
    category = models.ForeignKey(
        Category,
        on_delete=SET_NULL,
        related_name="products",
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        null=True,
        blank=True,
    )
    price = models.FloatField(default=0.0, verbose_name="Цена за покупку")
    date_created_at = models.DateField(verbose_name="Дата создания")
    date_updated_at = models.DateField(verbose_name="Дата изменения")
    owner = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Владелец")
    STATUS_CHOICES = [("awaiting_publication", "Ждет публикации"), ("publication", "Опубликовано")]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="awaiting_publication", verbose_name="Статус публикации"
    )

    def __str__(self):
        return f"{self.name_prod}, ({self.category})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name_prod"]
        permissions = [("can_unpublish_product","разрешение на отмену публикации продукта"),
                       ("can_delete_product", "разрешение на удаление любого продукта"),
                       ]

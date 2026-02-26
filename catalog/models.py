from django.db import models


class Category(models.Model):
    name_cat = models.CharField(max_length=50, verbose_name="Категория")
    descr_cat = models.CharField(max_length=100, verbose_name="Описание")

    def __str__(self):
        return f'{self.name_cat}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name_cat"]


class Product(models.Model):
    name_prod = models.CharField(max_length=50, verbose_name="Продукт")
    descr_prod = models.CharField(max_length=100, verbose_name="Описание")
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
        help_text="Введите категорию продукта",
    )
    price = models.FloatField(default=0.0, verbose_name="Цена за покупку")
    date_created_at = models.DateField( verbose_name="Дата создания")
    date_updated_at = models.DateField( verbose_name="Дата изменения")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ["name_prod"]

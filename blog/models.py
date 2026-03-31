from django.db import models
from django.db.models import SET_NULL


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.CharField(verbose_name="Содержимое")
    preview_image = models.ImageField(upload_to="image/blogs/", blank=True, null=True, verbose_name="Превью")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    published = models.BooleanField(default=True, verbose_name="Признак публикации")
    views_count = models.IntegerField(default=0, verbose_name="Счетчик просмотров")

    def __str__(self):
        return self.title


class Meta:
    verbose_name = "Статья"
    verbose_name_plural = "Статьи"
    ordering = ["title"]

from tkinter import image_names

from django import forms
from .models import Category, Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name_prod"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название товара"})
        self.fields["descr_prod"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание товара"}
        )
        self.fields["image"].widget.attrs.update({"class": "form-control-file"})
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update({"class": "form-control", "placeholder": "Введите стоимость товара"})

    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    def clean(self):
        cleaned_data = super().clean()
        name_prod = cleaned_data.get("name_prod")
        descr_prod = cleaned_data.get("descr_prod")

        for word in self.forbidden_words:
            if word.lower() == name_prod.lower():
                self.add_error("name_prod", f"Название содержит запрещенное слово: {word}")
            if word.lower() == descr_prod.lower():
                self.add_error("descr_prod", f"В описании содержится запрещенное слово: {word}")
        return cleaned_data

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")

        if price < 0 and price is not None:
            raise forms.ValidationError(f"Цена не может быть отрицательной")

    def clean_image(self):
        cleaned_data = super().clean()
        image = cleaned_data.get("image")
        image_name = image.name

        if image:
            if not image.name.lower().endswith((".jpg", ".png", ".jpeg")):
                raise forms.ValidationError(f"Недопустимый формат файла: {image_name} . Загрузите JPG или PNG")

            max_size = 5242880
            if image.size > max_size:
                raise forms.ValidationError(f"Изображение: {image_name} не может быть больше 5 МБ")
        return image
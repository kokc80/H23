from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email = "testsu@mail.ru",
            first_name = "testsuFirstName",
            last_name = "testsuLastName"
        )
        user.is_staff = True
        user.is_superuser = True
        # Задаем пароль хешируем
        user.set_password("1234")

        user.save()

        self.stdout.write(self.style.SUCCESS(f"Администратор успешно создан с почтой {user.email}!"))
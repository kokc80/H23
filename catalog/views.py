from django.shortcuts import render


def catalog(request):
    """контроллер для страницы home.html"""
    return render(request, "home.html")


def catalog_con(request):
    """контроллер для страницы contacts.html"""
    return render(request, "contacts.html")

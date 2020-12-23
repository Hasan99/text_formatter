from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def format_text(request):
    data = {
        "formatted_text": "",
        "error_message": "",
        "count_of_characters_with_spaces": 0,
        "count_of_characters_without_spaces": 0
    }

    return render(request, "home.html", data)

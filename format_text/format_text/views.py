import string
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def remove_punctuation(text):
    text_without_punctuations = ""

    for character in text:
        if character not in string.punctuation:
            text_without_punctuations = text_without_punctuations + character

    return text_without_punctuations


def format_text(request):
    data = {
        "formatted_text": "",
        "error_message": "",
        "result_message": "",
        "count_of_characters": ""
    }

    text = request.GET.get("text")
    remove_punctuations = request.GET.get("remove_punctuations")
    capitalize_all = request.GET.get("capitalize_all")
    remove_extra_spaces = request.GET.get("remove_extra_spaces")
    remove_lines = request.GET.get("remove_lines")
    count_characters = request.GET.get("count_characters")
    no_operation_specified = True
    allowed_to_show_success_message = True

    if not text:
        data["error_message"] = "Enter some text!"
        allowed_to_show_success_message = False
    else:
        data["formatted_text"] = text
        if remove_punctuations:
            data["formatted_text"] = remove_punctuation(data["formatted_text"])
            no_operation_specified = False
        if capitalize_all:
            data["formatted_text"] = data["formatted_text"].upper()
            no_operation_specified = False
        if remove_extra_spaces:
            data["formatted_text"] = data["formatted_text"].strip()
            no_operation_specified = False
        if remove_lines:
            data["formatted_text"] = data["formatted_text"].rstrip("\n")
            no_operation_specified = False
        if count_characters:
            data["count_of_characters"] = f"Characters Count: {len(data['formatted_text'])}"
            no_operation_specified = False

    if text and no_operation_specified:
        data["error_message"] = "Select any operation!"
        data["formatted_text"] = text
        allowed_to_show_success_message = False

    if allowed_to_show_success_message:
        data["result_message"] = "Text formatted successfully!"

    return render(request, "home.html", data)

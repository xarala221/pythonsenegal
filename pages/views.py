from django.shortcuts import render


def index(request):
    return render(request, "pages/index.html")


def about(request):
    return render(request, "pages/about.html")


def code_of_conduct(request):
    return render(request, "pages/code_of_conduct.html")

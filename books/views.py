from django.shortcuts import render


# Create your views here.


def index_view(request):
    context = {}
    template = "index.html"
    return render(request, template, context)

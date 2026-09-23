from django.shortcuts import render
from django.http import HttpResponse


def test_views(request):
    return HttpResponse("Hello World! 1")

def test_views_2(request):
    return render(request, "my_app/index.html", context={"info": "password"})

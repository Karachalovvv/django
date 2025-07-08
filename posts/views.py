from django.shortcuts import render, HttpResponse

def test(request):
    return HttpResponse("Hello, world! This is a test view.")

def html_view(request):
    return render(request, "base.html")
from django.http import HttpResponse


# Create your views here.

def cake_blog(request):
    return HttpResponse("Hello, Cakes!")

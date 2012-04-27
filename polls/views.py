# Create your views here.
from django import HttpResponse

def index(request):
    return HttpResponse("Hello, World. You are at the poll index")
    
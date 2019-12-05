from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("Hello, You're at the front page.")
    # return render(request, 'course/index.html')

def testing(request):
    return render(request, 'common/index.html')
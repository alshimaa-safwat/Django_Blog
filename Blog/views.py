from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# for testing
def index(request):
    return render(request, 'layouts/dashboard/base.html')

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def ImageWorker_test(request):
    return HttpResponse("this is ImageWorker test...ok!")

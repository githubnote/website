from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import site_info
from django.template import RequestContext


# Create your views here.
def ImageWorkerTest(request):
    try:
        site_error = site_info.objects.get()
    except site_error.DoesNotExist:
        raise Http404("ImageWorker does not exist")


    context = {"site_name": site_info.objects.get(),
               "site_slogan": site_info.objects.get(),
               "site_author": site_info.objects.get(),
               "test":"adfa111111adf",


    }

    return render(request, "ImageWorkerTest.html",context)



def index(request):
    context = {"text": "123"}

    return render(request, "index.html", context)


def test_info(request):
    context = site_info.objects.all()

    return render(request, "testInfo.html", {"test":context})

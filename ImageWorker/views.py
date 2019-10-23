from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from ImageWorker.models import site_info

# Create your views here.
def ImageWorkerTest(request):

    try:
        site_error = site_info.objects.get()
    except site_error.DoesNotExist:
        raise Http404("Question does not exist")







    context = {"site_name": site_info.objects.get().site_name,
               "site_slogan": site_info.objects.get().site_slogan,
               "site_author": site_info.objects.get().site_author,
               "test":"adfaadf",


    }

    return render(request, "ImageWorkerTest.html",context)
   
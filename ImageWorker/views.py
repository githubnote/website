from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import site_info


from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


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

    paginator = Paginator(list(context), 5)
    page = request.GET.get('page')


    indexmix = int(page) - 5
    indexmax = int(page) + 5

    if indexmix < 1 :
        indexmix = 1
    if indexmax > paginator.num_pages:

        indexmax = paginator.num_pages

    indexnum=[x for x in range(indexmix,indexmax)]


    try:
        #通过获取上面的page参数，查询此page是否为整数并且是否可用
        context_obj = paginator.page(page)
    except PageNotAnInteger:
        context_obj = paginator.page(1)
    except (EmptyPage, InvalidPage):
        context_obj = paginator.page(paginator.num_pages)

    return render(request, "testInfo.html",
                  {"test": context_obj,
                   "page": page,
                    "indexnum": indexnum,
                    }
    )

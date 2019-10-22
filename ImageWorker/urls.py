from django.urls import path
from . import views

urlpatterns = [
    path('', views.ImageWorker_test, name='ImageWorker_test'),
]

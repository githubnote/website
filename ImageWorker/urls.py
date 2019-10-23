from django.urls import path
from . import views


app_name="imageworker"
urlpatterns = [
    path('test/', views.ImageWorkerTest, name='ImageWorkerTest'),
    path('', views.index, name='index'),

]

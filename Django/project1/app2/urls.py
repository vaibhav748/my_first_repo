from django.urls import path
from . import views

urlpatterns = [
    path('page1',views.myfunction1, name="index1"),
    path('page2', views.myfunction2, name="about1")
]

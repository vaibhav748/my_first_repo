from django.urls import path
from . import views

urlpatterns = [
    path('page1',views.myfunction, name = 'index'),
    path('page2',views.about, name = 'about'),
    path('page3',views.myfirstpage, name='mypage1'),
    path('page4',views.mysecondpage, name='mypage2'),
    path('page5',views.mythirdpage, name='mypage3')
]
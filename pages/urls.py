from django.urls import path

from . import views

urlpatterns = [
    path('', views.show1, name='show'),
    path('p2/', views.show2, name='show'),
    path('p3/', views.show3, name='show'),
]

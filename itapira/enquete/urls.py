from django.urls import patch

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('felipe', views.caneta, name='caneta')
]
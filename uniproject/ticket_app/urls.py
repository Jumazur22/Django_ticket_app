from django.urls import path

from . import views

#This calls a view by mapping it to a url
urlpatterns = [
    path('', views.index, name="index")
]

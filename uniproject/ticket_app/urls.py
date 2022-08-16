from django.urls import path

from . import views

app_name = "ticket_app"


#This calls a view by mapping it to a url
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create_ticket, name="create_ticket"),
    path('register', views.register_request, name='register')
]

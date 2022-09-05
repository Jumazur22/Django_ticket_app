from django.urls import path
from django.contrib import admin

from . import views

#This calls a view by mapping it to a url
urlpatterns = [
    path("", views.register_request, name="register"),
    path('admin/', admin.site.urls),
    path("index", views.index, name="index"),
    path("create", views.create_ticket, name="create_ticket"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("update/<str:pk>", views.update_ticket, name="update_ticket"),
]

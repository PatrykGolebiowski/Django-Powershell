from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('NewADUser', views.newaduser, name="NewADuser"),
]
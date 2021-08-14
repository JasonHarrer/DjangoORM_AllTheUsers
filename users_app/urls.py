from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_user_form', views.new_user_form)
]

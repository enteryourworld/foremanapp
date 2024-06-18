from django.urls import path
from . import views
from .views import addworker, addforemans,addequipment

urlpatterns = [
    path('', views.list),
    path('create-project', views.projectnew),
    path('add-worker/', addworker, name="addworker"),
    path('registration',views.registration),
    path('add-foremans/', addforemans, name="addforemans"),
    path('add-equipment/', addequipment, name="addequipment"),
]
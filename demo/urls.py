from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_records/', views.get_records, name='get_records'),
    path('get_new_record/', views.get_new_record, name='get_new_record'),
    path('add_record/', views.add_record, name='add_record'),
]
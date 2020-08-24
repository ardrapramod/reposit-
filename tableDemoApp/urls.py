from django.urls import path

from tableDemoApp import views

urlpatterns = [
    path('dataTable', views.dataTable, name='dataTable'),

]
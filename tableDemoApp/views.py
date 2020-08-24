from django.contrib import auth
from django.shortcuts import render
from django.views import View

from .models import dataTables


# def dataTable(request):
#    dests = dataTables.objects.all()

#   return render(request, 'dataTable.html', {'dests': dests})

class dataTable(View):
    def get(self, request):

     return render(request, 'dataTable.html', {'dests': dests})

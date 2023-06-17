from django.shortcuts import render
from .models import Calatog
# Create your views here.


def calatogs_list(request):
    data_context = Calatog.objects.all()
    return render(request, 'catalog/archivo.html', context={
        "data_context": data_context
    })

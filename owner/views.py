from django.shortcuts import render
from .models import Owner
# Create your views here.


def owners_list(request):

    data_context = {
        'nombre_owner': 'Luis Pardo',
        'edad': 24,
        'pais': 'Peru'
    }

    datos = Owner.objects.all()

    # Lista filtrada
    peru = Owner.objects.filter(pais='Peru')

    return render(request, 'owner/archivo.html', context={
        "data_context": data_context,
        "datos": datos,
        "peru": peru
    })

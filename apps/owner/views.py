from django.shortcuts import render, redirect
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import OwnerSerializer
from .models import Owner
from .forms import OwnerForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.


def owner_list(request):

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


def owner_list2(request):
    owners = Owner.objects.all()
    peru = Owner.objects.filter(pais='Peru')
    argentina = Owner.objects.filter(pais='Argentina')
    return render(request, 'owner/owner_list.html', context={
        'owners': owners,
        'peru': len(peru),
        'argentina': len(argentina)
    })


def owner_search(request):
    query = request.GET.get('q', '')
    consulta = Q(pais__icontains=query) | Q(nombre__icontains=query)
    results = Owner.objects.filter(consulta)
    print(results)
    return render(request, 'owner/owner_search.html', context={
        'results': results,
        'query': query
    })


def owner_delete(request, id_owner):
    owner = Owner.objects.get(id = id_owner)
    owner.delete()
    #Return para ejercicio 4
    return redirect('owner_list2')


def owner_confirm_delete(request, id_owner):
    owner = Owner.objects.get(id=id_owner)
    if request.method == 'POST':
        owner.delete()
        return redirect('owner_list2')

    return render(request, 'owner/owner_confirm_delete.html', context={
        'owner': owner,
    })


def owner_edit(request, id_owner):
    owner = Owner.objects.get(id=id_owner)
    form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais, 'dni':owner.dni})
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_list2')

    return render(request, 'owner/owner_update.html', context={
        'form': form
    })

# USANDO LAS VISTAS BASADAS EN CLASES


class OwnerList(ListView):
    model = Owner
    template_name = 'owner/owner_list_vc.html'


class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_create_vc.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_update_vc.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerDelete(DeleteView):
    model = Owner
    template_name = 'owner/owner_delete_vc.html'
    success_url = reverse_lazy('owner_list_vc')


@api_view(['GET', 'POST'])
def owner_list_api(request):
    if request.method == 'GET':
        queryset = Owner.objects.all()
        serializers_class = OwnerSerializer(queryset, many=True)
        return Response(serializers_class.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializers_class = OwnerSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=status.HTTP_201_CREATED)
    return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def owner_detail_api(request, pk):
    owner = Owner.objects.filter(id=pk).first()
    if request.method == 'GET':
        serializers_class = OwnerSerializer(owner)
        return Response(serializers_class.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializers_class = OwnerSerializer(owner, data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        owner.delete()
        return Response('Owner ha sido eliminado correctamente de la BD', status=status.HTTP_200_OK)

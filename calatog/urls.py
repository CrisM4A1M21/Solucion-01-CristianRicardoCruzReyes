from django.urls import path
from calatog import views


urlpatterns = [
    path('calatogs_list/', views.calatogs_list, name='calatogs_list')
]
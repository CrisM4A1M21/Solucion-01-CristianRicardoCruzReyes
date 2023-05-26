from django.urls import path
from owner import views


urlpatterns = [
    path('owners_list/', views.owners_list, name='owners_list')
]
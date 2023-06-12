from django.urls import path
from owner import views


urlpatterns = [
    path('owner_list/', views.owner_list, name='owner_list'),
    path('owner_list2/', views.owner_list2, name='owner_list2'),
    path('owner_search/', views.owner_search, name='owner_search'),
    path('owner_delete/<int:id_owner>', views.owner_delete, name='owner_delete'),
    path('owner_confirm_delete/<int:id_owner>', views.owner_confirm_delete, name='owner_confirm_delete'),
    path('owner_update/<int:id_owner>', views.owner_edit, name='owner_update'),
    path('owner_list_vc/', views.OwnerList.as_view(), name='owner_list_vc'),
    path('owner_create_vc/', views.OwnerCreate.as_view(), name='owner_create_vc'),
    path('owner_update_vc/<int:pk>', views.OwnerUpdate.as_view(), name='owner_update_vc'),
    path('owner_delete_vc/<int:pk>', views.OwnerDelete.as_view(), name='owner_delete_vc')
]

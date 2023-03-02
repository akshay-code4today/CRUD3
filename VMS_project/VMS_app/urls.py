from django.urls import path
from .views import VehicleListView,VehicleDetailView,VehicleCreateView,VehicleUpdateView,VehicleDeleteView,TemplateDeleteView

urlpatterns = [
    path('list/', VehicleListView.as_view(), name='vehicle_list'),
    path('list/detail/<int:pk>', VehicleDetailView.as_view(), name='vehicle_detail'),
    path('create/', VehicleCreateView.as_view(), name='vehicle_create'),
    path('list/detail/update/<int:pk>/', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('list/detail/delete/<int:pk>/', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('about/', TemplateDeleteView.as_view(), name='About_us'),
]

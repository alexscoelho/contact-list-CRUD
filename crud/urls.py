from django.urls import path
from crud import views

urlpatterns = [
    path('contact/', views.contact_list),
    path('contact/<int:pk>', views.contact_detail),
    path('group/', views.group_list),
    path('group/<int:pk>', views.group_detail),
]


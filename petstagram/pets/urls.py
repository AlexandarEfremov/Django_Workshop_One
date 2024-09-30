from django.urls import path, include
from petstagram.pets import views

urlpatterns = [
    path('add/', views.pet_add_page, name='pets-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details_page, name='pets-details'),
        path('edit/', views.pet_edit_page, name='pets-edit'),
        path('delete/', views.pet_delete_page, name='pets-delete'),
    ]))
]
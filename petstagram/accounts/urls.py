from django.urls import path, include
from petstagram.accounts import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('profile/<int:pk>/', include([ #we do this as to not repeat profile 3 times
        path('', views.profile_details_page, name='profile-details'),
        path('edit/', views.profile_edit_page, name='profile-edit'),
        path('delete/', views.profile_delete_page, name='profile-delete')
    ])), #all of the pk apps need to receive the pk parameter
]
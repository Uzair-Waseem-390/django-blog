from django.urls import path

from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # Category management
    path('category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:pk>/', views.delete_category, name='delete_category'),

    # Post management
    path('post/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:pk>/', views.delete_post, name='delete_post'),
    
    path('category/add/', views.add_category, name='add_category'),
    path('post/add/', views.add_post, name='add_post'),
]
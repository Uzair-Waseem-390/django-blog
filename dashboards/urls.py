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
    
    
    # User management
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('user/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('user/delete/<int:user_id>/', views.delete_user, name='delete_user'),
]
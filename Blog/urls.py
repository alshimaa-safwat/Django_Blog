from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.get_dashboard, name="dashboard.index"),
    path('users', views.get_users, name="dashboard.users.index"),
    path('categories/', views.get_categories),
    path('categories/edit/<id>', views.edit_category),
    path('categories/delete/<id>', views.delete_category),
    path('categories/new/', views.add_category),
    path('posts/', views.get_posts),
    path('delete/<post_id>', views.delete_post),
]

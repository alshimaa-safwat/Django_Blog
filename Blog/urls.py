from django.urls import path
from Blog import views

urlpatterns = [
    path('categories/', views.get_categories),
    path('categories/edit/<id>', views.edit_category),
    path('categories/delete/<id>', views.delete_category),
    path('categories/new/', views.add_category),
    path('posts/', views.get_posts),
    path('posts/new/', views.add_post),
    path('delete/<post_id>', views.delete_post),
]

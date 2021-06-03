from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.get_dashboard, name="dashboard.index"),
    path('users', views.get_users, name="dashboard.users.index"),
    path('users/new/', views.create_user, name="dashboard.users.new"),
    path('users/<id>/edit', views.edit_user, name="dashboard.users.edit"),
    path('users/<id>/update', views.update_user, name="dashboard.users.update"),
    path('users/<id>/delete', views.delete_user, name="dashboard.users.delete"),

    path('categories/', views.get_categories),
    path('categories/edit/<id>', views.edit_category),
    path('categories/delete/<id>', views.delete_category),
    path('categories/new/', views.add_category),
    path('posts/', views.get_posts),
    path('posts/new/', views.add_post),
    path('delete/<post_id>', views.delete_post),
    path('editpost/<post_id>', views.edit_post),

    path('words/', views.words),
    path('words/editWord/<id>', views.edit_word),
    path('words/deleteWord/<id>', views.delete_word),
    path('words/addWord/', views.add_word),
]

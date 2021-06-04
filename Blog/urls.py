from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.get_dashboard, name='dashboard.index'),
    path('users', views.get_users, name='dashboard.users.index'),
    path('users/new', views.create_user, name='dashboard.users.new'),
    path('users/<id>/edit', views.edit_user, name='dashboard.users.edit'),
    path('users/<id>/update', views.update_user, name='dashboard.users.update'),
    path('users/<id>/delete', views.delete_user, name='dashboard.users.delete'),
    path('users/<id>/lock', views.lock_user, name='dashboard.users.lock'),
    path('users/<id>/unlock', views.unlock_user, name='dashboard.users.unlock'),
    path('users/<id>/upgrade', views.upgrade_user, name='dashboard.users.upgrade'),
    path('users/<id>/downgrade', views.downgrade_user, name='dashboard.users.downgrade'),

    path('categories', views.get_categories, name='dashboard.categories.index'),
    path('categories/<id>/edit', views.edit_category, name='dashboard.categories.edit'),
    path('categories/<id>/delete', views.delete_category, name='dashboard.categories.delete'),
    path('categories/new', views.add_category, name='dashboard.categories.new'),

    path('posts', views.get_posts, name='dashboard.posts.index'),
    path('posts/new', views.add_post, name='dashboard.posts.new'),
    path('posts/<id>/delete', views.delete_post, name='dashboard.posts.delete'),
    path('posts/<id>/edit', views.edit_post, name='dashboard.posts.edit'),

    path('words', views.words, name='dashboard.words.index'),
    path('words/<id>/edit', views.edit_word, name='dashboard.words.edit'),
    path('words/<id>/delete', views.delete_word, name='dashboard.words.delete'),
    path('words/new', views.add_word, name='dashboard.words.new'),
<<<<<<< HEAD
=======

    path('tags/', views.tags, name='dashboard.tags.index'),
    path('tag/new', views.add_tag , name='dashboard.tags.new'),

>>>>>>> 3d5916f02edcddc095993b500944be1be3f6c06d
]

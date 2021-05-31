from django.urls import path
from Blog import views

urlpatterns = [
    path('categories/', views.get_categories),
    path('categories/edit/<id>', views.edit_category),
    path('categories/delete/<id>', views.delete_category),
    path('categories/new/', views.add_category),
    path('words/', views.words),
    path('words/editWord/<id>', views.edit_word),
    path('words/deleteWord/<id>', views.delete_word),
    path('words/addWord/', views.add_word),
]

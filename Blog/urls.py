from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.index, name="index"),

    path('words/', views.words),
    path('words/editWord/<id>', views.editWord),
    path('words/deleteWord/<id>', views.deleteWord),
    path('words/addWord/', views.addWord),
]

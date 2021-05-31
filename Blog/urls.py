from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.get_dashboard, name="dashboard.index"),
    path('users', views.get_users, name="dashboard.users.index"),
]

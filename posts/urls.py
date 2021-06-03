from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('<postid>/addcomment',views.add_comment),
    path('<comid>/deletecomment',views.deletecomment),
    url(r'^about/$', views.about),
	path('listcat/<catid>', views.list_cat),
    url(r'^like$', views.get_like_data),
    
]
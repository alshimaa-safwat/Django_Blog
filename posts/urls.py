from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('<postid>/addcomment',views.addComment),
    path('<comid>/deletecomment',views.deletecomment),
    url(r'^about/$', views.about),
	path('listcat/<catid>', views.listCat),
    url(r'^like$', views.getLikeData),
    
]
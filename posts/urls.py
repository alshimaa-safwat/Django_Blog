from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^subscribe$', views.getSubscribeData),
     path('<postid>/addcomment',views.add_comment),
    path('<comid>/addreply',views.add_reply),
    path('<comid>/deletecomment',views.delete_comment),
    path('<repid>/deletereply',views.delete_reply),
    path('addtag',views.add_tag),
    path('listtag/<tagid>',views.list_tags),
]
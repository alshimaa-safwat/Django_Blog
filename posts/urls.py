from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    url(r'^subscribe$', views.get_subscribe_data),
     path('<postid>/addcomment',views.add_comment),
    path('<comid>/addreply',views.add_reply),
    path('<comid>/deletecomment',views.delete_comment),
    path('<repid>/deletereply',views.delete_reply),
    path('addtag',views.add_tag),
    path('listtag/<tagid>',views.list_tags),
    url(r'^about/$', views.about),
    path('listcat/<catid>', views.list_cat),
    url(r'^like$', views.get_like_data),
    # posts
    url(r'^$', views.homePage),
    url(r'^(?P<postid>[\w]+)/$', views.display_post),
    url('new', views.add_post),
    path('editpost/<postid>', views.edit_post),
    path('deletepost/<postid>', views.delete_post),
]

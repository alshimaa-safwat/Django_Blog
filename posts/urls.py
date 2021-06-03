from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('<postid>/addcomment', views.add_comment),
    path('<comid>/deletecomment', views.delete_comment),
    url(r'^about/$', views.about),
    path('listcat/<catid>', views.list_cat),
    url(r'^like$', views.get_like_data),
    url(r'^subscribe$', views.getSubscribeData),
    path('<comid>/addreply', views.addReply),
    path('<repid>/deletereply', views.deletereply),
    path('addtag', views.addTag),
    path('listtag/<tagid>', views.listTags),
    # posts
    url(r'^$', views.homePage),
    url(r'^(?P<postid>[\w]+)/$', views.display_post),
    url('new', views.add_post),
    path('editpost/<postid>', views.edit_post),
    path('deletepost/<postid>', views.delete_post),
]

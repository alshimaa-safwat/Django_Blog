from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^subscribe$', views.getSubscribeData),
    path('<postid>/addcomment', views.addComment),
    path('<comid>/addreply', views.addReply),
    path('<comid>/deletecomment', views.deletecomment),
    path('<repid>/deletereply', views.deletereply),
    path('addtag', views.addTag),
    path('listtag/<tagid>', views.listTags),
    path('<comid>/deletecomment', views.deletecomment),
    url(r'^about/$', views.about),
    path('listcat/<catid>', views.listCat),
    url(r'^like$', views.getLikeData),
    # posts
    url(r'^$', views.homePage),
    url(r'^(?P<postid>[\w]+)/$', views.display_post),
    url('new', views.add_post),
    path('editpost/<postid>', views.edit_post),
    path('deletepost/<postid>', views.delete_post),
]

from django.conf.urls import url
#from . import views
from . import classviews
app_name = 'CRUD'
urlpatterns = [
    # Function Based Views
    #url(r'^$',views.todos,name='todos'),
    #url(r'^(?P<pk>[0-9]+)/$',views.todolists,name='detail'),
    #url(r'^createtodo/$',views.createtodo,name ='create'),
    #url(r'^(?P<pk>[0-9]+)/createtask/$',views.createtask,name = 'createtask'),
    

    #Class Based Generic Views
    url(r'^$',classviews.AllTodos.as_view(),name='gtodos'),
    url(r'^(?P<pk>[0-9]+)/$',classviews.DetailTodolist.as_view(),name='gdetail'),
    url(r'^createtodo/$',classviews.Createtodo.as_view(),name='gcreate'),
    url(r'^createtask/$',classviews.Createtodolist.as_view(),name='gcreatetask'),
    url(r'^(?P<pk>[0-9]+)/update/$',classviews.Updatetodo.as_view(),name='gupdate'),
    url(r'^(?P<pk>[0-9]+)/delete/$',classviews.Deletetodo.as_view(),name='gdelete'),
    url(r'^(?P<pk>[0-9]+)/updatetask/$',classviews.Updatetodolist.as_view(),name='glistupdate'),
    url(r'^(?P<pk>[0-9]+)/deletetask/$',classviews.Deletetodolist.as_view(),name='glistdelete'),

]
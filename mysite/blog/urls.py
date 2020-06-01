from django.urls import path,re_path
from . import views

app_name='blog'
#app_name='basic_app'

urlpatterns=[
    path('', views.PostListView.as_view(), name='list'),
    path('new/',views.PostCreateView.as_view(), name='new'),
    path(r'^(?P<pk>\d+)/comment/$',views.CommCreateView.as_view(), name='comment'),
    re_path(r'^(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(), name='edit'),
    re_path(r'^(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(), name='remove'),
    re_path(r'^(?P<pk>\d+)/$',views.PostDetailView.as_view(), name='detail'),
]

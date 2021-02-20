from django.urls import path,re_path
from . import views

app_name = 'hello'

urlpatterns = [
    path('',views.PostListView.as_view(),name='list'),
    re_path(r'^(?P<pk>[-\w]+)/$',views.PostDetailView.as_view(),name='detail'),
    path('create',views.PostCreateView.as_view(),name='create'),
    re_path(r'^update/(?P<pk>\d+)/$', views.PostUpdateView.as_view(), name='update'),
    path('<pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]

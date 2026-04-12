from django.contrib import admin
from django.contrib.auth import login, logout
from django.urls import path, include
from blog.views import index, category, post, create_category, PostListView, PostDetailView, PostCreateView, \
    PostUpdateView, DeletePostView, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/<int:category_id>/', category, name='category'),
    #path('post/<int:post_id>/', post, name='post'),
    path('create_category/', create_category, name='create_category'),

    path('post_list/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', DeletePostView.as_view(), name='post_delete'),
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]

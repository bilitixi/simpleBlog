from django.contrib import admin
from django.urls import path
from blog.views import index, category, post, create_category, PostListView, PostDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/<int:category_id>/', category, name='category'),
    #path('post/<int:post_id>/', post, name='post'),
    path('create_category/', create_category, name='create_category'),

    path('post_list/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail')]
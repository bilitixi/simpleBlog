from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Category, Post, UserProfile
from .forms import CreatePostForm, PostUpdateForm
from .utils import create_user
import pandas as pd
import openpyxl

# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {'categories': categories})
def category(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'blog/category.html', {'category': category})
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post.html', {'post': post})
def create_category(request):
    if request.method == 'POST':
        name = request.POST['category_name']
        Category.objects.create(name=name)
        return redirect('category', category_id = Category.objects.last().id)
    return render(request, 'blog/create_category.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('post_list')
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostUpdateForm
    success_url = reverse_lazy('post_list') # reverse back top post
class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        github_url = request.POST['github_url']
        linkedln_url = request.POST['linkedln_url']
        create_user(username, password, first_name, last_name, github_url, linkedln_url)
        return redirect('login')
    return render(request, 'registration/register.html') #new folder
def create_users(request):
    if request.method == 'POST' and request.FILES['names_file']:
        names_file = request.FILES['names_file']
        fs = FileSystemStorage()
        fs.save(names_file.name, names_file) # save file to media
        uploaded_file_url = fs.url(names_file.name)
        uploader_file_path = fs.path(names_file.name)
        excel_read = pd.read_excel(uploader_file_path)
        data = pd.DataFrame(excel_read, columns=['username', 'password', 'first_name', 'last_name','email', 'github', 'linkedln'])
        usernames = data['username'].tolist()
        passwords = data['password'].tolist()
        first_names = data['first_name'].tolist()
        last_names = data['last_name'].tolist()
        emails = data['email'].tolist()
        github_urls = data['github'].tolist()
        linkedln_urls = data['linkedln'].tolist()
        for username, password, first_name, last_name, github_url, email ,linkedln_url in zip(usernames, passwords, first_names, last_names, github_urls, emails, linkedln_urls):
            try:
                user = User.objects.get(username=username)
                user.delete()
                create_user(username, password, first_name, last_name, github_url, email, linkedln_url)

            except User.DoesNotExist:

             create_user(username, password, first_name, last_name, github_url, email, linkedln_url)
        return redirect('login')

        return render(request, 'blog/create_users.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'blog/create_users.html')

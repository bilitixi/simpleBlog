from django.forms import ModelForm, Textarea, Select, FileInput, TextInput

from blog.models import Post



class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'author', 'snippet', 'category', 'header_image']

        widgets= {
            'title': TextInput(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'class': 'form-control'}),
            'author': TextInput(attrs={'class': 'form-control'}),
            'snippet': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'header_image': FileInput(attrs={'class': 'form-control'}),
        }
class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'snippet', 'header_image']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'snippet': TextInput(attrs={'class': 'form-control'}),
            'header_image': FileInput(attrs={'class': 'form-control'}),
        }
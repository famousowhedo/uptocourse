from django.shortcuts import render, redirect
from .models import Profile
from .models import Post
from   .forms import ContactMe
from django.views.generic import ListView, DetailView

# Create your views here.


def home(request):
    return render(request, 'famous/home.html')


def about(request):
    profiles = Profile.objects.get(pk=1)
    return render(request, 'famous/about.html',{"profiles":profiles})

class PostListView(ListView):
    model = Post
    template_name = 'famous/blog.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post


def contact(request):
    if request.method == "POST":
        form = ContactMe(request.POST)
        if form.is_valid():
             form.save()
             return redirect('home')

       
    else:
         form = ContactMe()

   
    return render(request, 'famous/contact.html', {'form':form})   
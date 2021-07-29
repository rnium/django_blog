from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    return render(request, 'blog/homepage.html', {"posts": posts})

def add_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auhor = request.user
            post.date = timezone.now()
            post.save()
            return redirect ('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            p = form.save(commit=False)
            p.auhtor = request.user
            p.date = timezone.now()
            p.save()
            return redirect('post_detail', pk=p.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/new_post.html', {"form": form})
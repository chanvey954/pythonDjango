from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "Post":
        form = PostForm(request.Post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

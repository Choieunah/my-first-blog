from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm




def post_list(request):
    q = request.GET.get('q', '')

    post_list = Post.objects.all() #전체내용가져오기

    if q:
        post_list = post_list.filter(title__icontains=q)
        

    return render(request, 'blog/post_list.html',{
            'post_list' : post_list,
            'q': q,
        })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html',{
            'post': post,
        })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog.views.post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
            'form':form,
    })

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog.views.post_detail',pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
            'form':form,
    })
#filter

# Create your views here

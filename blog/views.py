from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def post_list(request):
  #posts=Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
  posts=Post.objects.all()
  
  return render(request,'blog/post_list.html',{'posts':posts})
 
def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method=='POST':
        
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.autor=request.user
            post.data_publicada=timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
        
    else:
      form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
  
  

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post, Todo
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
#from .models import Todo

# Create your views here.
def index(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#def post_new(request):
#    form = PostForm()
#    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def Officemanagement(request):
     return render(request, 'blog/Officemanagement.html', {})
 
def index_2(request):
     return render(request, 'blog/index.html', {})
 
def Workmanagement(request):
    return render(request, 'blog/Workmanagement.html', {})

def todoapp(request):
    todo_items = Todo.objects.all()
    return render(request, 'blog/Workmanagement.html',{'todo_items':todo_items})
#入力を保存
def todo_post(request):
    todo_task = Todo(content = request.POST['content'])
    todo_task.save()
    return HttpResponseRedirect('/Workmanagement/')

def todo_delete(request,task_id):
    delete_task = Todo.objects.get(id=task_id)
    delete_task.delete()
    return HttpResponseRedirect('/Workmanagement/')
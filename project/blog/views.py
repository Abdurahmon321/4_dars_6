'''CRUD'''

# C - Create
# R - Read
# U - Update
# D - Delete


from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post, Category
from .forms import PostForm, CategoryForm

# Create your views here.



def all_posts(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'title': "Barcha maqolalar"
    }
    return render(request, 'blog/index.html', context=context)


def posts_by_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'categories': categories,
        'title': f"{category.title} ga tegishli maqolalar"
    }
    return render(request, 'blog/index.html', context=context)


# Read
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context=context)


def post_create(request):

    form = PostForm(data=request.POST)
    if form.is_valid():
        form.save()

    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'blog/post_form.html', context=context)


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(data=request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', pk=pk)
    context = {
        'form': form
    }
    return render(request, 'blog/post_form.html', context)


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('index')

    context = {
        'post': post
    }
    return render(request, 'blog/post_delete.html', context)


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        "category": category
    }
    return render(request, "category/category_detail.html", context=context)


def category_create(request):
    form = CategoryForm(data=request.POST)
    if form.is_valid():
        form.save()
    form = CategoryForm()
    context = {
        "category": form
    }
    return render(request, "category/category_create.html", context=context)


def category_update(request, pk):
    # post = Post.objects.get(pk=pk)
    # form = PostForm(data=request.POST or None, instance=post)
    # if form.is_valid():
    #     form.save()
    #     return redirect('post_detail', pk=pk)
    # context = {
    #     'form': form
    # }
    # return render(request, 'blog/post_form.html', context)
    category = Category.objects.get(pk=pk)
    form = CategoryForm(data=request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_detail', pk=pk)
    context = {
        'form': form
    }
    return render(request, "category/category_update.html", context)


def category_delete(request, pk):
    # post = Post.objects.get(pk=pk)
    #
    # if request.method == 'POST':
    #     post.delete()
    #     return redirect('index')
    #
    # context = {
    #     'post': post
    # }
    # return render(request, 'blog/post_delete.html', context)
    category = Category.objects.get(pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('index')

    context = {
        "category": category
    }

    return render(request, 'category/category_delete.html', context)




# def home(request):
#
#     text = "<h1>Maqolalar ro'yxati</h1>\n\n"
#
#     posts = Post.objects.all()
#     for post in posts:
#         text += (f"<p>Title: {post.title}</p>\n"
#                  f"<p>Content: {post.content}</p>\n")
#
#     return HttpResponse(text)
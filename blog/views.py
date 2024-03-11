from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import PostForm
from taggit.models import Tag
from django.contrib.auth.models import User


# Create your views here.


def post_list(request):
    posts=Post.objects.all().order_by("id")
    return render(request, "post_list.html", {"posts":posts})


def post_detail(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    return render(request, "post_detail.html", {"post": post})


def create_post(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)#we dont save   it , unless we will add something
            post.author=request.user
            post.save()
            form.save_m2m()
            return redirect("post_list")
        else:
            return redirect("post_list")
    else:
        form=PostForm()
    return render(request,"create_post.html",{"form":form})


def posts_by_tag(request,tag_slug):
    tag=Tag.objects.get(slug=tag_slug)
    posts=Post.objects.filter(tagged_items__tag_id__in=[tag.id])# rows in table __ , in -filtration
    return render(request, "posts_by_tag.html", {"posts":posts,"tag":tag})



def edit_post(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    if request.user !=post.author:
        return redirect(f"/post/{post_id}/")
    if request.method=="GET":
        form=PostForm(instance=post)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
        return redirect("post_list")
    return render(request, "edit_post.html", {"form":form,"post": post})



def author(request, author_slug):
    author = User.objects.get(username=author_slug)
    posts = Post.objects.filter(author=author)
    return render(request, "author.html", {"authors": author, "posts": posts})

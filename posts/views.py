from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core import serializers

# Create your views here.


def index(requests):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        # post_lists.append("#{}: {}<br><hr>".format(str(count), str(post)))
        post_lists += f"<p><strong>#{count}:</strong> <a href='{post.slug}'> {post.title} </a><br/><small>{post.content}</small></p><hr>"
    return HttpResponse(post_lists)


def index_use_template(requests):
    posts = Post.objects.all()
    json_data = serializers.serialize('json', posts)
    for post in posts:
        post.is_external = post.slug.startswith('http')
    now = datetime.now()
    pageTitle = "測試 Django Blog"
    context = {'locals': locals()}
    return render(requests, "index.html", locals())


def showPost(requests, slug):
    try:
        post = Post.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return redirect('/')
    except MultipleObjectsReturned:
        return redirect('/')    
    return render(requests, "post.html", locals())


def index_use_template1(requests):
    article_records = Post.objects.all()
    now = datetime.now()
    return render(requests, "pages/home.html", locals())


def showPost1(requests, slug):
    try:
        article = Post.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return redirect('/')
    except MultipleObjectsReturned:
        return redirect('/')    
    return render(requests, "pages/post.html", locals())


def login(requests):
    return render(requests, "pages/login.html")

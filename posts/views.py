from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from datetime import datetime

# Create your views here.


def index(requests):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        # post_lists.append("#{}: {}<br><hr>".format(str(count), str(post)))
        post_lists += f"<p><strong>#{count}:</strong> <a href='{post.slug}'> {post.title} </a><br/><small>{post.content}</small></p><hr>"
    return HttpResponse(post_lists)

    # now = datetime.now()
    # return render(requests, "index.html", locals())

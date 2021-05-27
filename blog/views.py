from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.


def news (request):
    posts = Post.objects.order_by('-publish')

    return render(request,'blog/blog.html',{'posts': posts})

def news_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,publish__year=year,publish__month=month,publish__day=day)

    return render(request,
                    'blog/detail.html',
                                {'post': post})

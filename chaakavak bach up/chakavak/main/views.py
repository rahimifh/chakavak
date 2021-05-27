from django.shortcuts import render,get_object_or_404
from .models import Product
from blog.models import Post
# Create your views here.

def main (request):
    posts = Post.objects.order_by('-publish')[:4]
    pro=Product.objects.all()
    return render(request, 'main/home.html', {'pro':pro,'posts':posts})

def products_list (request):
    produ=Product.objects.order_by('-created')
    return render(request, 'main/product.html', {'products':produ})
def products_detail (request, product_pk):
    Pro = get_object_or_404(Product, pk = product_pk)
    return render(request, 'main/pro-detail.html', {'product':Pro})

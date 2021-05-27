from django.shortcuts import render,get_object_or_404, redirect
from .models import Product,agency,apply,slider
from blog.models import Post
from .forms import Apply_form,Apply_formm
from django.urls import reverse
# Create your views here.

def main (request):
    posts = Post.objects.order_by('-publish')[:4]
    pro=Product.objects.all()
    slid=slider.objects.all()[:4]
    return render(request, 'main/home.html', {'pro':pro,'posts':posts, 'slid':slid})

def products_list (request):
    produ=Product.objects.order_by('-created')
    return render(request, 'main/product.html', {'products':produ})
def products_detail (request, product_pk):
    Pro = get_object_or_404(Product, pk = product_pk)
    return render(request, 'main/pro-detail.html', {'product':Pro})

def agency_add (request):
    agency_item=agency.objects.order_by('city')
    return render(request, 'main/agancylist.html',{'agency_items':agency_item})

def request_apply(request):
    if request.method == 'POST':
        form = Apply_form(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect(reverse('main:home'))
    else:
        form = Apply_form()
        return render(request,'main/applying.html',{'form': form})

def about_US (request):
    return render(request, 'main/about-us.html',)

def pishnahad(request):
    if request.method == 'POST':
        form = Apply_formm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect(reverse('main:home'))
    else:
        form = Apply_formm()
        return render(request,'main/pishnahad.html',{'form': form})

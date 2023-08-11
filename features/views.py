from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    blogs = Blog.objects.all()[:3]
    slides = Slider.objects.all()
    home = HomeContent.objects.filter()[:1].get()

    context = {
        'slides':slides,
        'home':home,
        'blogs':blogs,
    }
    return render(request,'index.html',context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_obj = Contact.objects.create( name=name,email=email,contact=contact,subject=subject,message=message)
        contact_obj.save()
        return redirect('contact')
    else:
        return render(request,'contact.html')
    


def blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    blogs_page = paginator.get_page(page_number)
    context = {
        'blogs_page': blogs_page
    }
    return render(request, 'blogs.html', context)

def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        'blog': blog
    }
    return render(request, 'blog_details.html', context)
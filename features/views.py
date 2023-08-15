from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    blogs = Blog.objects.all()[:3]
    services = Service.objects.all()[:3]
    slides = Slider.objects.all()
    home = HomeContent.objects.filter()[:1].get()

    context = {
        'slides':slides,
        'home':home,
        'blogs':blogs,
        'services':services,
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
        services = Service.objects.all()

        context = {
            'services': services
        }
        return render(request,'contact.html',context)
    


def blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    blogs_page = paginator.get_page(page_number)
    services = Service.objects.all()

    context = {
        'blogs_page': blogs_page,
        'services': services

    }
    return render(request, 'blogs.html', context)

def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    services = Service.objects.all()

    context = {
        'blog': blog,
        'services': services

    }
    return render(request, 'blog_details.html', context)



def services(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services.html', context)

def service_details(request,slug):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['phone']
        message = request.POST['message']
        service = Service.objects.get(slug=slug)
        ServiceInquiry.objects.create(name=name, email=email,contact=contact, message = message, service = service.service_title)
    
    service = Service.objects.get(slug=slug)
    services = Service.objects.all()
    context = {
        'service': service,
        'services': services
    }
    return render(request, 'service_details.html', context)


def about_us(request):
    services = Service.objects.all()
    blogs = Blog.objects.all()
    home = HomeContent.objects.all()[:1].get()
    about = AboutPageContent.objects.all()[:1].get()
    context = {
        'blogs': blogs,
        'services': services,
        'home': home,
        'about': about,
    }
    return render(request, 'about_us.html', context)
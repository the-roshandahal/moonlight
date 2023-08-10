from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
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
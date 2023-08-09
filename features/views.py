from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    # testimonial = Testimonial.objects.all()
    # gallery = None
    blogs = Blog.objects.all()
    slides = Slider.objects.all()
    home = HomeContent.objects.filter()[:1].get()

    context = {
        'slides':slides,
        'home':home,
        # 'testimonial':testimonial,
        # 'gallery':gallery,
        'blogs':blogs,
    }
    return render(request,'index.html',context)
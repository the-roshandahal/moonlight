from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    blogs = Blog.objects.all()[:3]
    services = Service.objects.all().order_by('order')
    slides = Slider.objects.all()
    try:
        home = HomeContent.objects.all()[:1].get()
    except HomeContent.DoesNotExist:
        home = None


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

        context = {
        }
        return render(request,'contact.html',context)
    


def blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    blogs_page = paginator.get_page(page_number)

    context = {
        'blogs_page': blogs_page,

    }
    return render(request, 'blogs.html', context)

def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)

    context = {
        'blog': blog,

    }
    return render(request, 'blog_details.html', context)



def services(request):
    services = Service.objects.all().order_by('-order')
    company_services = CompanyService.objects.all().order_by('-order')
    try:
        service_page_data = ServicePageContent.objects.all()[:1].get()
    except ServicePageContent.DoesNotExist:
        service_page_data = None

    context = {
        'services': services,
        'service_page_data':service_page_data,
        'company_services':company_services,
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
    services = Service.objects.all().order_by('-order')
    context = {
        'service': service,
        'services': services
    }
    return render(request, 'service_details.html', context)


def about_us(request):
    blogs = Blog.objects.all()
    home = HomeContent.objects.all()[:1].get()
    
    try:
        about = AboutPageContent.objects.all()[:1].get()
    except HomeContent.DoesNotExist:
        about = None
    context = {
        'blogs': blogs,
        'home': home,
        'about': about,
    }
    return render(request, 'about_us.html', context)


















def demands(request):
    jobs= JobVacancy.objects.filter(is_active = True)
    context = {
        'jobs': jobs,
    }
    return render(request,'demands.html',context)

def job_description(request,slug):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        vacancy = JobVacancy.objects.get(slug=slug)
        JobVacancyInquiry.objects.create(name=name, email=email,phone=phone, message = message, vacancy = vacancy)
        return redirect('job_description', slug=slug)
    
    job = JobVacancy.objects.get(slug=slug)
    all_jobs = JobVacancy.objects.filter(is_active = True).exclude(slug=slug)[:3]
    context = {
        'job': job,
        'all_jobs': all_jobs
    }
    return render(request, 'job_description.html', context)






def error_404(request, exception):
    return render(request, 'error.html', status=404)


def error_500(request):
    return render(request, 'error.html', status=500)
from django.urls import path
from . import views
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static  


urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("blogs", views.blogs, name="blogs"),
    path("blog_details/<str:slug>", views.blog_details, name="blog_details"),
    path("services", views.services, name="services"),
    path("service_details/<str:slug>", views.service_details, name="service_details"),
    
    path("demands", views.demands, name="demands"),
    path("job_description/<str:slug>", views.job_description, name="job_description"),
    path("about_us", views.about_us, name="about_us"),

    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
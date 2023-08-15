from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

class CompanySetup(models.Model):
    data_set = models.CharField(max_length=200)
    color_logo = models.ImageField(upload_to="logos",verbose_name="Color Logo (170*55)")
    white_logo = models.ImageField(upload_to="logos",verbose_name="White Logo (170*55)")

    company_name = models.CharField(max_length=255)

    location = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    facebook_url = models.URLField(null=True,blank=True)
    instagram_url = models.URLField(null=True,blank=True)
    linkedin_url = models.URLField(null=True,blank=True)
    youtube_url = models.URLField(null=True,blank=True)
    
    privacy_policy = models.TextField()
    terms_and_conditions = models.TextField()

    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "01. Company Setup" 


class Slider(models.Model):
    image = models.ImageField(upload_to="slider_images",verbose_name="Image (1920*800)")
    heading_text = models.CharField(max_length=200) 
    sub_heading_text = models.CharField(max_length=200) 
    button_text = models.CharField(max_length=50)
    button_url = models.URLField()
    def __str__(self):
        return self.heading_text
    class Meta:
        verbose_name_plural = "02. Slider" 



class HomeContent(models.Model):
    data_set = models.CharField(max_length=200)

    header_heading = models.CharField(max_length=150)
    header_text = models.TextField()
    header_image = models.ImageField(upload_to="home_images/", verbose_name="Header Image (585*335)")
    header_button_text = models.CharField(max_length=100)
    header_button_url = models.URLField()

    service_title = models.CharField(max_length=255)
    service_text = models.TextField()

    bottom_title = models.CharField(max_length=150)
    bottom_sub_title = models.CharField(max_length=150)
    bottom_text = models.TextField()
    bottom_image = models.ImageField(upload_to="home_images/", verbose_name="Bottom Image (570*465)")


    years_of_experience = models.IntegerField()
    countries = models.FloatField()
    employees = models.IntegerField()
    clients = models.IntegerField()
    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "03.Home Page Content" 


class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    contact = models.TextField()
    subject = models.TextField(null=True, blank=True)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "04. Contact"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    blog = models.TextField()
    image = models.ImageField(upload_to="blogs_images/",verbose_name="Blog Image (370*270)")
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "05. Blogs" 

class Service(models.Model):
    service_title = models.CharField(max_length=200)
    service_description = models.TextField()
    service_image = models.ImageField(upload_to="Services_images/",verbose_name="Service Image (370*250)")
    slug = AutoSlugField(populate_from='service_title', unique=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.service_title
    class Meta:
        verbose_name_plural = "06. Services" 



class ServiceInquiry(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    contact = models.CharField(max_length = 255)
    message = models.CharField(max_length = 255)
    service = models.CharField(max_length = 255)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "07. Service Inquiry"



class AboutPageContent(models.Model):
    data_set = models.CharField(max_length=200)

    title = models.CharField(max_length=150)
    title_description = models.TextField()
    title_image = models.ImageField(upload_to="about_images/", null=True, blank=True)


    sub_title = models.CharField(max_length=150)
    sub_text = models.TextField()

    mission = models.TextField()
    vision = models.TextField()
    goal = models.TextField()
    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "11.About Page Content" 
















class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team_images/team')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "03. Team Members"


class Testimonial(models.Model):
    name= models.CharField(max_length=200)
    position= models.CharField(max_length=200)
    testimonial= models.TextField()
    image = models.ImageField(upload_to="testimonial_images/", blank=True, null=True)


    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "04. Testimonials"

class Faqs(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = "05. FAQs"





class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=150)
    team = models.TextField()
    order = models.IntegerField()
    image = models.ImageField(upload_to="team_images/", null=True, blank=True)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "10. team"



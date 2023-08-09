# Generated by Django 4.1.4 on 2023-08-09 13:44

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=200)),
                ('mini_title_text', models.CharField(max_length=150)),
                ('title_text', models.CharField(max_length=150)),
                ('sub_text', models.TextField()),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='home_images/')),
                ('mission', models.TextField()),
                ('vision', models.TextField()),
                ('goal', models.TextField()),
            ],
            options={
                'verbose_name_plural': '11.About Page Content',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('blog', models.TextField()),
                ('image', models.ImageField(upload_to='blogs_images/', verbose_name='Image (670*670)')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '06. Blogs',
            },
        ),
        migrations.CreateModel(
            name='CompanySetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=200)),
                ('color_logo', models.ImageField(upload_to='logos', verbose_name='Color Logo (170*55)')),
                ('white_logo', models.ImageField(upload_to='logos', verbose_name='White Logo (170*55)')),
                ('company_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('opening_hours', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('privacy_policy', models.TextField()),
                ('terms_and_conditions', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '01. Company Setup',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('contact', models.TextField()),
                ('subject', models.TextField(blank=True, null=True)),
                ('message', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '07. Contact',
            },
        ),
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '05. FAQs',
            },
        ),
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=200)),
                ('header_heading', models.CharField(max_length=150)),
                ('header_text', models.TextField()),
                ('header_image', models.ImageField(upload_to='home_images/', verbose_name='Header Image (585*335)')),
                ('header_button_text', models.CharField(max_length=100)),
                ('header_button_url', models.URLField()),
                ('service_title', models.CharField(max_length=255)),
                ('service_text', models.TextField()),
                ('bottom_title', models.CharField(max_length=150)),
                ('bottom_sub_title', models.CharField(max_length=150)),
                ('bottom_text', models.TextField()),
                ('bottom_image', models.ImageField(upload_to='home_images/', verbose_name='Header Image (585*335)')),
                ('bottom_button_text', models.CharField(max_length=100)),
                ('bottom_button_url', models.URLField()),
                ('years_of_experience', models.IntegerField()),
                ('countries', models.FloatField()),
                ('employees', models.IntegerField()),
                ('clients', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': '03.Home Page Content',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider_images', verbose_name='Image (1920*800)')),
                ('heading_text', models.CharField(max_length=200)),
                ('sub_heading_text', models.CharField(max_length=200)),
                ('button_text', models.CharField(max_length=50)),
                ('button_url', models.URLField()),
            ],
            options={
                'verbose_name_plural': '02. Slider',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=150)),
                ('team', models.TextField()),
                ('order', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='team_images/')),
            ],
            options={
                'verbose_name_plural': '10. team',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='team_images/team')),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '03. Team Members',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('testimonial', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonial_images/')),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '04. Testimonials',
            },
        ),
    ]
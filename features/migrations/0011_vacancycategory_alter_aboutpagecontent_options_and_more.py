# Generated by Django 4.1.4 on 2023-08-18 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0010_delete_faqs_delete_team_delete_teammember_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': '08. Vacancy Category',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutpagecontent',
            options={'verbose_name_plural': '03.About Page Content'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name_plural': '06. Blogs'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': '05. Contact'},
        ),
        migrations.AlterModelOptions(
            name='homecontent',
            options={'verbose_name_plural': '02.Home Page Content'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': '07. Services'},
        ),
        migrations.AlterModelOptions(
            name='serviceinquiry',
            options={'verbose_name_plural': '08. Service Inquiry'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': '04. Slider'},
        ),
        migrations.AlterField(
            model_name='aboutpagecontent',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='about_images/', verbose_name='Image (470*450)'),
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('both', 'both')], max_length=255)),
                ('openings', models.IntegerField()),
                ('job_description', models.TextField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='features.vacancycategory')),
            ],
            options={
                'verbose_name_plural': '08. Vacancy ',
            },
        ),
    ]

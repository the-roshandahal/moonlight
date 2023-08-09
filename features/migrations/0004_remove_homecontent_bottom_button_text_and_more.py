# Generated by Django 4.1.4 on 2023-08-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_remove_homecontent_cliensats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homecontent',
            name='bottom_button_text',
        ),
        migrations.RemoveField(
            model_name='homecontent',
            name='bottom_button_url',
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='bottom_image',
            field=models.ImageField(upload_to='home_images/', verbose_name='Bottom Image (570*465)'),
        ),
    ]

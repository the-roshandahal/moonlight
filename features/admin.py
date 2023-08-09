from django.contrib import admin
from.models import *
# Register your models here.
from django_summernote.models import Attachment
admin.site.unregister(Attachment)
from django.contrib.auth.models import Group
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(CompanySetup)
admin.site.register(Slider)
admin.site.register(HomeContent)
admin.site.register(Blog)
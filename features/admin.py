from django.contrib import admin
from.models import *
from django_summernote.models import Attachment
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

admin.site.unregister(Attachment)
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(CompanySetup)
admin.site.register(Slider)
admin.site.register(HomeContent)
admin.site.register(ServiceInquiry)
admin.site.register(AboutPageContent)



class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created')
    summernote_fields = ('blog',) 
admin.site.register(Blog,BlogAdmin)


class ServiceAdmin(SummernoteModelAdmin):
    list_display = ('service_title', 'created')
    summernote_fields = ('service_description',)

admin.site.register(Service,ServiceAdmin)
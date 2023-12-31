from django.contrib import admin
from.models import *
from django_summernote.models import Attachment
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

admin.site.unregister(Attachment)
admin.site.unregister(Group)
admin.site.unregister(User)


admin.site.register(ServiceInquiry)
admin.site.register(Contact)
admin.site.register(Slider)

admin.site.register(JobVacancyCategory)
admin.site.register(JobVacancyInquiry)
admin.site.register(CompanyService)

class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created')
    summernote_fields = ('blog',) 
admin.site.register(Blog,BlogAdmin)


class ServiceAdmin(SummernoteModelAdmin):
    list_display = ('service_title','order', 'created')
    summernote_fields = ('service_description',)

admin.site.register(Service,ServiceAdmin)

class VacancyAdmin(SummernoteModelAdmin):
    list_display = ('job_title','category','is_active', 'created')
    summernote_fields = ('job_description',) 
admin.site.register(JobVacancy,VacancyAdmin)


class ReadOnlyModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Disable the "Add" button
        return True
    
    def has_change_permission(self, request, obj=None):
        # Allow editing
        return True
    
    def has_delete_permission(self, request, obj=None):
        # Disable the "Delete" button
        return False
@admin.register(AboutPageContent)
class AboutPageContentAdmin(SummernoteModelAdmin, ReadOnlyModelAdmin):
    summernote_fields = ('why_us', 'title_description')

@admin.register(CompanySetup)
class CompanySetupAdmin(ReadOnlyModelAdmin):
    pass

@admin.register(HomeContent)
class HomeContentAdmin(SummernoteModelAdmin,ReadOnlyModelAdmin):
    summernote_fields = ('bottom_text','header_text')


@admin.register(ServicePageContent)
class HomeContentAdmin(SummernoteModelAdmin,ReadOnlyModelAdmin):
    summernote_fields = ('service_title','why_chose_us','get_started')

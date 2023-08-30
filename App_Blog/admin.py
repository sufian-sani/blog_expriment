from django.contrib import admin
from App_Blog.models import *
# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Likes)


# @admin.register(BlogFeedbackRange)

# class BlogFeedbackRangeInline(admin.TabularInline):
#     model = BlogFeedbackRange
# from django.contrib.admin.views.main import ChangeList
# from django.contrib.admin.util import quote
# class FooChangeList(ChangeList):
#     def url_for_result(self, result):
#         pk = getattr(result, self.pk_attname)
#         return '/foos/foo/%d/' % (quote(pk))
from django.contrib.admin.views.main import ChangeList

class CustomChangeList(ChangeList):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # import pdb;pdb.set_trace()
        queryset = queryset.filter(id=4)  # Replace with your condition
        # queryset = queryset.filter(author__name='J.K. Rowling')  # Replace with your condition
        return queryset
# Your custom implementation here
from django.urls import reverse
# from django.utils.html import format_html
# def detail_url(self, instance):
#     url = reverse('product_detail', kwargs={'pk': instance.slug})
#     response = format_html("""<a href="{0}">{0}</a>""")
#     return response
from django.http import HttpResponseRedirect
class BlogFeedbackRangeAdmin(admin.ModelAdmin):
    # actions_on_top = True
    # list_display_links = False
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def changelist_view(self, request, extra_context=None):
       object, created = WidgetAdminAdmin.get_my_object(self)
    #    import pdb;pdb.set_trace()
       url = reverse('admin:%s_%s_change' %(object._meta.app_label, object._meta.model_name),  args=[object.id] )
       return HttpResponseRedirect(url)
    
class WidgetAdminAdmin(BlogFeedbackRangeAdmin):
    def get_my_object(self):
        return BlogFeedbackRange.objects.get_or_create(id=4)
    
    
   
    # def get_changelist(self, request, **kwargs):
    #     return CustomChangeList
    
    # list_display = ['float']

    # def float(self,obj):
    #     return u'<a href="/foos/%s/">%s</a>' % (obj.float,obj)
    # float.allow_tags = True
    # float.short_description = "float"
    # def __init__(self,*args,**kwargs):
    #     super(BlogFeedbackRangeAdmin, self).__init__(*args, **kwargs)
    #     self.list_display_links = (None, )

    # def has_change_permission(self, request, obj=None):
    #     return obj is None or obj.user == request.user

    
    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['show_save_and_continue'] = False
    #     extra_context['show_save'] = False
    #     return super(BlogFeedbackRange, self).changeform_view(request, object_id, extra_context=extra_context)

admin.site.register(BlogFeedbackRange, BlogFeedbackRangeAdmin)
from django.contrib import admin
from .models import Test, Contact, Tag

# Register your models here.


class TagInline(admin.TabularInline):
    model = Tag


# 定义管理页面格式
class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'email')
    inlines = [TagInline]
    list_display = ('name', 'age', 'email')
    search_fields = ('name', )
    # fieldsets = (
    #     ['Main', {
    #         'fields': ('name', 'email'),
    #     }],
    #     ['Advance', {
    #         # CSS
    #         'classes': ('collapse', ),
    #         'fields': ('age', )
    #     }]
    # )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])

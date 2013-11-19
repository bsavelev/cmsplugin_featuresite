from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext
from django.contrib import admin

from .models import Topic, Service, Feature, Client, ClientPhoto


class BaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('slug', 'title', 'pub_date')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    save_on_top = True


class PhotoInline(admin.TabularInline):
    model = ClientPhoto
    extra = 5


class ClientAdmin(BaseAdmin):
    inlines = [PhotoInline, ]


admin.site.register(Topic, BaseAdmin)
admin.site.register(Service, BaseAdmin)
admin.site.register(Feature, BaseAdmin)
admin.site.register(Client, ClientAdmin)

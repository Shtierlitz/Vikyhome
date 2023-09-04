from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Service, Extra, Post


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'title_photo', 'price', 'price_description')
    list_display_links = ('id', 'title', 'description')

    def title_photo(self, object):
        """Функция отображения картинки в админ панели."""
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100>")


class ExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'price_description')
    list_display_links = ('id', 'title', 'price')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "text")
    list_display_links = ('id', 'title')


admin.site.register(Extra, ExtraAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Post, PostAdmin)

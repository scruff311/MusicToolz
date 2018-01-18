from django.contrib import admin

# Register your models here.
from .models import Song

# Dvieweast311D
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    ordering = ['title']
    actions = ['activate', 'deactivate']

    def activate(self, request, queryset):
        rows_updated = queryset.update(active=True)
        if rows_updated == 1:
            message_bit = "1 song was"
        else:
            message_bit = "%s songs were" % rows_updated
        self.message_user(
            request, "%s successfully marked as active." % message_bit)
    activate.short_description = "Mark selected songs as active"

    def deactivate(self, request, queryset):
        rows_updated = queryset.update(active=False)
        if rows_updated == 1:
            message_bit = "1 song was"
        else:
            message_bit = "%s songs were" % rows_updated
        self.message_user(
            request, "%s successfully marked as inactive." % message_bit)
    deactivate.short_description = "Mark selected songs as inactive"


admin.site.register(Song, SongAdmin)

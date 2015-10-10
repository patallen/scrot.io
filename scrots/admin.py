from django.contrib import admin
from .models import Website, Snapshot


class SnapshotInline(admin.StackedInline):
    model = Snapshot


class WebsiteAdmin(admin.ModelAdmin):
    inlines = (SnapshotInline,)
    list_display = ['admin_thumb', 'domain', 'create_date', 'update_date']


admin.site.register(Website, WebsiteAdmin)
admin.site.register(Snapshot)

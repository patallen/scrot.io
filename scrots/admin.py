from django.contrib import admin
from .models import Scrot, Website, Snapshot


class SnapshotInline(admin.StackedInline):
    model = Snapshot


class WebsiteAdmin(admin.ModelAdmin):
    inlines = (SnapshotInline,)


admin.site.register(Scrot)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Snapshot)

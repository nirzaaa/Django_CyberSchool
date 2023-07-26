from django.contrib import admin
from .models import Profile, Resume
from django.contrib.sessions.models import Session
from django.contrib import admin

admin.site.register(Profile)
admin.site.register(Resume)

class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)
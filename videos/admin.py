from django.contrib import admin

# Register your models here.
from embed_video.admin import AdminVideoMixin
from .models import Video


class AdminVideo(AdminVideoMixin , admin.ModelAdmin):
    pass

admin.site.register(Video , AdminVideo)
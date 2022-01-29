from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from embed_video.fields import  EmbedVideoField


class Video(models.Model):
    title = models.CharField(_("title"), max_length=250)
    added = models.DateTimeField(_("added"), auto_now_add=True)
    url =  EmbedVideoField()

    

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.title


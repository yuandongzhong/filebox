import os

from django.db import models


class TeamFile(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='teamfiles/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.file.name)

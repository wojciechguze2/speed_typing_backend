from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    url = models.URLField(null=True, blank=False)

    def repr(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url
        }

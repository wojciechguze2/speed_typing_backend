from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def repr(self):
        return {
            'id': self.id,
            'name': self.name
        }

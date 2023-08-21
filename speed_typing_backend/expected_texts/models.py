from django.db import models

from speed_typing_backend.authors.models import Author


class ExpectedText(models.Model):
    text = models.TextField(max_length=16182, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(Author, null=True, blank=False, on_delete=models.SET_NULL)

    def repr(self) -> dict:
        return {
            'id': self.id,
            'text': self.text,
            'author': self.author.repr() if self.author else None
        }

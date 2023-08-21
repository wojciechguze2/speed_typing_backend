from django.db import models

from speed_typing_backend.authors.models import Author
from speed_typing_backend.globals.models import Locale


class ExpectedText(models.Model):
    text = models.TextField(max_length=16182, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, null=True, blank=False, on_delete=models.SET_NULL)
    locale = models.ForeignKey(Locale, null=False, blank=False, default=Locale.DEFAULT_LOCALE_ID, on_delete=models.SET_DEFAULT)

    def repr(self) -> dict:
        return {
            'id': self.id,
            'text': self.text,
            'author': self.author.repr() if self.author else None,
            'locale': self.locale.repr()
        }

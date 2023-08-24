from django import forms

from speed_typing_backend.authors.models import Author
from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.globals.models import Locale


class ExpectedTextForm(forms.ModelForm):
    class Meta:
        model = ExpectedText
        fields = ['text', 'author', 'locale', 'active']

    def __init__(self, *args, **kwargs):
        super(ExpectedTextForm, self).__init__(*args, **kwargs)
        authors = Author.objects.all()
        locales = Locale.objects.all()

        self.fields['author'].queryset = authors
        self.fields['author'].widget = forms.Select(choices=[(author.id, author.name) for author in authors])

        self.fields['locale'].queryset = locales
        self.fields['locale'].widget = forms.Select(choices=[(locale.id, locale.iso) for locale in locales])

from django import forms

from speed_typing_backend.globals.models import StaticPage, Locale


class StaticPageForm(forms.ModelForm):
    class Meta:
        model = StaticPage
        fields = ['path', 'title', 'content', 'locale']

    def __init__(self, *args, **kwargs):
        super(StaticPageForm, self).__init__(*args, **kwargs)
        locales = Locale.objects.all()

        self.fields['locale'].queryset = locales
        self.fields['locale'].widget = forms.Select(choices=[(locale.id, locale.iso) for locale in locales])

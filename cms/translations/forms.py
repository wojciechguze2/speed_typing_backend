from django import forms

from speed_typing_backend.translations.models import Translation, TranslationBase


class TranslationBaseForm(forms.ModelForm):
    class Meta:
        model = TranslationBase
        fields = ['code']


class TranslationForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = ['translation']
        widgets = {
            'translation': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super(TranslationForm, self).__init__(*args, **kwargs)
        self.instance: Translation

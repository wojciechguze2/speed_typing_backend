from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Locale(models.Model):
    """
    iso codes: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    """
    POLISH_LOCALE_ID = 1
    ENGLISH_LOCALE_ID = 2
    GERMAN_LOCALE_ID = 3

    DEFAULT_LOCALE_ID = POLISH_LOCALE_ID  # polish (:
    FOREIGN_LOCALE_IDS = [
        ENGLISH_LOCALE_ID,
        GERMAN_LOCALE_ID
    ]

    AVAILABLE_LANGUAGE_IDS = [DEFAULT_LOCALE_ID] + FOREIGN_LOCALE_IDS

    AVAILABLE_LANGUAGE_CODES = [
        'pl',
        'en',
        'de'
    ]

    iso = models.CharField(null=False, blank=False, max_length=15)
    name = models.CharField(null=False, blank=False, max_length=63)

    def repr(self):
        return {
            'id': self.id,
            'iso': self.iso,
            'name': self.name
        }


class StaticPage(models.Model):
    path = models.CharField(null=False, blank=False, max_length=127)
    title = models.CharField(null=False, blank=False, max_length=127)
    content = models.TextField(null=False, blank=False, max_length=8191)
    locale = models.ForeignKey(Locale, null=False, blank=False, default=Locale.DEFAULT_LOCALE_ID,
                               on_delete=models.CASCADE)

    def repr(self):
        return {
            'id': self.id,
            'path': self.path,
            'title': self.title,
            'locale': self.locale.repr()
        }

    def repr_long(self):
        return {
            'id': self.id,
            'path': self.path,
            'title': self.title,
            'content': self.content,
            'locale': self.locale.repr()
        }


@receiver(post_save, sender=StaticPage, dispatch_uid='clear_static_page_path')
def clear_static_page_path(sender, instance: StaticPage, **kwargs):
    if instance.path.startswith('/'):
        instance.path = instance.path[1:]
        instance.save(update_fields=['path'])


class ContactMessage(models.Model):
    firstname = models.CharField(null=True, blank=True, max_length=254)
    lastname = models.CharField(null=True, blank=True, max_length=254)
    email = models.EmailField(null=False, blank=False, max_length=254)
    phone = models.CharField(null=True, blank=True, max_length=15)
    message = models.CharField(null=True, blank=True, max_length=4095)

    def __str__(self):
        return (
            f'Firstname: {self.firstname} \n'
            f'Lastname: {self.lastname} \n'
            f'E-mail: {self.email} \n'
            f'Phone number: {self.phone} \n'
            f'Message: {self.message}'
        )


@receiver(post_save, sender=ContactMessage, dispatch_uid='send_contact_message')
def send_contact_message(sender, instance: ContactMessage, created: bool, **kwargs):
    from speed_typing_backend.globals.functions import send_contact_email

    if created:
        send_contact_email(instance)

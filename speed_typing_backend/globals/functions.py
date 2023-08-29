from django.conf import settings
from django.core.mail import send_mail

from speed_typing_backend.constants import DEFAULT_EMAIL_RECIPIENT_LIST
from speed_typing_backend.globals.models import ContactMessage
from speed_typing_backend.settings import FRONTEND_DOMAIN


def format_ms_to_string(time_ms: [float, int]):
    if not time_ms:
        return 0

    milliseconds = int(time_ms % 1000)
    seconds = int((time_ms // 1000) % 60)
    minutes = int(time_ms // 1000 // 60)

    return f"{minutes}m {seconds}s {milliseconds}ms"


def send_contact_email(contact_message: ContactMessage):
    if not settings.EMAIL_ENABLED:
        return None

    send_mail(
        subject=f'{FRONTEND_DOMAIN} - Contact request',
        message=contact_message.__str__(),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=DEFAULT_EMAIL_RECIPIENT_LIST
    )

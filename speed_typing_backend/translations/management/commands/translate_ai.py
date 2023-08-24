from abc import ABC

from django.core.management import BaseCommand

from speed_typing_backend.openai_integration.integration import OpenAI


class Command(BaseCommand, ABC):
    def handle(self, *args, **kwargs):
        OpenAI().create_translations()

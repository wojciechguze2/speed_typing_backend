from abc import ABC

from django.core.management import BaseCommand

from speed_typing_backend.openai_integration.integration import OpenAI


class Command(BaseCommand, ABC):
    def handle(self, *args, **kwargs):
        try:
            count = int(input('Count (default: 2): '))
        except Exception as e:
            count = int(2)

        if not count:
            count = int(2)

        if count > 50:
            raise ResourceWarning

        OpenAI().create_expected_texts(count)

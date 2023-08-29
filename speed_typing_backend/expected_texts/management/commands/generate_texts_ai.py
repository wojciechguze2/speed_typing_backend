from abc import ABC

from django.core.management import BaseCommand

from speed_typing_backend.openai_integration.integration import OpenAI


class Command(BaseCommand, ABC):
    def handle(self, *args, **kwargs):
        try:
            count = int(input('Count (default: 2): '))
        except Exception as e:
            count = 2

        if not count:
            count = 2

        try:
            max_chars = int(input('Max chars: (default: 127): '))
        except Exception as e:
            max_chars = 127

        if not max_chars:
            max_chars = 127

        if count > 50 or max_chars > 255:
            raise ResourceWarning

        OpenAI().create_expected_texts(count, max_chars)

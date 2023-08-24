# import random

import openai
from django.db import transaction

# from speed_typing_backend.authors.models import Author
from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.globals.models import Locale
from speed_typing_backend.openai_integration.exceptions import TranslationError, OpenAIConfigurationError
from speed_typing_backend.settings import OPENAI_SECRET_KEY
from speed_typing_backend.translations.models import TranslationBase, Translation


class OpenAI:
    def __init__(self, api_key: [str, None] = None):
        self.openai: openai = openai

        if api_key:
            self.openai.api_key = api_key
        else:
            self.openai.api_key = OPENAI_SECRET_KEY

        if not self.openai.api_key:
            raise OpenAIConfigurationError

    def __translate(self, text: str, target_locale_iso: str, max_tokens=254):
        source_locale = 'polskiego'
        target_locale = None

        if target_locale_iso == 'en':
            target_locale = 'angielski'
        elif target_locale_iso == 'de':
            target_locale = 'niemiecki'

        if not target_locale:
            raise TranslationError

        if target_locale:
            prompt = f"Przetłumacz z {source_locale} na {target_locale} tekst: '{text}'"

            response = self.openai.Completion.create(
                engine='text-davinci-003',
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=0.25,
                stop=None
            )

            translation = response.choices[0].text.strip().replace('"', '').replace("'", '')

            if not translation:
                raise TranslationError

            print({
                'source': text,
                'translation': translation,
                'target_locale': target_locale
            })

            return translation

    def __get_opensource_text(self, author_name: [str, None] = None, topic: str = 'dowolna', max_chars: int = 254):
        prompt = 'Wygeneruj w języku polskim tekst'

        if author_name:
            prompt += ' autora o nazwie: %s' % author_name

        if topic:
            prompt += ' o kategorii: %s' % topic

        if max_chars:
            prompt += ' (maksymalna ilość znaków: %d)' % max_chars

        response = self.openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_chars,
            temperature=0.9,
            stop=None
        )

        text = response.choices[0].text.strip()

        if not text.endswith('.'):
            last_dot_index = text.rfind('.')

            if last_dot_index != -1:
                text = text[:last_dot_index + 1]

        print({
            'topic': topic,
            'text': text
        })

        return text

    def __translate_expected_text(self, text: ExpectedText, locale: Locale):
        return self.__translate(text.text, locale.iso)

    def create_translations(self):
        base_translations = TranslationBase.objects.filter(
            translation__locale_id=Locale.DEFAULT_LOCALE_ID,
            auto_translate_enabled=True
        )

        foreign_locales = Locale.objects.filter(
            id__in=Locale.FOREIGN_LOCALE_IDS
        )

        for base_translation in base_translations:
            default_translation = base_translation.default_translation
            locales = foreign_locales.exclude(
                id__in=list(base_translation.translation_set.values_list('locale_id', flat=True))
            )

            with transaction.atomic():
                for locale in locales:
                    translation = self.__translate(default_translation.translation, locale.iso, max_tokens=127)

                    Translation.objects.create(
                        base=base_translation,
                        locale_id=locale.id,
                        translation=translation
                    )

    def translate_expected_texts(self, expected_text_ids: [list, None] = None):
        texts_to_translate = ExpectedText.objects.filter(
            expectedtext__isnull=True,  # child not defined = texts not translated yet
            locale_id=Locale.DEFAULT_LOCALE_ID
        )

        if expected_text_ids:
            texts_to_translate = texts_to_translate.filter(
                id__in=expected_text_ids
            )

        for text_to_translate in texts_to_translate:
            with transaction.atomic():
                for locale in Locale.objects.filter(id__in=[Locale.ENGLISH_LOCALE_ID, Locale.GERMAN_LOCALE_ID]):
                    translation = self.__translate_expected_text(text_to_translate, locale)

                    ExpectedText.objects.create(
                        text=translation,
                        author=text_to_translate.author,
                        locale_id=locale.id,
                        active=True,
                        original_text=text_to_translate
                )

    def create_expected_texts(self, count=2):
        topics = [
            'literatura',
            'sztuka',
            'sztuczna inteligencja',
            'kosmos',
            'loty w kosmos',
            'czas',
            'inwestowanie czasu',
            'tworzenie stron internetowych',
            'oceany',
            'morza',
            'rzeki',
            'przyroda',
            'zwierzęta',
            'płazy',
            'ssaki',
            'natura',
            'góry',
            'jeziora',
            'kula ziemska',
            'zdrowy tryb życia',
            None
        ]
        # authors = Author.objects.all()
        author = None
        topic_index = 0

        for index in range(count):
            # author = random.choice([random.choice(authors), None])
            # author_name = author.name if author else None
            # topic = random.choice(topics)

            topic = topics[topic_index]

            text = self.__get_opensource_text(None, topic)

            if not text:
                continue

            with transaction.atomic():
                expected_text, created = ExpectedText.objects.get_or_create(
                    text=text,
                    defaults=dict(
                        author=author,
                        locale_id=Locale.DEFAULT_LOCALE_ID
                    )
                )

                if created:
                    for locale in Locale.objects.filter(id__in=[Locale.ENGLISH_LOCALE_ID, Locale.GERMAN_LOCALE_ID]):
                        translation = self.__translate_expected_text(expected_text, locale)

                        ExpectedText.objects.create(
                            text=translation,
                            author=author,
                            locale_id=locale.id,
                            active=True,
                            original_text=expected_text
                        )

            if index > len(topics):
                topic_index = 0
            else:
                topic_index += 1

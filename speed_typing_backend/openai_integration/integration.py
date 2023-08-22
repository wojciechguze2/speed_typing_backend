import openai

from speed_typing_backend.openai_integration.exceptions import TranslationError
from speed_typing_backend.settings import OPENAI_SECRET_KEY


def translate(text: str, target_locale_iso: str, max_tokens=254):
    if not OPENAI_SECRET_KEY:
        raise TranslationError

    openai.api_key = OPENAI_SECRET_KEY

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

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.25,
            stop=None
        )

        translation = response.choices[0].text.strip().replace('"', '').replace("'", '')

        if not translation:
            raise TranslationError

        """
        print('prompt:', prompt, '\n' 't:', translation)
        print()
        """

        return translation


def get_opensource_text(author_name: [str, None], topic: str = 'dowolna', max_chars: int = 254):
    if not OPENAI_SECRET_KEY:
        raise TranslationError

    openai.api_key = OPENAI_SECRET_KEY

    prompt = 'Wygeneruj w języku polskim tekst'

    """
    if author_name:
        prompt += ' autora o nazwie: %s' % author_name
    """

    if topic:
        prompt += ' o kategorii: %s' % topic

    if max_chars:
        prompt += ' (maksymalna ilość znaków: %d)' % max_chars

    response = openai.Completion.create(
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

    return text

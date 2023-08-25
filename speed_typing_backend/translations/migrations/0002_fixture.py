from django.db import migrations

from speed_typing_backend.settings import OPENAI_SECRET_KEY
from speed_typing_backend.openai_integration.integration import OpenAI
from speed_typing_backend.translations.models import TranslationBase


def single_translation_data(locale_id: int, translation: str, auto_translate_enabled: bool = True):
    return {
        'locale_id': locale_id,
        'translation': translation,
        'auto_translate_enabled': auto_translate_enabled
    }


def add_fixture(apps, schema_editor):
    from speed_typing_backend.globals.models import Locale
    from speed_typing_backend.translations.models import Translation

    init_translations_data = [
        {
            'code': 'account.edit_account',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Edytuj konto'),
                single_translation_data(Locale.ENGLISH_LOCALE_ID, 'Edit account'),
                single_translation_data(Locale.GERMAN_LOCALE_ID, 'Konto bearbeiten'),
            ]
        },
        {
            'code': 'account.delete_account',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Usuń konto'),
            ]
        },
        {
            'code': 'account.delete_account_confirm',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Czy na pewno chcesz usunąć konto?'),
            ]
        },
        {
            'code': 'account.last_login_date',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Data ostatniego logowania'),
            ]
        },
        {
            'code': 'account.join_date',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Data dołączenia'),
            ]
        },
        {
            'code': 'account.last_game_mode',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Ostatni rozegrany tryb gry'),
            ]
        },
        {
            'code': 'contact.contact_form',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Formularz kontaktowy'),
            ]
        },
        {
            'code': 'contact.firstname',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Imię'),
            ]
        },
        {
            'code': 'contact.lastname',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Nazwisko'),
            ]
        },
        {
            'code': 'contact.phone_number',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Numer telefonu'),
            ]
        },
        {
            'code': 'messages.message',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Wiadomość'),
            ]
        },
        {
            'code': 'messages.send',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Wyślij'),
            ]
        },
        {
            'code': 'homepage.content_1.header',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Rozwijaj swoje umiejętności, sprawdzaj się i analizuj statystyki!'),
            ]
        },
        {
            'code': 'homepage.content_2.header',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Dlaczego ćwiczenie szybkiego pisania jest ważne'),
            ]
        },
        {
            'code': 'homepage.content_2.content',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Szybkie i dokładne pisanie na klawiaturze to umiejętność, która ma ogromne znaczenie w dzisiejszym cyfrowym świecie. <br>Efektywne posługiwanie się klawiaturą zwiększa wydajność pracy, oszczędza czas i pomaga w komunikacji online.'),
            ]
        },
        {
            'code': 'homepage.content_3.header',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Jeśli masz pytania, sugestie, chcesz się ze mną skontaktować, nie wahaj się do mnie napisać.'),
            ]
        },
        {
            'code': 'homepage.content_3.content',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zapraszam do kontaktu!'),
            ]
        },
        {
            'code': 'homepage.content_3.button_text',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Przejdź do formularza kontaktowego'),
            ]
        },
        {
            'code': 'login.login',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Logowanie'),
            ]
        },
        {
            'code': 'login.login',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Logowanie'),
            ]
        },
        {
            'code': 'messages.close',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zamknij'),
            ]
        },
        {
            'code': 'messages.email',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'E-mail'),
            ]
        },
        {
            'code': 'messages.password',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Hasło'),
            ]
        },
        {
            'code': 'login.no_account',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Nie posiadasz konta?'),
            ]
        },
        {
            'code': 'messages.login',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zaloguj się'),
            ]
        },
        {
            'code': 'messages.register',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zarejestruj się'),
            ]
        },
        {
            'code': 'register.already_have_an_account',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Posiadasz już konto?'),
            ]
        },
        {
            'code': 'login.no_password',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zapomniałeś hasła?'),
            ]
        },
        {
            'code': 'login.remind',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Przypomnij!'),
            ]
        },
        {
            'code': 'register.need_admin_accept',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Po utworzeniu konta konieczne będzie zatwierdzenie przez administratora.'),
            ]
        },
        {
            'code': 'account.new_email',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Nowy e-mail'),
            ]
        },
        {
            'code': 'account.new_password',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Nowe hasło'),
            ]
        },
        {
            'code': 'messages.cancel',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Anuluj'),
            ]
        },
        {
            'code': 'messages.confirm',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Potwierdź'),
            ]
        },
        {
            'code': 'messages.save',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zapisz'),
            ]
        },
        {
            'code': 'messages.logout',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Wyloguj się'),
            ]
        },
        {
            'code': 'messages.restart',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Restartuj'),
            ]
        },
        {
            'code': 'account.tabs.data',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Dane'),
            ]
        },
        {
            'code': 'account.tabs.games_history',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Historia gier'),
            ]
        },
        {
            'code': 'account.tabs.statistics',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Statystyki'),
            ]
        },
        {
            'code': 'account.tabs.statistics',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Statystyki'),
            ]
        },
        {
            'code': 'game.input_length',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Ilość wprowadzonych znaków'),
            ]
        },
        {
            'code': 'game.mistakes_count',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Ilość błędów'),
            ]
        },
        {
            'code': 'game.time',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Czas'),
            ]
        },
        {
            'code': 'messages.cpm',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'CPM'),
            ]
        },
        {
            'code': 'homepage.cards.card_1.body',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Strona oferuje ćwiczenia w trzech językach: polskim, angielskim i niemieckim.'),
            ]
        },
        {
            'code': 'homepage.cards.card_1.footer',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zmień język'),
            ]
        },
        {
            'code': 'messages.change_language',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zmień język'),
            ]
        },
        {
            'code': 'homepage.cards.card_2.body',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Rozbudowana baza tekstów do ćwiczeń pozwala sprawdzić się w różnorodnych kontekstach.'),
            ]
        },
        {
            'code': 'homepage.cards.card_2.footer',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Przejdź do listy tekstów'),
            ]
        },
        {
            'code': 'homepage.cards.card_3.body',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Dzięki rozbudowanym statystykom możesz śledzić postępy oraz analizować wyniki.'),
            ]
        },
        {
            'code': 'homepage.cards.card_3.footer_not_authenticated',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zaloguj się, aby zobaczyć swoje statystki'),
            ]
        },
        {
            'code': 'homepage.cards.card_3.footer',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zobacz swoje statystki'),
            ]
        },
        {
            'code': 'homepage.special.expected_output',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Lorem ipsum dolor sit amet, consectetur adipisci tempor incidunt ut labore et dolore magna aliqua veniam, quis nostrud exercitation ullamcorpor s commodo consequat. Duis autem vel eum irrure esse molestiae consequat...', auto_translate_enabled=False),
            ]
        },
        {
            'code': 'messages.loading',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Ładowanie...'),
            ]
        },
        {
            'code': 'login.special.message',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Efektywność, Wydajność, Sukces.'),
            ]
        },
        {
            'code': 'login.special.additional_message',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Pamiętaj o silnym haśle!'),
            ]
        },
        {
            'code': 'messages.information',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Informacje'),
            ]
        },
        {
            'code': 'messages.regulations',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Regulamin'),
            ]
        },
        {
            'code': 'messages.privacy_policy',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Polityka prywatności'),
            ]
        },
        {
            'code': 'messages.sitemap',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Mapa strony'),
            ]
        },
        {
            'code': 'messages.most_popular_game_modes',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Najpopularniejsze tryby gry'),
            ]
        },
        {
            'code': 'messages.newest_game_modes',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Najnowsze tryby gry'),
            ]
        },
        {
            'code': 'game.click_to_start',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Kliknij aby rozpocząć'),
            ]
        },
        {
            'code': 'game.click_to_start',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Kliknij aby rozpocząć'),
            ]
        },
        {
            'code': 'game_mode.fast-game',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Szybka gra'),
            ]
        },
        {
            'code': 'messages.game_modes',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Tryby gry'),
            ]
        },
        {
            'code': 'messages.texts_list',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Lista tekstów'),
            ]
        },
        {
            'code': 'texts.text',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Tekst'),
            ]
        },
        {
            'code': 'messages.author',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Autor'),
            ]
        },
        {
            'code': 'messages.language',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Język'),
            ]
        },
        {
            'code': 'messages.about_site',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'O stronie'),
            ]
        },
        {
            'code': 'messages.contact',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Kontakt'),
            ]
        },
        {
            'code': 'about.used_technologies',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Wykorzystane technologie'),
            ]
        },
        {
            'code': 'about.my_first_project',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'to mój pierwszy większy projekt osobisty, na który w końcu znalazłem czas.'),
            ]
        },
        {
            'code': 'about.execution_time',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Cały proces tworzenia zajął mi około tygodnia.'),
            ]
        },
        {
            'code': 'about.site_goal',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Głównym celem tej strony jest pomoc użytkownikom w ćwiczeniu i doskonaleniu umiejętności szybkiego pisania na klawiaturze.'),
            ]
        },
        {
            'code': 'about.more_projects.before_link',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Więcej moich projektów będziesz mógł/mogła ujrzeć na moim '),
            ]
        },
        {
            'code': 'about.more_projects.after_link',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Githubie już wkrótce :)'),
            ]
        },
        {
            'code': 'messages.game_mode',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Tryb gry'),
            ]
        },
        {
            'code': 'messages.site',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Strona'),
            ]
        },
        {
            'code': 'messages.date',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Data'),
            ]
        },
        {
            'code': 'game.text_length',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Długość tekstu'),
            ]
        },
        {
            'code': 'account.history.no_games_found',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Jeszcze nie rozegrałeś żadnej gry.'),
            ]
        },
        {
            'code': 'account.statistics.last_cpm',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Ostatni CPM'),
            ]
        },
        {
            'code': 'account.statistics.average_cpm',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Średni CPM'),
            ]
        },
        {
            'code': 'account.statistics.best_cpm',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Najlepszy CPM'),
            ]
        },
        {
            'code': 'account.statistics.games_played_count',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Ilość rozegranych gier'),
            ]
        },
        {
            'code': 'account.statistics.favourite_game_mode',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Ulubiony tryb gry'),
            ]
        },
        {
            'code': 'alert.load_data_error.title',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Błąd'),
            ]
        },
        {
            'code': 'alert.load_data_error.message',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Wystąpił błąd przy pobieraniu danych. Proszę o kontakt.'),
            ]
        },
        {
            'code': 'alert.save_game_success.title',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zapis'),
            ]
        },
        {
            'code': 'alert.save_game_success.message',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zapisano grę w historii'),
            ]
        },
        {
            'code': 'alert.save_game.not_authenticated.title',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Nie zapisano gry'),
            ]
        },
        {
            'code': 'alert.save_game.not_authenticated.message',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Zaloguj się aby gry były zapisywanie do historii'),
            ]
        },
        {
            'code': 'alert.email_validation_error.title',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Niepoprawny adres E-mail'),
            ]
        },
        {
            'code': 'alert.success.message',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Wykonano operację pomyślnie'),
            ]
        },
        {
            'code': 'messages.login_error',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Nie znaleziono użytkownika.'),
            ]
        },
        {
            'code': 'messages.user_inactive',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Użytkownik jest nieaktywny.'),
            ]
        },
        {
            'code': 'register.error_message',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Wystąpiły błędy przy tworzeniu konta. Prosimy o kontakt.'),
            ]
        },
        {
            'code': 'messages.user_already_exists',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Podany użytkownik już istnieje.'),
            ]
        },
        {
            'code': 'game_mode.long-text',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Długi tekst'),
            ]
        },
        {
            'code': 'game_mode.time-limit',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Limit czasu'),
            ]
        },
        {
            'code': 'game_mode.by-one-letter',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Po jednej literze'),
            ]
        },
        {
            'code': 'game_mode.by-one-word',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Po jednym wyrazie'),
            ]
        },
        {
            'code': 'game_mode.multilanguage',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Wiele języków'),
            ]
        },
        {
            'code': 'game_mode.random',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Losowy tryb gry'),
            ]
        },
        {
            'code': 'game.remain_time',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Pozostały czas'),
            ]
        },
        {
            'code': 'game.time_limit',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Limit czasu'),
            ]
        },
        {
            'code': 'messages.remind_password',
            'translations': [
                single_translation_data(Locale.POLISH_LOCALE_ID, 'Przypomnij hasło'),
            ]
        },
    ]

    for translation_data in init_translations_data:
        code = translation_data['code']

        translation_base, _ = TranslationBase.objects.get_or_create(
            code=code
        )

        for translation_locale_data in translation_data['translations']:
            locale_id = translation_locale_data['locale_id']
            translation = translation_locale_data['translation']

            Translation.objects.get_or_create(
                base=translation_base,
                locale_id=locale_id,
                defaults=dict(
                    translation=translation
                )
            )

    if OPENAI_SECRET_KEY:
        OpenAI().create_translations()
        assert (
                Translation.objects.filter(locale_id=Locale.DEFAULT_LOCALE_ID) .count()
                == Translation.objects.filter(locale_id=Locale.ENGLISH_LOCALE_ID).count()
                == Translation.objects.filter(locale_id=Locale.GERMAN_LOCALE_ID).count()
        )


class Migration(migrations.Migration):
    dependencies = [
        ('translations', '0001_initial'),
        ('globals', '0002_fixture'),
    ]

    operations = [
        migrations.RunPython(add_fixture)
    ]

from django.db import migrations


def create_locales(apps):
    locale_model = apps.get_model('globals', 'Locale')

    locale_model.objects.get_or_create(
        id=1,
        iso='pl',
        defaults=dict(
            name='polski'
        )
    )

    locale_model.objects.get_or_create(
        id=2,
        iso='en',
        defaults=dict(
            name='english'
        )
    )

    locale_model.objects.get_or_create(
        id=3,
        iso='de',
        defaults=dict(
            name='german'
        )
    )


def create_texts(apps):
    from speed_typing_backend.globals.models import Locale
    from speed_typing_backend.expected_texts.models import ExpectedText

    authors_model = apps.get_model('authors', 'Author')
    expected_texts_model: ExpectedText = apps.get_model('expected_texts', 'ExpectedText')
    shakespeare_id = authors_model.objects.get(name='William Shakespeare').id

    expected_texts_model.objects.get_or_create(
        text='Opanowanie sztuki szybkiego pisania na klawiaturze to umiejętność, która może znacząco zwiększyć Twoją produktywność i efektywność podczas pracy na komputerze. Bez względu na to, czy jesteś programistą, pisarzem, studentem czy profesjonalistą pracującym w biurze, umiejętność szybkiego i precyzyjnego pisania może Cię wyróżnić i zaoszczędzić dużo czasu.',
        locale_id=Locale.DEFAULT_LOCALE_ID
    )

    expected_texts_model.objects.get_or_create(
        text='Cały świat to scena, a wszyscy mężczyźni i kobiety to tylko aktorzy. Mają swoje wejścia i wyjścia, a jeden mężczyzna w swoim czasie gra wiele ról, zdarza się, że jego akt to siedem wieków. I tak przed naszymi oczami spektakl ma swój bieg, a każdy w swoim czasie wchodzi na scenę i znika.',
        locale_id=Locale.DEFAULT_LOCALE_ID,
        author_id=shakespeare_id
    )

    expected_texts_model.objects.get_or_create(
        text="All the world's a stage, and all the men and women merely players. They have their exits and their entrances, and one man in his time plays many parts, his acts being seven ages. At first, the infant, mewling and puking in the nurse's arms.",
        locale_id=Locale.ENGLISH_LOCALE_ID,
        author_id=shakespeare_id
    )

    expected_texts_model.objects.get_or_create(
        text="Die ganze Welt ist eine Bühne, und alle Männer und Frauen sind bloße Spieler. Sie haben ihre Abgänge und ihre Auftritte, und ein Mann spielt zu seiner Zeit viele Rollen, seine Akte sind sieben Zeitalter. Zuerst das Kind, das in den Armen der Amme quengelt und sich übergibt.",
        locale_id=Locale.GERMAN_LOCALE_ID,
        author_id=shakespeare_id
    )

    expected_texts_model.objects.get_or_create(
        text="Zarówno w biurze, jak i w pracy zdalnej, umiejętność szybkiego pisania to atut nie do przecenienia.",
        locale_id=Locale.DEFAULT_LOCALE_ID
    )


def add_fixture(apps, schema_editor):
    create_locales(apps)
    create_texts(apps)


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0001_initial'),
        ('users', '0001_initial'),
        ('authors', '0003_author_url'),
        ('expected_texts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_fixture)
    ]

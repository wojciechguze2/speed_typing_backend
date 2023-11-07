# speed_typing_backend

## Typing speed test - backend

Backend strony został napisany w języku [Python3](https://www.python.org/) z wykorzystaniem m.in. Frameworka [Django](https://www.djangoproject.com/) oraz bazy danych [PostgreSQL](https://www.postgresql.org/).

CMS nie został dokończony - brakuje m.in. stylowania templatek, edycji niektórych rzeczy.

Na dzień dzisiejszy (01.09.2023) nie planuję, przynajmniej w najbliższej przyszłości, rozwijać tego projektu. Ewentualnie jeśli znajdę czas to dokończę CMS.

Frontend: [speed_typing](https://github.com/wojciechguze2/speed_typing)

### Development
1. Check settings.py and add necessary environment variables on your machine

2. Go to main project directory (where you can find manage.py)

3. Install requirements
```
python -m pip install -r requirements.txt
```

4. Run migrations
```
python manage.py migrate
```

5. Run server
```
python manage.py runserver
```

### OpenAI integration
1. Add OPENAI_SECRET_KEY to your env variables, f.e.:
```
export OPENAI_SECRET_KEY='<here put your secret key>'
```
2. Text generator:
```
python manage.py generate_texts_ai
```
3. Automatically translate missing translations:
```
python manage.py translate_ai
```

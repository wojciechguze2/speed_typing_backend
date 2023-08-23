from speed_typing_backend.settings import *
SECRET_KEY = 'o-secure-s_ow9-%qw9gr)-h8$_v@h@w2*f9)0qykw681)0&(a3yay!x'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'speed_typing',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

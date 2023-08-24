from django.urls import path, include

urlpatterns = [
    path('', include('cms.expected_texts.urls')),
    path('', include('cms.game_modes.urls')),
    path('', include('cms.static_pages.urls')),
    path('', include('cms.translations.urls')),
    path('', include('cms.security.urls')),
    path('', include('cms.globals.urls')),
]

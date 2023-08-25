from dataclasses import dataclass

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Count, Avg

from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.game_modes.models import GameMode
from speed_typing_backend.globals.models import Locale


class CustomUser(AbstractUser):
    locale = models.ForeignKey(Locale, null=False, blank=False, default=Locale.DEFAULT_LOCALE_ID,
                               on_delete=models.SET_DEFAULT)

    class Meta:
        app_label = 'users'


@dataclass
class UserStatistics:
    def __init__(self, user: CustomUser):
        self.user = user

    @property
    def has_games(self):
        return self.user.game_set.exists()

    @property
    def last_cpm(self):
        if not self.has_games:
            return None

        return round(float(self.user.game_set.order_by('-create_date').first().cpm), 2)

    @property
    def average_cpm(self):
        if not self.has_games:
            return None

        return round(float(self.user.game_set.aggregate(Avg('cpm'))['cpm__avg']), 2)

    @property
    def best_cpm(self):
        if not self.has_games:
            return None

        return round(float(self.user.game_set.order_by('-cpm').first().cpm), 2)

    @property
    def games_played_count(self):
        if not self.has_games:
            return 0

        return self.user.game_set.count()

    @property
    def favorite_game_mode_code(self):
        if not self.has_games:
            return None

        favorite_game = self.user.game_set.values('game_mode__code').annotate(
            total_games=Count('game_mode')
        ).order_by('-total_games').first()

        if favorite_game:
            return favorite_game['game_mode__code']

        return None

    def repr(self):
        return {
            'lastCpm': self.last_cpm,
            'averageCpm': self.average_cpm,
            'bestCpm': self.best_cpm,
            'gamesPlayedCount': self.games_played_count,
            'favoriteGameModeCode': self.favorite_game_mode_code,
        }

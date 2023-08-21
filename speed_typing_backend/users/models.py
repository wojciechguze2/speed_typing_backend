from dataclasses import dataclass

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, Avg

from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.game_modes.models import GameMode


@dataclass
class UserStatistics:
    def __init__(self, user: User):
        self.user = user

    def has_games(self):
        return self.user.usergame_set.exists()

    @property
    def last_cpm(self):
        if not self.has_games:
            return None

        return self.user.usergame_set.order_by('-create_date').first().cpm

    @property
    def average_cpm(self):
        if not self.has_games:
            return None

        return self.user.usergame_set.aggregate(Avg('cpm'))['cpm__avg']

    @property
    def best_cpm(self):
        if not self.has_games:
            return None

        return self.user.usergame_set.order_by('-cpm').first().cpm

    @property
    def games_played_count(self):
        if not self.has_games:
            return 0

        return self.user.usergame_set.count()

    @property
    def favorite_game_mode_code(self):
        if not self.has_games:
            return None

        favorite_game = self.user.usergame_set.values('game_mode__code').annotate(
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


class UserGame(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    expected_text = models.ForeignKey(ExpectedText, null=False, blank=False, on_delete=models.CASCADE)
    game_mode = models.ForeignKey(GameMode, null=False, blank=False, on_delete=models.CASCADE)
    cpm = models.DecimalField(null=True, blank=False, max_digits=13, decimal_places=4)
    time_ms = models.DecimalField(null=True, blank=False, max_digits=13, decimal_places=4)
    create_date = models.DateTimeField(auto_now_add=True)

    def repr(self):
        return {
            'expectedTextId': self.expected_text_id,
            'gameModeCode': self.game_mode.code,
            'cpm': self.cpm,
            'timeMs': self.time_ms,
            'createDate': self.create_date
        }

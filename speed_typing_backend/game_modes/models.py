from django.db import models

from speed_typing_backend.expected_texts.models import ExpectedText


class GameModeType(models.Model):
    GAME_MODE_TYPE_TEXT_LENGTH = 'text-length'
    GAME_MODE_TYPE_TIME = 'time'

    code = models.CharField(max_length=31, null=False, blank=False)

    def repr(self):
        return {
            'id': self.id,
            'code': self.code,
        }


class GameMode(models.Model):
    GAME_MODE_FAST_GAME_CODE = 'fast-game'
    GAME_MODE_LONG_TEXT_CODE = 'long-text'
    GAME_MODE_TIME_LIMIT_CODE = 'time-limit'
    GAME_MODE_BY_ONE_LETTER_CODE = 'by-one-letter'
    GAME_MODE_BY_ONE_WORD_CODE = 'by-one-word'
    GAME_MODE_MULTILANGUAGE = 'multilanguage'
    GAME_MODE_RANDOM = 'random'  # do not save it to db

    code = models.CharField(max_length=255, null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=False)
    text_assignment = models.BooleanField(default=False, null=False, blank=False)
    multilanguage = models.BooleanField(default=False, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def repr(self):
        return {
            'id': self.id,
            'code': self.code,
            'typeCodes': [
                game_mode_type_relation.game_mode_type.code
                for game_mode_type_relation in self.gamemodegamemodetype_set.all()
            ]
        }


class GameModeGameModeType(models.Model):
    game_mode = models.ForeignKey(GameMode, null=False, blank=False, on_delete=models.CASCADE)
    game_mode_type = models.ForeignKey(GameModeType, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('game_mode', 'game_mode_type')


class GameModeDefaultTimeLimits(models.Model):
    DEFAULT_TIME_LIMITS = [
        20,
        25,
        40,
        120,
        180,
    ]

    time_limit_seconds = models.IntegerField(null=False, blank=False)
    max_chars = models.IntegerField(null=False, blank=False)

    class Meta:
        unique_together = ('time_limit_seconds', 'max_chars')


class GameModeExpectedText(models.Model):
    game_mode = models.ForeignKey(GameMode, null=False, blank=False, on_delete=models.CASCADE)
    expected_text = models.ForeignKey(ExpectedText, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('game_mode', 'expected_text')

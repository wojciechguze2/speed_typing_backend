from django.db import models

from speed_typing_backend.expected_texts.models import ExpectedText
from speed_typing_backend.game_modes.models import GameMode
from speed_typing_backend.globals.functions import format_ms_to_string
from speed_typing_backend.users.models import CustomUser


class Game(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=False, on_delete=models.SET_NULL)
    expected_text = models.ForeignKey(ExpectedText, null=False, blank=False, on_delete=models.CASCADE)
    game_mode = models.ForeignKey(GameMode, null=False, blank=False, on_delete=models.CASCADE)
    cpm = models.DecimalField(null=True, blank=False, max_digits=13, decimal_places=4)
    time_ms = models.DecimalField(null=True, blank=False, max_digits=13, decimal_places=4)
    mistakes_count = models.IntegerField(null=False, blank=False, default=0)
    create_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def repr(self):
        return {
            'id': self.id,
            'gameModeCode': self.game_mode.code,
            'cpm': self.cpm,
            'mistakesCount': self.mistakes_count,
            'timeMs': format_ms_to_string(self.time_ms),
            'createDate': self.create_date.strftime('%Y-%m-%d %H:%M:%S'),
            'expectedTextId': self.expected_text_id,
            'expectedTextLength': self.expected_text.length
        }

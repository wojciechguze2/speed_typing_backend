from speed_typing_backend.game_modes.models import GameMode


def get_random_game_mode():
    return GameMode.objects.filter(active=True).exclude(code=GameMode.GAME_MODE_RANDOM).order_by('?').first()

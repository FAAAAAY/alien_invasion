import json

class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        try:
            with open('record.json') as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0
    
    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def record(self):
        """Записывает новый рекорд в файл"""
        with open('record.json', 'w') as f:
            json.dump(self.high_score, f)

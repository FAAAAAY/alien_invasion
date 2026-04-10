class Settings():
    """Класс для хранения всех настроек игры Ailen Invasion"""

    def __init__(self):
        """Инициализирует статические настройки игры"""

        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        self.bullet_width = 4
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.2
        self.score_scale = 1.5
    
    def initialize_dynamic_settings(self):
        """Инициализирует динамические настройки игры"""      
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.7
        self.alien_points = 50

        self.fleet_direction = 1  

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale*self.alien_points)
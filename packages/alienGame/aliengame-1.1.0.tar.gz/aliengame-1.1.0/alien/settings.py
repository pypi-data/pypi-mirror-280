class Settings():
    """
    存储《外星人入侵》的所有设置的类
    """
    def __init__(self):
        """
        初始化游戏的设置
        """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置

        self.ship_limit = 3

        # 子弹的参数设置

        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        # 子弹状态
        self.bullet_sta = False

        # 外星人的设置
        self.fleet_drop_speed = 10

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        初始化随游戏进行而变化的设置
        :return:
        """
        # 飞船的速度
        self.ship_speed_factor = 1.5
        # 子弹的速度
        self.bullet_speed_factor = 3
        # 外星人的速度
        self.alien_speed_factor = 1
        # 设置方向
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """
        提高速度设置
        :return:
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

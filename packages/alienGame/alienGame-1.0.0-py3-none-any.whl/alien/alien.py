import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """
    表示单个外星人的类
    """
    def __init__(self, ai_settings, screen):
        """
        初始化外星人并设置其起始位置
        :param ai_setting:
        :param screen:
        """
        super().__init__()
        self.screen = screen
        self.ai_settings =ai_settings

        # 加载外星人的图像，并设置其rect属性
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # 将外星人最初都放置在屏幕左上角位置
        # 将外星人的边距x,y设置成对应的宽高?然后在临近左上角位置?
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """
        在指定的位置创建外星人
        :return:
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        向左或者向右移动外星人
        :return:
        """
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """
        如果外星人位于屏幕边缘，就返回True
        :return:
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
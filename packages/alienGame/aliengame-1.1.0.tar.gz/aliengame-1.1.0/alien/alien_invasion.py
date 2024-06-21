import pygame
import game_fuctions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()

    # 定义一个Settings类的对象ai_setting
    ai_settings = Settings()

    # 绘制一个荧屏 并起名为Alien Invasion
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(("Alien Invasion"))

    # 创建一个飞船类
    ship = Ship(ai_settings, screen)

    # 创建一个Group，用来存子弹
    bullets = Group()
    # 创建一个Group，用来存外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 开始游戏的主循环
    while True:
        # 事件处理函数，飞船移动、子弹绘制
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 飞船移动
            ship.update()

            # 移动所有子弹
            bullets.update()

            # 移动外星人
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

            # 删除已经消失的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # 绘制屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
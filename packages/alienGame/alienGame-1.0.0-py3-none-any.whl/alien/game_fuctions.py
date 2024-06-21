# -*- coding: utf-8 -*-
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

# 绘制屏幕的函数
def update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button):
    """
    更新屏幕上的图像，并切换到新屏幕
    :param ai_settings:
    :param screen:
    :param ship:
    :return:
    """
    # 绘制颜色
    screen.fill(ai_setting.bg_color)
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    aliens.draw(screen)
    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    # 显示得分
    sb.show_score()
    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 刷新荧屏
    pygame.display.flip()

# 事件处理的函数
def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """
    响应按键和鼠标事件
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 如果是down 移动飞船 标志True
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, screen, event, ship, bullets)
        # 如果是up 停止飞船 标志False
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """
    在玩家单机Play按钮时开始游戏
    :param stats:
    :param play_button:
    :param mouse_x:
    :param mouse_y:
    :return:
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏速度
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏信息
        stats.reset_stats()
        stats.game_active = True

        # 重置计分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

# 按下事件函数
def check_keydown_events(ai_settings, screen, event, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 让子弹有一个状态
        new_bullet = Bullet(ai_settings, screen, ship)
        # 加入到bullets中去
        bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit(0)

# 松开事件函数
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

# 子弹
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 调用相应外星人和子弹碰撞的函数
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 检查是否有子弹击中外星人，如果是这样，删除相应的外星人和子弹
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 删除现有的子弹并创建一群外星人
        bullets.empty()
        ai_settings.increase_speed()

        # 提高等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

# 外星人
def create_fleet(ai_settings, screen, ship, aliens):
    """
    创建外星人群
    :param ai_setting:
    :param screen:
    :param aliens:
    :return:
    """
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人的宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)

    # 创建外星人
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """
    计算可容纳多少行外星人
    :param ai_settings:
    :param ship_height:
    :param alien_height:
    :return:
    """
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并将其加入当行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """
    更新外星人群中所有外星人的位置
    :param aliens:
    :return:
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """
    有外星人到大边缘时采取相应的措施
    :param ai_settings:
    :param aliens:
    :return:
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """
    将整群外星人下移，并改变方向
    :param ai_settings:
    :param aliens:
    :return:
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

# 飞船
def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """
    响应被外星人撞到的飞船
    :param ai_settings:
    :param stats:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return:
    """
    if stats.ships_left > 0:
        # 飞船数减1
        stats.ships_left -= 1
        # 更新计分牌
        sb.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """
    检查是否有外星人到达了屏幕底端
    :param ai_settings:
    :param stats:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return:
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 飞船到达底端
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """
    检查是否诞生了新的最高分
    :param stats:
    :param sb:
    :return:
    """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

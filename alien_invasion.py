#import sys

import pygame

from settings import Settings

from ship import Ship

from game_functions import game_functions as gf

def run_game(): 
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    
    ai_settings = Settings() 
    
    #screen = pygame.display.set_mode(1200,800)
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")
    
    #创建一艘飞船
    #ship = Ship(screen)
    ship = Ship(ai_settings,screen)

    #设置背景色
    bg_color = (230,230,230)
    
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
       # for event in pygame.event.get():
       #     if event.type == pygame.QUIT:
       #         sys.exit()
        
        gf.check_events(ship)


        # 每次循环时都重绘屏幕        
        #screen.fill(bg_color) #
        #screen.fill(ai_settings.bg_color)         
        
        #ship.blitme()

        # 让最近绘制的屏幕可见
        #pygame.display.flip()

        ship.update()
        gf.update_screen(ai_settings,screen,ship)
        
run_game()
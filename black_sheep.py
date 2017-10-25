
import pygame, os, ctypes

from pygame.sprite import Group
from sheep import Sheep
from settings import Settings
from game_stats import GameStats
import game_functions as gf

def run_game():
    # Inicializa pygame, screen, e settings.
    pygame.init()
    pygame.display.set_caption("Black Sheep")

    user32 = ctypes.windll.user32
    screenSize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    screen = pygame.display.set_mode((screenSize), pygame.FULLSCREEN)

    settings = Settings(screenSize)

    # Cria uma instância do GameStats para armazenas as estatísticas do jogo.
    stats = GameStats()

    # Inicia a ovelha preta.
    black_sheep = Sheep(screen, settings, "black")

    # Inicia as ovelhas brancas.  
    white_sheeps = Group()
    gf.create_white_sheeps(screen, settings, stats, white_sheeps)

    while True:
        # Verifica evento do Mouse e Teclado.
        gf.check_keydown_events(stats, black_sheep, white_sheeps)

        # Carrega o menu
        if stats.game_active == "menu":
            font = pygame.font.SysFont(None, 128)
            title = font.render('Black Sheep', True, settings.font_color)

            screen.fill(settings.bg_color)
            screen.blit(title, [screen.get_rect().right - (title.get_size()[0] + screenSize[0] / 20),
                                screen.get_rect().centery / 2 - (title.get_size()[1] / 2)])

            gf.button(screen, settings, stats, screenSize)

        # Movimenta as ovelhas.
        elif stats.game_active == "move":
            # Verifica e incrementa o tempo.
            gf.check_time(stats, black_sheep)

            black_sheep.update(settings)
            white_sheeps.update(settings)

            font = pygame.font.SysFont(None, 42)
            text = font.render(('Level  ' + str(stats.level)), True, settings.font_color)

            screen.fill(settings.bg_color)
            screen.blit(text, [10, 10])
            black_sheep.blitme()
            white_sheeps.draw(screen)

        # Carrega procima fase.
        elif stats.game_active == "next":
            black_sheep.loadColorSheep("black")
            black_sheep.blitme()
            gf.draw_box(screen, settings, screenSize, "Acertou")
            pygame.display.flip()
            gf.next_stage(screen, settings, stats, black_sheep, white_sheeps)

        # Reinicia o jogo
        elif stats.game_active == "reset":
            black_sheep.loadColorSheep("black")
            black_sheep.blitme()
            gf.draw_box(screen, settings, screenSize, "Perdeu")
            pygame.display.flip()
            gf.reset_stage(screen, settings, stats, black_sheep, white_sheeps)

        # Redesenha a tela.
        pygame.display.flip()


run_game()

import pygame, sys

from time import sleep

from sheep import Sheep


# Verifica eventos do Mouse e Teclado.
def check_keydown_events(stats, black_sheep, white_sheeps):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if stats.game_active == 'move':
                    stats.game_active = 'menu'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if stats.game_active == "pause":
                check_click(event.pos, stats, black_sheep, white_sheeps)


# Verifica e incrementa o tempo.           
def check_time(stats, black_sheep):
    if stats.time > 200 and stats.game_active == "move":
        stats.game_active = "pause"
    else:
        if stats.time > 50 and stats.time < 50.5:
            black_sheep.loadColorSheep("white")
        stats.time += 0.1


        # Verifica a posição do click do mouse.


def check_click(pos, stats, black_sheep, white_sheeps):
    if (pos[0] < black_sheep.rect.right and
                pos[0] > black_sheep.rect.left and
                pos[1] > black_sheep.rect.top and
                pos[1] < black_sheep.rect.bottom):
        stats.game_active = "next"
    else:
        for sheep in white_sheeps:
            if (pos[0] < sheep.rect.right and
                        pos[0] > sheep.rect.left and
                        pos[1] > sheep.rect.top and
                        pos[1] < sheep.rect.bottom):
                stats.game_active = "reset"


# Carrega o proximo nivel.
def next_stage(screen, settings, stats, black_sheep, white_sheeps):
    stats.level += 1
    stats.time = 0.1
    settings.sheep_speed += 0.3

    load_level(screen, settings, stats, black_sheep, white_sheeps)

    stats.game_active = "move"


# Reinicia o Jogo.
def reset_stage(screen, settings, stats, black_sheep, white_sheeps):
    stats.level = 1
    stats.time = 0.1
    settings.sheep_speed = 0.5

    load_level(screen, settings, stats, black_sheep, white_sheeps)

    stats.game_active = "menu"


# Carrega level
def load_level(screen, settings, stats, black_sheep, white_sheeps):
    stats.game_active = "wait"

    black_sheep.loadColorSheep("black")

    white_sheeps.empty()
    create_white_sheeps(screen, settings, stats, white_sheeps)

    sleep(3)


# Desenha a caixa de dialogo
def draw_box(screen, settings, screenSize, result):
    pygame.draw.rect(screen, settings.rect_color,
                     [(screenSize[0] / 2 - settings.rect_width / 2),
                      (screenSize[1] / 2 - settings.rect_height / 2),
                      settings.rect_width, settings.rect_height])

    font = pygame.font.SysFont(None, 42)
    text = font.render(('Você ' + result + '.'), True, settings.font_color)

    font_size = text.get_size()

    screen.blit(text,
                [(screenSize[0] / 2 - font_size[0] / 2),
                 (screenSize[1] / 2 - font_size[1] / 2)])


# Desenha os botoes
def button(screen, settings, stats, screenSize):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    text = ["New game", "Exit"]
    if stats.time > 0.1 or not stats.level == 1:
        text[0] = "Continue"

    font = [pygame.font.SysFont(None, 64), pygame.font.SysFont(None, 64)]
    text_buttons = [font[0].render(text[0], True, settings.font_color_buttons),
                    font[1].render(text[1], True, settings.font_color_buttons)]

    font_size_buttons = [text_buttons[0].get_size(), text_buttons[1].get_size()]

    buttons_x = [screen.get_rect().right - (font_size_buttons[0][0] + screenSize[0] / 20),
                 screen.get_rect().right - (font_size_buttons[1][0] + screenSize[0] / 20)]

    buttons_y = [screenSize[1] / 2 + screenSize[1] / 4 - font_size_buttons[0][1] / 2,
                 screenSize[1] / 2 + screenSize[1] / 4 + font_size_buttons[1][1] / 2]

    if ((buttons_x[0] + font_size_buttons[0][0]) > mouse[0] > buttons_x[0] and
                    (buttons_y[0] + font_size_buttons[0][1]) > mouse[1] > buttons_y[0]):
        font[0] = pygame.font.SysFont(None, 72)
        text_buttons[0] = font[0].render(text[0], True, settings.font_color_buttons_featured)
        if click[0] == 1:
            stats.game_active = "move"
    else:
        font[0] = pygame.font.SysFont(None, 64)
        text_buttons[0] = font[0].render(text[0], True, settings.font_color_buttons)

    if ((buttons_x[1] + font_size_buttons[1][0]) > mouse[0] > buttons_x[1] and
                    (buttons_y[1] + font_size_buttons[1][1]) > mouse[1] > buttons_y[1]):
        font[1] = pygame.font.SysFont(None, 72)
        text_buttons[1] = font[1].render(text[1], True, settings.font_color_buttons_featured)
        if click[0] == 1:
            sys.exit()
    else:
        font[1] = pygame.font.SysFont(None, 64)
        text_buttons[1] = font[1].render(text[1], True, settings.font_color_buttons)

    screen.blit(text_buttons[0], [buttons_x[0], buttons_y[0]])
    screen.blit(text_buttons[1], [buttons_x[1], buttons_y[1]])


# Cria as ovelhas brancas.                   
def create_white_sheeps(screen, settings, stats, white_sheeps):
    for sheep_number in range(stats.level):
        sheep = Sheep(screen, settings, "white")
        white_sheeps.add(sheep)

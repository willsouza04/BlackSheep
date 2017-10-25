class Settings():

    def __init__(self, screenSize):

        # Configurações da tela
        self.screen_width = screenSize[0]
        self.screen_height = screenSize[1]
        self.bg_color = (100, 100, 100)

        # Configurações do retangulo
        self.rect_color = (150, 150, 150)
        self.rect_width = 300
        self.rect_height = 200

        # Configurações da fonte
        self.font_color = (20, 20, 20)

        # Configurações da ovelha
        self.sheep_speed = 0.5

        # Configurações do menu
        self.font_color_buttons = (200, 200, 200)
        self.font_color_buttons_featured = (150, 150, 150)
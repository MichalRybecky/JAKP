import pygame
import pygame_textinput

from utils.load_assets import (
    BG_CALC_L,
    BG_CALC_D,
    BIG_FONT,
    MAIN_FONT,
    BACK,
    MENU,
    FONT_COLOR_L,
    FONT_COLOR_D,
)
from settings import WIN, WIDTH, WIDTH_H, HEIGHT_H, FPS
from utils.user_settings_handling import return_user_settings
from apps.settings_menu import settings_menu


def kalkulacka_app():
    """
    GUI pre Kalkulacku
    """
    run = True
    click = False
    clock = pygame.time.Clock()
    active = None

    # BUTTON INITIALIZATION
    B_RETURNED_PRICE = pygame.Rect(140, 480, 220, 95)
    B_BACK = pygame.Rect(20, 20, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 65 - 20, 20, 60, 60)

    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        user_settings = return_user_settings()
        BG = BG_CALC_L if user_settings["theme"] == "light" else BG_CALC_D
        FONT_COLOR = FONT_COLOR_L if user_settings["theme"] == "light" else FONT_COLOR_D
        WIN.blit(BG, (0, 0))
        WIN.blit(BACK, (20, 20))
        WIN.blit(MENU, (WIDTH - 65 - 20, 20))

        # LABELS
        label_ac = BIG_FONT.render("AC", 1, FONT_COLOR)
        WIN.blit(label_ac, (65, 365))
        label_7 = BIG_FONT.render("7", 1, FONT_COLOR)
        WIN.blit(label_7, (80, 465))
        label_4 = BIG_FONT.render("4", 1, FONT_COLOR)
        WIN.blit(label_4, (80, 565))
        label_4 = BIG_FONT.render("1", 1, FONT_COLOR)
        WIN.blit(label_4, (88, 665))
        label_0 = BIG_FONT.render("0", 1, FONT_COLOR)
        WIN.blit(label_0, (130, 765))
        label_8 = BIG_FONT.render("8", 1, FONT_COLOR)
        WIN.blit(label_8, (185, 465))
        label_5 = BIG_FONT.render("5", 1, FONT_COLOR)
        WIN.blit(label_5, (185, 565))
        label_2 = BIG_FONT.render("2", 1, FONT_COLOR)
        WIN.blit(label_2, (185, 665))
        label_9 = BIG_FONT.render("9", 1, FONT_COLOR)
        WIN.blit(label_9, (280, 465))
        label_6 = BIG_FONT.render("6", 1, FONT_COLOR)
        WIN.blit(label_6, (280, 565))
        label_3 = BIG_FONT.render("3", 1, FONT_COLOR)
        WIN.blit(label_3, (280, 665))
        label_equals = BIG_FONT.render("=", 1, FONT_COLOR)
        WIN.blit(label_equals, (395, 765))
        label_dot = BIG_FONT.render(".", 1, FONT_COLOR)
        WIN.blit(label_dot, (290, 765))
        label_divide = BIG_FONT.render("/", 1, FONT_COLOR)
        WIN.blit(label_divide, (400, 365))
        label_times = BIG_FONT.render("*", 1, FONT_COLOR)
        WIN.blit(label_times, (400, 475))
        label_minus = BIG_FONT.render("-", 1, FONT_COLOR)
        WIN.blit(label_minus, (400, 570))
        label_plus = BIG_FONT.render("+", 1, FONT_COLOR)
        WIN.blit(label_plus, (398, 668))

        # Zistovanie, ci nebolo kliknute na textove pole
        if click:
            if B_STOCK_INPUT.collidepoint(pos_x, pos_y):
                active = stock_input
            elif B_GET_PRICE.collidepoint(pos_x, pos_y):
                result = price_validation(stock_input.get_text().strip())
            elif B_BACK.collidepoint(pos_x, pos_y):
                run = False
            elif B_MENU.collidepoint(pos_x, pos_y):
                settings_menu()
                events = pygame.event.get()
                stock_input.update(events)
            else:
                active = None

        # Setnutie aktivneho textoveho pola, pokial nejake je
        try:
            active.update(events)
        except AttributeError:
            pass

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_RETURN]:
        #    result = price_validation(stock_input.get_text().strip())

        # Event handling
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.update()
        clock.tick(FPS)

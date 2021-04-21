import pygame
import pygame_textinput

from utils.load_assets import SETTINGS_MENU
from settings import WIN, FPS#, UI_COLOR, WIDTH, HEIGHT, WIDTH_H, HEIGHT_H, FPS


def settings_menu():
    """
    GUI pre settings menu
    """
    run = True
    click = False
    clock = pygame.time.Clock()
    active = None

    # BUTTON INITIALIZATION
    B_GET_PRICE = pygame.Rect(130, 385, 240, 65)
    B_RETURNED_PRICE = pygame.Rect(140, 480, 220, 95)

    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        WIN.blit(SETTINGS_MENU, (245, 25))

        # Zistovanie, ci nebolo kliknute na textove pole
        if click:
            #if B_STOCK_INPUT.collidepoint(pos_x, pos_y):
            #    active = stock_input
            #else:
            #    active = None
            run = False

        # Setnutie aktivneho textoveho pola, pokial nejake je
        try:
            active.update(events)
        except AttributeError:
            pass

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

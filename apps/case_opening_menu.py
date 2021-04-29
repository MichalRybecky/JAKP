import pygame
import pygame_textinput

from utils.load_assets import (
    BG_CASEKY_VOLBA_L,
    BG_CASEKY_VOLBA_D,
    BIG_FONT,
    BACK,
    MENU,
    FONT_COLOR_L,
    FONT_COLOR_D,
)
from settings import UI_COLOR, WIN, WIDTH, HEIGHT, WIDTH_H, HEIGHT_H, FPS
from utils.user_settings_handling import return_user_settings
from apps.settings_menu import settings_menu


def cases_app_opening():
    """
    GUI pre Caseky inventar
    """
    run = True
    click = False
    clock = pygame.time.Clock()

    # BUTTON INITIALIZATION
    B_INV_BACK = pygame.Rect(190, 205, 55, 55)
    B_INV_FORWARD = pygame.Rect(255, 205, 55, 55)
    B_OPENING = pygame.Rect(110, 105, 280, 75)
    B_BACK = pygame.Rect(20, 20, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 65 - 20, 20, 60, 60)
    
    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        user_settings = return_user_settings()
        BG = BG_CASEKY_VOLBA_L if user_settings["theme"] == "light" else BG_CASEKY_VOLBA_D
        FONT_COLOR = FONT_COLOR_L if user_settings["theme"] == "light" else FONT_COLOR_D
        WIN.blit(BG, (0, 0))
        WIN.blit(BACK, (20, 20))
        WIN.blit(MENU, (WIDTH - 65 - 20, 20))

        # LABELS
        #label_caseky = BIG_FONT.render("Caseky", 1, FONT_COLOR)
        #WIN.blit(
        #    label_caseky,
        #    (WIDTH_H - 60, 120),
        #)

        # Zistovanie, ci nebolo kliknute na textove pole
        if click:
            if B_BACK.collidepoint(pos_x, pos_y):
                run = False
            elif B_MENU.collidepoint(pos_x, pos_y):
                settings_menu()
            #elif B_INV_FORWARD.collidepoint(pos_x, pos_y):
            #    inv_forward()

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

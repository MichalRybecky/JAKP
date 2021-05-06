import pygame
import pygame_textinput

from utils.load_assets import SETTINGS_MENU_L, SETTINGS_MENU_D
from settings import WIN, FPS, UI_COLOR
from utils.user_settings_handling import return_user_settings
from utils.user_settings_handling import write_user_settings


def toggle_theme():
    user_settings = return_user_settings()
    if user_settings["theme"] == "light":
        user_settings["theme"] = "dark"
    else:
        user_settings["theme"] = "light"
    write_user_settings(user_settings)


def settings_menu():
    """
    GUI pre settings menu
    """
    run = True
    click = False
    clock = pygame.time.Clock()
    active = None
    click_cooldown = 0.0

    # BUTTON INITIALIZATION
    B_BG_TOGGLE = pygame.Rect(275, 55, 60, 60)
    B_THEME_TOGGLE = pygame.Rect(365, 65, 80, 40)

    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        user_settings = return_user_settings()
        if user_settings["theme"] == "light":
            WIN.blit(SETTINGS_MENU_L, (245, 25))
        else:
            WIN.blit(SETTINGS_MENU_D, (245, 25))

        # Zistovanie, ci nebolo kliknute na textove pole
        if click and click_cooldown == 0.0:
            if B_THEME_TOGGLE.collidepoint(pos_x, pos_y):
                toggle_theme()
                run = False
                # click_cooldown = FPS // 3
            else:
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

        if click_cooldown != 0.0:
            click_cooldown -= 1
        pygame.display.update()
        clock.tick(FPS)

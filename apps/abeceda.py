import pygame
import pygame_textinput

from utils.load_assets import (
    BG_L,
    BG_D,
    BIG_FONT,
    MAIN_FONT,
    BACK,
    MENU,
    FONT_COLOR_L,
    FONT_COLOR_D,
)
from settings import UI_COLOR, WIN, WIDTH, WIDTH_H, HEIGHT_H, FPS
from utils.user_settings_handling import return_user_settings
from apps.settings_menu import settings_menu


def abeceda_app():
    """
    GUI pre Abecedny zoradovac
    """
    run = True
    click = False
    clock = pygame.time.Clock()
    user_settings = return_user_settings()
    FONT_COLOR = FONT_COLOR_L if user_settings["theme"] == "light" else FONT_COLOR_D
    abc_input = pygame_textinput.TextInput(
        initial_string="slova na zoradenie oddelene medzerou",
        font_family="pixel_font.ttf",
        font_size=20,
        text_color=FONT_COLOR,
        cursor_color=FONT_COLOR,
        max_string_length=50,
    )
    events = pygame.event.get()
    abc_input.update(events)
    active = None

    # BUTTON INITIALIZATION
    B_ABC_INPUT = pygame.Rect(40, 140, WIDTH - 80, 280)
    B_SORT = pygame.Rect(130, 440, 240, 65)
    B_OUTPUT = pygame.Rect(40, 525, WIDTH - 80, 280) # delete after proper bg
    B_BACK = pygame.Rect(20, 20, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 65 - 20, 20, 60, 60)

    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        user_settings = return_user_settings()
        BG = BG_L if user_settings["theme"] == "light" else BG_D
        FONT_COLOR = FONT_COLOR_L if user_settings["theme"] == "light" else FONT_COLOR_D
        WIN.blit(BG, (0, 0))
        WIN.blit(BACK, (20, 20))
        WIN.blit(MENU, (WIDTH - 65 - 20, 20))

        pygame.draw.rect(WIN, UI_COLOR, B_ABC_INPUT)
        pygame.draw.rect(WIN, UI_COLOR, B_SORT)
        pygame.draw.rect(WIN, UI_COLOR, B_OUTPUT)

        # LABELS
        label_abc_input = MAIN_FONT.render(abc_input.get_text(), 1, FONT_COLOR)
        WIN.blit(
            label_abc_input,
            (60, 150),
        )

        label_return = BIG_FONT.render("Sort", 1, FONT_COLOR)
        WIN.blit(label_return, (WIDTH_H - (label_return.get_width() // 2), HEIGHT_H))

        # Zistovanie, ci nebolo kliknute na textove pole
        if click:
            if B_ABC_INPUT.collidepoint(pos_x, pos_y):
                active = abc_input
            elif B_SORT.collidepoint(pos_x, pos_y):
                # TODO: pridat volanie sort funkcie ked bude hotova
                pass
            elif B_BACK.collidepoint(pos_x, pos_y):
                run = False
            elif B_MENU.collidepoint(pos_x, pos_y):
                settings_menu()
                events = pygame.event.get()
                abc_input.update(events)
            else:
                active = None

        # Setnutie aktivneho textoveho pola, pokial nejake je
        try:
            active.update(events)
        except AttributeError:
            pass

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            # TODO: pridat volanie sort funkcie ked bude hotova
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

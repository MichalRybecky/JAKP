import pygame
import pygame_textinput

from utils.load_assets import BG_MENY_L, BG_MENY_D, BIG_FONT, BACK, MENU, FONT_COLOR_L, FONT_COLOR_D
from settings import WIN, WIDTH, HEIGHT_H, FPS
from utils.user_settings_handling import return_user_settings
from apps.settings_menu import settings_menu

from utils.premeny_mien import from_eur, from_xyz


def convert(rates, cur_amount, cur_from, cur_to):
    if cur_from.get_text().lower() == "eur":
        result = from_eur(
            rates[cur_to.get_text().upper()], int(cur_amount.get_text())
        )
    else:
        result = from_xyz(
            rates[cur_from.get_text().upper()], int(cur_amount.get_text())
        )
    return result


def meny_app(rates):
    """
    GUI pre Premenu mien
    """
    run = True
    click = False
    clock = pygame.time.Clock()

    user_settings = return_user_settings()
    FONT_COLOR = FONT_COLOR_L if user_settings["theme"] == "light" else FONT_COLOR_D
    cur_amount = pygame_textinput.TextInput(
        initial_string="1",
        font_family="pixel_font.ttf",
        font_size=20,
        text_color=FONT_COLOR,
        cursor_color=FONT_COLOR,
        max_string_length=7,
    )
    cur_from = pygame_textinput.TextInput(
        initial_string="EUR",
        font_family="pixel_font.ttf",
        font_size=16,
        text_color=FONT_COLOR,
        cursor_color=FONT_COLOR,
        max_string_length=3,
    )
    cur_to = pygame_textinput.TextInput(
        initial_string="USD",
        font_family="pixel_font.ttf",
        font_size=16,
        text_color=FONT_COLOR,
        cursor_color=FONT_COLOR,
        max_string_length=3,
    )
    cur_result = pygame_textinput.TextInput(
        font_family="pixel_font.ttf",
        font_size=20,
        text_color=FONT_COLOR,
        cursor_color=FONT_COLOR,
    )
    events = pygame.event.get()
    cur_amount.update(events)
    cur_from.update(events)
    cur_to.update(events)
    result = 0.0
    active = None
    switch_cooldown = 0

    # BUTTON INITIALIZATION
    B_CUR_AMOUNT = pygame.Rect(45, 250, 250, 100)
    B_CONVERT = pygame.Rect(45, 500, 250, 80)
    B_RESULT = pygame.Rect(45, 375, 250, 100)
    B_FROM = pygame.Rect(WIDTH - 175, 250, 125, 95)
    B_TO = pygame.Rect(WIDTH - 175, 375, 125, 95)
    B_BACK = pygame.Rect(20, 20, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 60 - 20, 20, 60, 60)
    B_SWITCH = pygame.Rect(WIDTH - 175, 500, 125, 95)

    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        user_settings = return_user_settings()
        BG_MENY = BG_MENY_L if user_settings["theme"] == "light" else BG_MENY_D
        FONT_COLOR = FONT_COLOR_L if user_settings["theme"] == "light" else FONT_COLOR_D
        WIN.blit(BG_MENY, (0, 0))
        WIN.blit(BACK, (20, 20))
        WIN.blit(MENU, (WIDTH - 65 - 20, 20))

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

        # BUTTONS AND COLLIDEPOINTS
        label_cur_amount = BIG_FONT.render(cur_amount.get_text(), 1, FONT_COLOR)
        WIN.blit(
            label_cur_amount,
            (175 - len(cur_amount.get_text()) * 12, 275),
        )
        label_cur_from = BIG_FONT.render(cur_from.get_text(), 1, FONT_COLOR)
        label_cur_to = BIG_FONT.render(cur_to.get_text(), 1, FONT_COLOR)
        WIN.blit(label_cur_from, (WIDTH - 145, 275))
        WIN.blit(label_cur_to, (WIDTH - 145, 400))

        # LABELS
        label_konvertuj = BIG_FONT.render("Convert", 1, FONT_COLOR)
        WIN.blit(label_konvertuj, (100, HEIGHT_H + 70))
        if result != 0.0:
            label_result = BIG_FONT.render(str(result), 1, FONT_COLOR)
            WIN.blit(label_result, (200 - len(str(result)) * 12, 400))

        # Zistovanie, ci nebolo kliknute na textove pole
        if click:
            if B_CUR_AMOUNT.collidepoint(pos_x, pos_y):
                active = cur_amount
            elif B_FROM.collidepoint(pos_x, pos_y):
                active = cur_from
            elif B_TO.collidepoint(pos_x, pos_y):
                active = cur_to
            elif B_BACK.collidepoint(pos_x, pos_y):
                run = False
            elif B_MENU.collidepoint(pos_x, pos_y):
                settings_menu()
                events = pygame.event.get()
                cur_amount.update(events)
                cur_from.update(events)
                cur_to.update(events)
            elif B_CONVERT.collidepoint(pos_x, pos_y):
                result = convert(rates, cur_amount, cur_from, cur_to)
            elif B_SWITCH.collidepoint(pos_x, pos_y) and switch_cooldown == 0:
                cur_from, cur_to = cur_to, cur_from
                cur_from.update(events)
                cur_to.update(events)
                switch_cooldown = FPS // 3
            else:
                active = None

        # Setnutie aktivneho textoveho pola, pokial nejake je
        try:
            active.update(events)
        except AttributeError:
            pass

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            result = convert(rates, cur_amount, cur_from, cur_to)

        if switch_cooldown != 0:
            switch_cooldown -= 1
        pygame.display.update()
        clock.tick(FPS)

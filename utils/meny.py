import pygame
import pygame_textinput

from utils.load_assets import BG, MAIN_FONT, BIG_FONT, BACK, MENU
from settings import WIN, UI_COLOR, WIDTH, HEIGHT, WIDTH_H, HEIGHT_H, FPS


def meny_app():
    """
    GUI pre Premenu mien
    """
    run = True
    click = False
    clock = pygame.time.Clock()
    cur_amount = pygame_textinput.TextInput(initial_string="1")
    cur_from = pygame_textinput.TextInput(initial_string="EUR")
    cur_to = pygame_textinput.TextInput(initial_string="USD")
    events = pygame.event.get()
    cur_amount.update(events)
    cur_from.update(events)
    cur_to.update(events)
    active = None

    # BUTTON INITIALIZATION
    B_CUR_AMOUNT = pygame.Rect(WIDTH_H - 150, HEIGHT_H + 150, 300, 40)
    B_CONVERT = pygame.Rect(WIDTH_H - 100, HEIGHT_H + 200, 200, 60)
    B_RESULT = pygame.Rect(WIDTH_H - 150, HEIGHT_H + 325, 300, 40)
    B_FROM = pygame.Rect(50, HEIGHT_H - 200, 80, 40)
    B_TO = pygame.Rect(WIDTH - 130, HEIGHT_H - 200, 80, 40)
    B_BACK = pygame.Rect(10, 10, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 60 - 10, 10, 60, 60)

    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        WIN.blit(BG, (0, 0))
        WIN.blit(BACK, (10, 10))
        WIN.blit(MENU, (WIDTH - 60 - 10, 10))

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
        pygame.draw.rect(WIN, UI_COLOR, B_CUR_AMOUNT)
        WIN.blit(
            cur_amount.get_surface(),
            (WIDTH_H - len(cur_amount.get_text()) * 6, HEIGHT_H + 160),
        )

        pygame.draw.rect(WIN, UI_COLOR, B_FROM)
        WIN.blit(cur_from.get_surface(), (70, HEIGHT_H - 190))

        pygame.draw.rect(WIN, UI_COLOR, B_TO)
        WIN.blit(cur_to.get_surface(), (WIDTH - 120, HEIGHT_H - 190))

        pygame.draw.rect(WIN, UI_COLOR, B_CONVERT)
        pygame.draw.rect(WIN, UI_COLOR, B_RESULT)

        # LABELS
        label_cur_amount = BIG_FONT.render("Penaze", 1, (0, 0, 0))
        WIN.blit(
            label_cur_amount,
            (WIDTH_H - (label_cur_amount.get_width() // 2), HEIGHT_H + 100),
        )
        label_convert = MAIN_FONT.render("Konvertovat", 1, (0, 0, 0))
        WIN.blit(
            label_convert,
            (WIDTH_H - (label_convert.get_width() // 2), HEIGHT_H + 215),
        )
        label_convert = BIG_FONT.render("Vysledok", 1, (0, 0, 0))
        WIN.blit(
            label_convert,
            (WIDTH_H - (label_convert.get_width() // 2), HEIGHT_H + 275),
        )

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
            else:
                active = None

        # Setnutie aktivneho textoveho pola, pokial nejake je
        try:
            # TODO Limit znakov
            active.update(events)
        except AttributeError:
            pass

        pygame.display.update()
        clock.tick(FPS)


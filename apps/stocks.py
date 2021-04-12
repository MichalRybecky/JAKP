import pygame
import pygame_textinput

from utils.load_assets import BG_STOCKS, MAIN_FONT, BIG_FONT, BACK, MENU, FONT_COLOR
from settings import WIN, UI_COLOR, WIDTH, HEIGHT, WIDTH_H, HEIGHT_H, FPS

from utils.stocks import get_price


def stocks_app():
    """
    GUI pre Stocks
    """
    run = True
    click = False
    clock = pygame.time.Clock()
    stock_input = pygame_textinput.TextInput(
        initial_string="GME", font_family="pixel_font.ttf", font_size=20, text_color=FONT_COLOR,
    )
    events = pygame.event.get()
    stock_input.update(events)
    active = None
    result = 0.0

    # BUTTON INITIALIZATION
    B_STOCK_INPUT = pygame.Rect(140, 260, 220, 95)
    B_GET_PRICE = pygame.Rect(130, 385, 240, 65)
    B_RETURNED_PRICE = pygame.Rect(140, 480, 220, 95)
    B_BACK = pygame.Rect(20, 20, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 65 - 20, 20, 60, 60)

    # LABELS
    label_return = BIG_FONT.render("Return", 1, FONT_COLOR)

    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        WIN.blit(BG_STOCKS, (0, 0))
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
        WIN.blit(
            stock_input.get_surface(),
            (WIDTH_H - len(stock_input.get_text()) * 14, 285),
        )

        # LABELS
        WIN.blit(label_return, (WIDTH_H - (label_return.get_width() // 2), 395))

        if result != 0.0:
            label_price = MAIN_FONT.render(result, 1, FONT_COLOR)
            WIN.blit(
                label_price,
                (WIDTH_H - (label_price.get_width() // 2), HEIGHT_H + 65),
            )

        # Zistovanie, ci nebolo kliknute na textove pole
        if click:
            if B_STOCK_INPUT.collidepoint(pos_x, pos_y):
                active = stock_input
            elif B_GET_PRICE.collidepoint(pos_x, pos_y):
                result = get_price(stock_input.get_text().strip())
                if result < 0:
                    if result == -1:
                        result = "Unknown symbol"
                    elif result == -2:
                        result = "Empty string"
                else:
                    result = str(result) + " $"

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

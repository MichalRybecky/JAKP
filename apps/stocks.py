import pygame
import pygame_textinput

from utils.load_assets import BG_STOCKS_L, BG_STOCKS_D, MAIN_FONT, BIG_FONT, BACK, MENU, FONT_COLOR_L, FONT_COLOR_D
from settings import WIN, UI_COLOR, WIDTH, HEIGHT, WIDTH_H, HEIGHT_H, FPS
from utils.user_settings_handling import return_user_settings

from utils.stocks import get_price


def return_price(ticker):
    result = get_price(ticker)
    if result < 0:
        if result == -1:
            result = "Unknown symbol"
        elif result == -2:
            result = "Empty string"
    else:
        result = str(result) + " $"
    return result


def stocks_app():
    """
    GUI pre Stocks
    """
    run = True
    click = False
    clock = pygame.time.Clock()
    user_settings = return_user_settings()
    if user_settings["theme"] == "light":
        FONT_COLOR = FONT_COLOR_L
    else:
        FONT_COLOR = FONT_COLOR_D
    stock_input = pygame_textinput.TextInput(
        initial_string="GME",
        font_family="pixel_font.ttf",
        font_size=20,
        text_color=FONT_COLOR,
        cursor_color=FONT_COLOR,
        max_string_length=5
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
        user_settings = return_user_settings()
        if user_settings["theme"] == "light":
            FONT_COLOR = FONT_COLOR_L
            BG_STOCKS = BG_STOCKS_L
        else:
            FONT_COLOR = FONT_COLOR_D
            BG_STOCKS = BG_STOCKS_D

        WIN.blit(BG_STOCKS, (0, 0))
        WIN.blit(BACK, (20, 20))
        WIN.blit(MENU, (WIDTH - 65 - 20, 20))

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
                result = return_price(stock_input.get_text().strip())
            elif B_BACK.collidepoint(pos_x, pos_y):
                run = False
            else:
                active = None

        # Setnutie aktivneho textoveho pola, pokial nejake je
        try:
            active.update(events)
        except AttributeError:
            pass

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            result = return_price(stock_input.get_text().strip())

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

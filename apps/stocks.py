import pygame
import pygame_textinput

from utils.load_assets import BG, MAIN_FONT, BIG_FONT, BACK, MENU
from settings import WIN, UI_COLOR, WIDTH, HEIGHT, WIDTH_H, HEIGHT_H, FPS

from utils.stocks import get_price


def stocks_app():
    """
    GUI pre Stocks 
    """
    run = True
    click = False
    clock = pygame.time.Clock()
    stock_input = pygame_textinput.TextInput(initial_string="GME")
    events = pygame.event.get()
    stock_input.update(events)
    active = None
    returned_price = 0.0

    # BUTTON INITIALIZATION
    B_STOCK_INPUT = pygame.Rect(WIDTH_H - 50, HEIGHT_H + 150, 100, 40)
    B_GET_PRICE = pygame.Rect(WIDTH_H - 75, HEIGHT_H + 250, 150, 40)
    B_RETURNED_PRICE = pygame.Rect(WIDTH_H - 100, HEIGHT_H + 350, 200, 40)
    B_BACK = pygame.Rect(10, 10, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 60 - 10, 10, 60, 60)
    
    # LABELS
    label_zadaj_stock = BIG_FONT.render("Stock", 1, (0, 0, 0))

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
        pygame.draw.rect(WIN, UI_COLOR, B_STOCK_INPUT)
        WIN.blit(
            stock_input.get_surface(),
            (WIDTH_H - len(stock_input.get_text()) * 6, HEIGHT_H + 160),
        )
        pygame.draw.rect(WIN, UI_COLOR, B_GET_PRICE)
        pygame.draw.rect(WIN, UI_COLOR, B_RETURNED_PRICE)

        # LABELS
        WIN.blit(
            label_zadaj_stock,
            (WIDTH_H - (label_zadaj_stock.get_width() // 2), HEIGHT_H + 100),
        )
        if returned_price != 0.0:
            label_price = MAIN_FONT.render(returned_price, 1, (0, 0, 0))
            WIN.blit(
                label_price,
                (WIDTH_H - (label_price.get_width() // 2), HEIGHT_H + 350),
            )

        # Zistovanie, ci nebolo kliknute na textove pole
        if click:
            if B_STOCK_INPUT.collidepoint(pos_x, pos_y):
                active = stock_input
            elif B_GET_PRICE.collidepoint(pos_x, pos_y):
                returned_price = get_price(stock_input.get_text().strip())
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


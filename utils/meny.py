import pygame
import pygame_textinput

from utils.load_assets import BG, MAIN_FONT, BIG_FONT
from settings import WIN, UI_COLOR, WIDTH, HEIGHT, WIDTH_H, HEIGHT_H


def meny_app():
    """
    GUI pre Premenu mien
    """
    run = True
    click = False
    cur_amount = pygame_textinput.TextInput()
    cur_from = pygame_textinput.TextInput("EUR")
    cur_to = pygame_textinput.TextInput("USD")
    events = pygame.event.get()
    cur_from.update(events)
    cur_to.update(events)
    active = None

    # BUTTON INITIALIZATION
    B_CUR_AMOUNT = pygame.Rect(WIDTH_H - 150, HEIGHT_H + 150, 300, 40)
    B_FROM = pygame.Rect(WIDTH_H - 150, HEIGHT_H - 200, 300, 40)
    B_TO = pygame.Rect(WIDTH_H - 150, HEIGHT_H - 400, 300, 40)

    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        WIN.blit(BG, (0, 0))
        
        #Event handling
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

        # BUTTONS, TEXTS AND COLLIDEPOINTS
        pygame.draw.rect(WIN, UI_COLOR, B_CUR_AMOUNT)
        WIN.blit(cur_amount.get_surface(), (WIDTH_H - len(cur_amount.get_text()) * 6, HEIGHT_H + 160))

        pygame.draw.rect(WIN, UI_COLOR, B_FROM)
        WIN.blit(cur_from.get_surface(), (WIDTH_H - 150, HEIGHT_H - 200))

        pygame.draw.rect(WIN, UI_COLOR, B_TO)
        WIN.blit(cur_to.get_surface(), (WIDTH_H - 150, HEIGHT_H - 400))


        if B_CUR_AMOUNT.collidepoint(pos_x, pos_y):
            active = cur_amount
        elif B_FROM.collidepoint(pos_x, pos_y):
            active = cur_from
        elif B_TO.collidepoint(pos_x, pos_y):
            active = cur_to

        try: 
            active.update(events)
        except AttributeError:
            pass
        
        # LABELS
        label_cur_amount = BIG_FONT.render("Penaze", 1, UI_COLOR)
        WIN.blit(label_cur_amount, (WIDTH_H - (label_cur_amount.get_width() // 2), HEIGHT_H + 100))

        pygame.display.update()

    pygame.quit()

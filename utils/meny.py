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
    
    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        WIN.blit(BG, (0, 0))
        
        pygame.draw.rect(WIN, UI_COLOR, pygame.Rect(WIDTH_H - 150, HEIGHT_H + 150, 300, 40)) 

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

        if cur_amount.update(events):
            print(cur_amount.get_text())
        elif cur_from.update(events):
            print(cur_from.get_text())
        elif cur_to.update(events):
            print(cur_to.get_text())

        # TEXTY
        WIN.blit(cur_amount.get_surface(), (WIDTH_H - len(cur_amount.get_text()) * 6, HEIGHT_H + 160))
        WIN.blit(cur_from.get_surface(), (100, 100))
        WIN.blit(cur_to.get_surface(), (100, 100))

        # LABELS
        label_cur_amount = BIG_FONT.render("Penaze", 1, UI_COLOR)
        WIN.blit(label_cur_amount, (WIDTH_H - (label_cur_amount.get_width() // 2), HEIGHT_H + 100))

        pygame.display.update()

    pygame.quit()

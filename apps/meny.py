import pygame
import pygame_textinput

from utils.load_assets import BG_MENY, MAIN_FONT, BIG_FONT, BACK, MENU
from settings import WIN, UI_COLOR, WIDTH, HEIGHT, WIDTH_H, HEIGHT_H, FPS

from utils.premeny_mien import from_eur, from_xyz

import http.client
import xml.etree.ElementTree as ET

conn = http.client.HTTPSConnection("www.ecb.europa.eu")
conn.request("GET", "/stats/eurofxref/eurofxref-daily.xml")
res = conn.getresponse()
data = res.read()
root = ET.fromstring(data)
rates = {}
for i in root[2][0]:
    entry = i.attrib
    rates.update({entry['currency']: float(entry['rate'])})

def meny_app():
    """
    GUI pre Premenu mien
    """
    run = True
    click = False
    clock = pygame.time.Clock()
    cur_amount = pygame_textinput.TextInput(
        initial_string="1", font_family="pixel_font.ttf", font_size=20,
    )
    cur_from = pygame_textinput.TextInput(
        initial_string="EUR", font_family="pixel_font.ttf", font_size=16
    )
    cur_to = pygame_textinput.TextInput(
        initial_string="USD", font_family="pixel_font.ttf", font_size=16
    )
    cur_result = pygame_textinput.TextInput(font_family="pixel_font.ttf", font_size=20)
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
        WIN.blit(
            cur_amount.get_surface(),
            (175 - len(cur_amount.get_text()) * 12, 275),
        )
        WIN.blit(cur_from.get_surface(), (WIDTH - 140, 280))
        WIN.blit(cur_to.get_surface(), (WIDTH - 140, 405))

        # LABELS
        label_konvertuj = BIG_FONT.render("Konvertuj", 1, (0, 0, 0))
        WIN.blit(label_konvertuj, (80, HEIGHT_H + 75))
        if result != 0.0:
            label_result = BIG_FONT.render(str(result), 1, (0, 0, 0))
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
            elif B_CONVERT.collidepoint(pos_x, pos_y):
                if cur_from.get_text().lower() == "eur":
                    result = from_eur(
                        rates[cur_to.get_text().upper()], int(cur_amount.get_text())
                    )
                else:
                    result = from_xyz(
                        rates[cur_from.get_text().upper()], int(cur_amount.get_text())
                    )
            elif B_SWITCH.collidepoint(pos_x, pos_y) and switch_cooldown == 0:
                switch_1, switch_2 = cur_from.get_text(), cur_to.get_text()
                cur_from = pygame_textinput.TextInput(
                    initial_string=switch_2, font_family="pixel_font.ttf", font_size=16
                )
                cur_to = pygame_textinput.TextInput(
                    initial_string=switch_1, font_family="pixel_font.ttf", font_size=16
                )
                cur_from.update(events)
                cur_to.update(events)
                switch_cooldown = FPS // 3
            else:
                active = None

        # Setnutie aktivneho textoveho pola, pokial nejake je
        try:
            # TODO Limit znakov
            active.update(events)
        except AttributeError:
            pass

        if switch_cooldown != 0:
            switch_cooldown -= 1
        pygame.display.update()
        clock.tick(FPS)

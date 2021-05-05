import pygame
import pygame_textinput

from utils.load_assets import (
    BG_L,
    BG_D,
    BIG_FONT,
    BACK,
    MENU,
    FONT_COLOR_L,
    FONT_COLOR_D,
)
from cases.load_items import *
from settings import UI_COLOR, WIN, WIDTH, HEIGHT, WIDTH_H, HEIGHT_H, FPS
from utils.user_settings_handling import return_user_settings
from apps.settings_menu import settings_menu

from cases.open_case import open_case
from cases.inventory_handling import add_to_inventory


def case_opening_app(case_type: str):
    """
    GUI pre otvaranie oboch typov casok
    """
    run = True
    click = False
    clock = pygame.time.Clock()

    # BUTTON INITIALIZATION
    B_BACK = pygame.Rect(20, 20, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 65 - 20, 20, 60, 60)
    B_OPEN = pygame.Rect(160, 450, 180, 75)
    B_GO_BACK = pygame.Rect(WIDTH_H - 105, 570, 200, 65)

    dropped_item = {}

    def opening_cooldown():
        for _ in range(20):
            WIN.blit(OPENING, (0, 0))
            pygame.display.update()
            clock.tick(FPS)

    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        user_settings = return_user_settings()
        FONT_COLOR = FONT_COLOR_L if user_settings["theme"] == "light" else FONT_COLOR_D

        BG = BG_L if user_settings["theme"] == "light" else BG_D
        WIN.blit(BG, (0, 0))

        if dropped_item != {}:
            if case_type == "trip":
                if dropped_item["rarity"] == 1:
                    BG = TRIP_OPEN_L
                elif dropped_item["rarity"] == 2:
                    BG = TRIP_OPEN_SR
                elif dropped_item["rarity"] == 3:
                    BG = TRIP_OPEN_R
                else:
                    BG = TRIP_OPEN_C
            else:
                if dropped_item["rarity"] == 1:
                    BG = CLASS_OPEN_L
                elif dropped_item["rarity"] == 2:
                    BG = CLASS_OPEN_SR
                elif dropped_item["rarity"] == 3:
                    BG = CLASS_OPEN_R
                else:
                    BG = CLASS_OPEN_C
            WIN.blit(BG, (0, 0))
            WIN.blit(dropped_item["icon"], (190, 360))

            # Go back label
            label_go_back = BIG_FONT.render("Go back", 1, FONT_COLOR)
            WIN.blit(label_go_back, (WIDTH_H - 75, 580))
        else:
            CURRENT_CASE = (
                TRIP_COLLECTION_OPEN if case_type == "trip" else CLASS_COLLECTION_OPEN
            )
            WIN.blit(CURRENT_CASE, (0, 0))
            label_open = BIG_FONT.render("Open", 1, FONT_COLOR)
            WIN.blit(label_open, (WIDTH_H - 50, 460))

        WIN.blit(BACK, (20, 20))
        WIN.blit(MENU, (WIDTH - 65 - 20, 20))

        # Zistovanie, ci nebolo kliknute na textove pole
        if click:
            if (
                B_BACK.collidepoint(pos_x, pos_y)
                or B_GO_BACK.collidepoint(pos_x, pos_y)
                and dropped_item != {}
            ):
                run = False
            elif B_MENU.collidepoint(pos_x, pos_y):
                settings_menu()
            elif B_OPEN.collidepoint(pos_x, pos_y) and dropped_item == {}:
                dropped_item = open_case(case_type)
                add_to_inventory(dropped_item)
                opening_cooldown()

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

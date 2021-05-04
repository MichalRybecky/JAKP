import pygame
import pygame_textinput

from utils.load_assets import (
    BG_CASEKY_INV_L,
    BG_CASEKY_INV_D,
    BIG_FONT,
    MAIN_FONT,
    BACK,
    MENU,
    FONT_COLOR_L,
    FONT_COLOR_D,
)
from settings import WIN, WIDTH, WIDTH_H, FPS
from utils.user_settings_handling import return_user_settings
from apps.settings_menu import settings_menu

from apps.case_opening_menu import cases_app_opening
from cases.inventory_handling import read_inventory
from cases.load_items import COUNTER, LEG_BG, SR_BG, R_BG, C_BG
from cases.icon_list import icon_list


def get_current_items(items: list, current_subinv: int):
    return items[current_subinv*12:current_subinv*12+12]


def blit_items(items: list):
    """
    Blitne itemy do ich policok na backgrounde podla poradia
    """
    if len(items) > 12:
        raise Exception("Privela itemov na screen, maximalny pocet je 12")

    x = 50
    y = 300
    x_diff = 145
    y_diff = 145
    for item in items:
        for icon_name in icon_list:
            if item['name'] == icon_name['name']:
                icon = icon_name['icon'] 
                break
        if item['rarity'] == 4:
            item_bg = C_BG
        elif item['rarity'] == 3:
            item_bg = R_BG
        elif item['rarity'] == 2:
            item_bg = SR_BG
        else:
            item_bg = LEG_BG
        WIN.blit(item_bg, (x-5, y))
        WIN.blit(icon, (x, y))
        WIN.blit(COUNTER, (x + 70, y + 75)) 
        amount_to_display = str(item['amount']) if item['amount'] < 100 else "99"
        label_amount = MAIN_FONT.render(str(amount_to_display), 1, (10, 10, 10))
        WIN.blit(label_amount, (x + 90 - label_amount.get_width() // 2, y + 82))
        x += x_diff
        if x > 450:
            x = 50
            y += y_diff

def cases_app_inv():
    """
    GUI pre Caseky
    """
    run = True
    click = False
    clock = pygame.time.Clock()

    current_subinv = 0
    cooldown = 0

    # BUTTON INITIALIZATION
    B_INV_BACK = pygame.Rect(190, 205, 55, 55)
    B_INV_FORWARD = pygame.Rect(255, 205, 55, 55)
    B_OPENING = pygame.Rect(110, 105, 280, 75)
    B_BACK = pygame.Rect(20, 20, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 65 - 20, 20, 60, 60)
    
    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        user_settings = return_user_settings()
        BG = BG_CASEKY_INV_L if user_settings["theme"] == "light" else BG_CASEKY_INV_D
        FONT_COLOR = FONT_COLOR_L if user_settings["theme"] == "light" else FONT_COLOR_D
        WIN.blit(BG, (0, 0))
        WIN.blit(BACK, (20, 20))
        WIN.blit(MENU, (WIDTH - 65 - 20, 20))

        # LABELS
        label_caseky = BIG_FONT.render("Caseky", 1, FONT_COLOR)
        WIN.blit(
            label_caseky,
            (WIDTH_H - 60, 120),
        )

        current_items = get_current_items(read_inventory("by_rarity"), current_subinv)
        blit_items(current_items)


        # Zistovanie, ci nebolo kliknute na textove pole
        if click:
            if B_BACK.collidepoint(pos_x, pos_y) and not cooldown:
                run = False
                cooldown = FPS // 3
            elif B_MENU.collidepoint(pos_x, pos_y):
                settings_menu()
            elif B_INV_FORWARD.collidepoint(pos_x, pos_y) and not cooldown:
                # TODO: maximalny pocet subinventarov
                current_subinv = current_subinv + 1 if current_subinv < 5 else current_subinv
                cooldown = FPS // 3
            elif B_INV_BACK.collidepoint(pos_x, pos_y) and not cooldown:
                current_subinv = current_subinv - 1 if current_subinv > 0 else current_subinv
                cooldown = FPS // 3
            elif B_OPENING.collidepoint(pos_x, pos_y) and not cooldown:
                cases_app_opening()
                cooldown = FPS // 3

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
        if cooldown != 0:
            cooldown -= 1

        pygame.display.update()
        clock.tick(FPS)

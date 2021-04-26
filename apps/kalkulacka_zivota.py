import pygame
import pygame_textinput

from utils.load_assets import BG_D, BG_L, SMALL_FONT, MAIN_FONT, BIG_FONT, BACK, MENU, FONT_COLOR_L, FONT_COLOR_D, BG_ZIVOT_L, BG_ZIVOT_D
from settings import WIN, WIDTH, HEIGHT, WIDTH_H, HEIGHT_H, FPS, UI_COLOR
from utils.user_settings_handling import return_user_settings
from apps.settings_menu import settings_menu

from utils.kalkulacka_zivota import kalkulacka_zivota


def kalkulacka_zivota_app():
    """
    GUI pre Kalkulacku zivota
    """
    run = True
    click = False
    clock = pygame.time.Clock()

    user_settings = return_user_settings()
    if user_settings["theme"] == "light":
        FONT_COLOR = FONT_COLOR_L
    else:
        FONT_COLOR = FONT_COLOR_D
    input_field = pygame_textinput.TextInput(
        initial_string="31/12/2000",
        font_family="pixel_font.ttf",
        font_size=20,
        text_color=FONT_COLOR,
        cursor_color=FONT_COLOR,
        max_string_length=10,
    )
    events = pygame.event.get()
    input_field.update(events)
    active = None
    return_cooldown = 0
    result = {}

    # BUTTON INITIALIZATION
    B_INPUT_FIELD = pygame.Rect(95, 145, WIDTH - 190, 95)
    B_RETURN = pygame.Rect(130, 270, WIDTH - 260, 65)
    B_BACK = pygame.Rect(20, 20, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 60 - 20, 20, 60, 60)

    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        user_settings = return_user_settings()
        FONT_COLOR = FONT_COLOR_L if user_settings["theme"] == "light" else FONT_COLOR_D
        BG_ZIVOT = BG_ZIVOT_L if user_settings["theme"] == "light" else BG_ZIVOT_D
        
        WIN.blit(BG_ZIVOT, (0, 0))
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
        label_input_field = BIG_FONT.render(input_field.get_text(), 1, FONT_COLOR)
        WIN.blit(label_input_field, (150, 170))

        label_return = BIG_FONT.render("Return", 1, FONT_COLOR)
        WIN.blit(label_return, (190, 280))

        # LABELS
        if result != {}:
            if type(result) == str:
                label_result = SMALL_FONT.render(result, 1, FONT_COLOR)
                WIN.blit(label_result, (40, HEIGHT_H + 140))
            else:
                label_years = MAIN_FONT.render(f'Years: {str(result["years"])}', 1, FONT_COLOR)
                label_months = MAIN_FONT.render(f'Months: {str(result["months"])}', 1, FONT_COLOR)
                label_weeks = MAIN_FONT.render(f'Weeks: {str(result["weeks"])}', 1, FONT_COLOR)
                label_days = MAIN_FONT.render(f'Days: {str(result["days"])}', 1, FONT_COLOR)
                label_hours = MAIN_FONT.render(f'Hours: {str(result["hours"])}', 1, FONT_COLOR)
                label_minutes = SMALL_FONT.render(f'Minutes: {str(result["minutes"])}', 1, FONT_COLOR)
                label_seconds = SMALL_FONT.render(f'Seconds: {str(result["seconds"])}', 1, FONT_COLOR)
                label_miliseconds = SMALL_FONT.render(f'Miliseconds: {str(result["miliseconds"])}', 1, FONT_COLOR)
                to_blit = [label_years, label_months, label_weeks, label_days, label_hours, label_minutes, label_seconds, label_miliseconds]

                y_diff = 0
                for label in to_blit:
                    WIN.blit(label, (150, HEIGHT_H - 50 + y_diff))
                    y_diff += 40

            

        # Zistovanie, ci nebolo kliknute na textove pole
        if click:
            if B_INPUT_FIELD.collidepoint(pos_x, pos_y):
                active = input_field
            elif B_BACK.collidepoint(pos_x, pos_y):
                run = False
            elif B_MENU.collidepoint(pos_x, pos_y):
                settings_menu()
            elif B_RETURN.collidepoint(pos_x, pos_y):
                if return_cooldown == 0:
                    return_cooldown = FPS // 6
                    result = kalkulacka_zivota(input_field.get_text().strip())

            else:
                active = None

        # Setnutie aktivneho textoveho pola, pokial nejake je
        try:
            active.update(events)
        except AttributeError:
            pass

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and return_cooldown == 0:
            return_cooldown = FPS // 6
            result = kalkulacka_zivota(input_field.get_text().strip())

        if return_cooldown != 0:
            return_cooldown -= 1

        pygame.display.update()
        clock.tick(FPS)

import pygame
import pygame_textinput

from utils.load_assets import BG_D, BG_L, SMALL_FONT, MAIN_FONT, BIG_FONT, BACK, MENU, FONT_COLOR_L, FONT_COLOR_D
from settings import WIN, WIDTH, HEIGHT, WIDTH_H, HEIGHT_H, FPS, UI_COLOR
from utils.user_settings_handling import return_user_settings

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
    B_INPUT_FIELD = pygame.Rect(100, 300, WIDTH - 200, 80)
    B_RETURN = pygame.Rect(150, 450, WIDTH - 300, 80)
    B_BACK = pygame.Rect(20, 20, 60, 60)
    B_MENU = pygame.Rect(WIDTH - 60 - 20, 20, 60, 60)

    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        if user_settings["theme"] == "light":
            FONT_COLOR = FONT_COLOR_L
            BG = BG_L
        else:
            FONT_COLOR = FONT_COLOR_D
            BG = BG_D
        WIN.blit(BG, (0, 0))
        WIN.blit(BACK, (20, 20))
        WIN.blit(MENU, (WIDTH - 65 - 20, 20))

        pygame.draw.rect(WIN, UI_COLOR, B_INPUT_FIELD)
        pygame.draw.rect(WIN, UI_COLOR, B_RETURN)

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
            input_field.get_surface(),
            (WIDTH_H - len(input_field.get_text()) * 10, 320),
        )

        # LABELS
        if result != {}:
            if type(result) == str:
                display_string = result
            else:
                display_string = f"{str(int(result['years']))}, {str(int(result['months']))}, {str(int(result['days']))}, {str(int(result['hours']))}, {str(int(result['minutes']))}, {str(int(result['seconds']))}, {str(int(result['miliseconds']))}"
            label_result = SMALL_FONT.render(display_string, 1, FONT_COLOR)
            WIN.blit(label_result, (40, HEIGHT_H + 140))
            

        # Zistovanie, ci nebolo kliknute na textove pole
        if click:
            if B_INPUT_FIELD.collidepoint(pos_x, pos_y):
                active = input_field
            elif B_BACK.collidepoint(pos_x, pos_y):
                run = False
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

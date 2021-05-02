import pygame
from settings import WIN, FPS
from utils.load_assets import BG_D, BG_L, BACK, MAIN_FONT, FONT_COLOR_L, FONT_COLOR_D
from utils.user_settings_handling import return_user_settings
from utils.kvadraticka import kvadraticka_rovnica

pygame.init()
font = MAIN_FONT


def kvadraticka_app():
    cooldown = 0
    clock = pygame.time.Clock()
    b_back = pygame.Rect(400, 20, 60, 60)
    user_settings = return_user_settings()

    if user_settings["theme"] == "light":
        bg_kvadraticka = BG_L
        font_color = FONT_COLOR_L
    else:
        bg_kvadraticka = BG_D
        font_color = FONT_COLOR_D

    color_active_a = pygame.Color("lightskyblue3")
    color_passive_a = pygame.Color("gray15")
    color_a = color_passive_a

    color_active_b = pygame.Color("lightskyblue3")
    color_passive_b = pygame.Color("gray15")
    color_b = color_passive_b

    color_active_c = pygame.Color("lightskyblue3")
    color_passive_c = pygame.Color("gray15")
    color_c = color_passive_c

    active_a = False
    active_b = False
    active_c = False

    text_a = ""
    a_rect = pygame.Rect(100, 200, 100, 30)
    text_b = ""
    b_rect = pygame.Rect(100, 300, 100, 30)
    text_c = ""
    c_rect = pygame.Rect(100, 400, 100, 30)

    button_rect = pygame.Rect(100, 450, 100, 30)

    # pravdy a klamstva
    run = True
    click = False
    while run:
        pos_x, pos_y = pygame.mouse.get_pos()

        WIN.blit(bg_kvadraticka, (0, 0))
        WIN.blit(BACK, (400, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    # aktivovanie okienok
                    if a_rect.collidepoint(pos_x, pos_y):
                        active_a = True
                        color_a = color_active_a
                    else:
                        active_a = False
                        color_a = color_passive_a

                    if b_rect.collidepoint(pos_x, pos_y):
                        active_b = True
                        color_b = color_active_b
                    else:
                        active_b = False
                        color_b = color_passive_b

                    if c_rect.collidepoint(pos_x, pos_y):
                        active_c = True
                        color_c = color_active_c
                    else:
                        active_c = False
                        color_c = color_passive_c

                    if button_rect.collidepoint(pos_x, pos_y):
                        print(text_a, text_b, text_c)
                        kvadraticka_rovnica(int(text_a), int(text_b), int(text_c))

            # pisanie do okienok
            if active_a:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text_a = text_a[:-1]
                    else:
                        text_a += event.unicode

            if active_b:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text_b = text_b[:-1]
                    else:
                        text_b += event.unicode

            if active_c:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text_c = text_c[:-1]
                    else:
                        text_c += event.unicode

        if click:
            if b_back.collidepoint(pos_x, pos_y) and cooldown == 0:
                run = False

        # rectangle
        pygame.draw.rect(WIN, color_a, a_rect, 2)
        pygame.draw.rect(WIN, color_b, b_rect, 2)
        pygame.draw.rect(WIN, color_c, c_rect, 2)
        pygame.draw.rect(WIN, font_color, button_rect, 2)

        text_a_surface = font.render(text_a, True, font_color)
        WIN.blit(text_a_surface, (a_rect.x + 5, a_rect.y + 5))
        a_rect.w = max(100, text_a_surface.get_width() + 5)

        text_b_surface = font.render(text_b, True, font_color)
        WIN.blit(text_b_surface, (b_rect.x + 5, b_rect.y + 5))
        b_rect.w = max(100, text_b_surface.get_width() + 5)

        text_c_surface = font.render(text_c, True, font_color)
        WIN.blit(text_c_surface, (c_rect.x + 5, c_rect.y + 5))
        c_rect.w = max(100, text_c_surface.get_width() + 5)

        if cooldown != 0:
            cooldown -= 1

        pygame.display.update()
        clock.tick(FPS)

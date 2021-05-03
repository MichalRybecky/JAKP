import pygame
from settings import WIN, FPS
from utils.load_assets import BG_kvadraticka_D, BG_kvadraticka_L, BACK, FONT_COLOR_L, FONT_COLOR_D, BIG_FONT, MAIN_FONT
from utils.user_settings_handling import return_user_settings

# from utils.kvadraticka import kvadraticka_rovnica

pygame.init()
font = BIG_FONT
small_font = MAIN_FONT


def kvadraticka_app():
    cooldown = 0
    clock = pygame.time.Clock()
    b_back = pygame.Rect(415, 20, 60, 60)
    user_settings = return_user_settings()

    if user_settings["theme"] == "light":
        bg_kvadraticka = BG_kvadraticka_L
        font_color = FONT_COLOR_L
    else:
        bg_kvadraticka = BG_kvadraticka_D
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
    calculate = False
    a_check, b_check, c_check = None, None, None

    text_a = ""
    a_rect = pygame.Rect(203, 80, 198, 50)
    text_b = ""
    b_rect = pygame.Rect(203, 185, 198, 50)
    text_c = ""
    c_rect = pygame.Rect(203, 290, 198, 50)

    button_rect = pygame.Rect(130, 380, 240, 63)

    # pravdy a klamstva
    run = True
    click = False
    while run:
        pos_x, pos_y = pygame.mouse.get_pos()

        WIN.blit(bg_kvadraticka, (0, 0))
        WIN.blit(BACK, (415, 20))

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
                        calculate = False
                    else:
                        active_a = False
                        color_a = color_passive_a

                    if b_rect.collidepoint(pos_x, pos_y):
                        active_b = True
                        color_b = color_active_b
                        calculate = False
                    else:
                        active_b = False
                        color_b = color_passive_b

                    if c_rect.collidepoint(pos_x, pos_y):
                        active_c = True
                        color_c = color_active_c
                        calculate = False
                    else:
                        active_c = False
                        color_c = color_passive_c

                    if button_rect.collidepoint(pos_x, pos_y):
                        if len(text_a) == 0 or len(text_b) == 0 or len(text_c) == 0:
                            pass
                        else:
                            if len(text_a) != 0 and len(text_b) != 0 and len(text_c) != 0:
                                for v, i in enumerate(text_a):
                                    if i not in "1234567890":
                                        a_check = False
                                    else:
                                        a_check = True
                                for v, j in enumerate(text_b):
                                    if j not in "1234567890":
                                        b_check = False
                                    else:
                                        b_check = True
                                for v, z in enumerate(text_c):
                                    if z not in "1234567890":
                                        c_check = False
                                    else:
                                        c_check = True
                                if a_check and b_check and c_check:
                                    calculate = True
                            else:
                                pass

            # pisanie do okienok
            if active_a:
                if len(text_a) < 8:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            text_a = text_a[:-1]
                        else:
                            text_a += event.unicode
                if len(text_a) == 8:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            text_a = text_a[:-1]

            if active_b:
                if len(text_b) < 8:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            text_b = text_b[:-1]
                        else:
                            text_b += event.unicode
                if len(text_b) == 8:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            text_b = text_b[:-1]

            if active_c:
                if len(text_c) < 8:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            text_c = text_c[:-1]
                        else:
                            text_c += event.unicode
                if len(text_c) == 8:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            text_c = text_c[:-1]

        if click:
            if b_back.collidepoint(pos_x, pos_y) and cooldown == 0:
                run = False

        if calculate:
            a, b, c = int(text_a), int(text_b), int(text_c)
            diskriminant = b ** 2 - (4 * a * c)
            d_iskriminant = small_font.render("Diskriminant = " + str(diskriminant), True, font_color)
            WIN.blit(d_iskriminant, (80, 500))
            if diskriminant < 0:
                math_error = font.render("Math ERROR", True, font_color)
                WIN.blit(math_error, (140, 630))
            else:
                x_1 = ((-b) + diskriminant ** 0.5) / (2 * a)
                f_x_1 = small_font.render("x1 = " + str(x_1), True, font_color)
                WIN.blit(f_x_1, (80, 550))
                x_2 = ((-b) - diskriminant ** 0.5) / (2 * a)
                f_x_2 = small_font.render("x2 = " + str(x_2), True, font_color)
                WIN.blit(f_x_2, (80, 600))

        if a_check == False or b_check == False or c_check == False:
            ERROR = font.render("Syntax ERROR", True, font_color)
            WIN.blit(ERROR, (120, 630))

        # rectangle
        pygame.draw.rect(WIN, color_a, a_rect, 2)
        pygame.draw.rect(WIN, color_b, b_rect, 2)
        pygame.draw.rect(WIN, color_c, c_rect, 2)
        pocitaj = font.render("Calculate", True, font_color)
        WIN.blit(pocitaj, (170, 390))

        text_a_surface = font.render(text_a, True, font_color)
        WIN.blit(text_a_surface, (a_rect.x + 5, a_rect.y + 5))
        a_x = font.render("a", True, font_color)
        WIN.blit(a_x, (112, 75))

        text_b_surface = font.render(text_b, True, font_color)
        WIN.blit(text_b_surface, (b_rect.x + 5, b_rect.y + 5))
        b_x = font.render("b", True, font_color)
        WIN.blit(b_x, (115, 186))

        text_c_surface = font.render(text_c, True, font_color)
        WIN.blit(text_c_surface, (c_rect.x + 5, c_rect.y + 5))
        c_x = font.render("c", True, font_color)
        WIN.blit(c_x, (115, 285))

        if cooldown != 0:
            cooldown -= 1

        pygame.display.update()
        clock.tick(FPS)

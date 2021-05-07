import pygame
from settings import WIN
from utils.load_assets import BG_kebab_L, BG_kebab_D, BACK, MAIN_FONT, FONT_COLOR_L, FONT_COLOR_D
from utils.user_settings_handling import return_user_settings

pygame.init()

# fonty
kebab = MAIN_FONT
euro = pygame.font.Font("freesansbold.ttf", 20)


# vypisanie uctu
def vypisanie_uctu(kz, kp, tz, tp, FONT_COLOR):
    penaze = kz * 3.6 + kp * 4.1 + tz * 4.1 + tp * 4.6
    round_penaze = round(penaze, 2)
    penaze_na_obrazovke = kebab.render("" + str(round_penaze), True, FONT_COLOR)
    euro_na_obrazovke = euro.render("€", True, FONT_COLOR)
    WIN.blit(penaze_na_obrazovke, (220, 775))
    WIN.blit(euro_na_obrazovke, (300, 780))


def kebab_app():
    global kp
    global kz
    global tz
    global tp

    kz = 0
    kp = 0
    tz = 0
    tp = 0

    cooldown = 0
    FPS = 60
    clock = pygame.time.Clock()

    B_BACK = pygame.Rect(20, 20, 60, 60)

    # pravdy a klamstva
    run = True
    click = False
    while run:
        pos_x, pos_y = pygame.mouse.get_pos()
        user_settings = return_user_settings()
        
        if user_settings["theme"] == "light":
            BG_kebab = BG_kebab_L
            FONT_COLOR = FONT_COLOR_L
        else:
            BG_kebab = BG_kebab_D
            FONT_COLOR = FONT_COLOR_D

        WIN.blit(BG_kebab, (0, 0))
        WIN.blit(BACK, (20, 20))

        # kuraci kebab part
        kuraci_kebab = kebab.render("Kuraci Kebab", True, FONT_COLOR)
        WIN.blit(kuraci_kebab, (170, 85))
        k_zemla = kebab.render("Zemla", True, FONT_COLOR)
        WIN.blit(k_zemla, (105, 175))
        k_placka = kebab.render("Placka", True, FONT_COLOR)
        WIN.blit(k_placka, (325, 175))
        # collide points
        kz_decrease = pygame.Rect(45, 270, 35, 35)
        kz_increase = pygame.Rect(200, 270, 35, 35)
        kp_decrease = pygame.Rect(265, 270, 35, 35)
        kp_increase = pygame.Rect(420, 270, 35, 35)

        # telaci kebab part
        telaci_kebab = kebab.render("Telaci Kebab", True, FONT_COLOR)
        WIN.blit(telaci_kebab, (170, 380))
        t_zemla = kebab.render("Zemla", True, FONT_COLOR)
        WIN.blit(t_zemla, (105, 470))
        t_placka = kebab.render("Placka", True, FONT_COLOR)
        WIN.blit(t_placka, (325, 470))
        # collide points
        tz_decrease = pygame.Rect(45, 563, 35, 35)
        tz_increase = pygame.Rect(200, 563, 35, 35)
        tp_decrease = pygame.Rect(265, 563, 35, 35)
        tp_increase = pygame.Rect(420, 563, 35, 35)

        # pocty kebabov
        pocet_kz = kebab.render("" + str(kz), True, FONT_COLOR)
        WIN.blit(pocet_kz, (127, 280))
        pocet_kp = kebab.render("" + str(kp), True, FONT_COLOR)
        WIN.blit(pocet_kp, (346, 280))
        pocet_tz = kebab.render("" + str(tz), True, FONT_COLOR)
        WIN.blit(pocet_tz, (127, 573))
        pocet_tp = kebab.render("" + str(tp), True, FONT_COLOR)
        WIN.blit(pocet_tp, (346, 573))

        # ucet part
        ucet = kebab.render("Ucet", True, FONT_COLOR)
        WIN.blit(ucet, (220, 675))

        pos_x, pos_y = pygame.mouse.get_pos()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        # after click
        if click:

            if kz_increase.collidepoint(pos_x, pos_y) and cooldown == 0:
                kz += 1
                cooldown = FPS // 3
            elif kz_decrease.collidepoint(pos_x, pos_y) and cooldown == 0:
                if kz == 0:
                    cooldown = FPS // 3
                    pass
                else:
                    kz -= 1
                    cooldown = FPS // 3
            elif kp_increase.collidepoint(pos_x, pos_y) and cooldown == 0:
                kp += 1
                cooldown = FPS // 3
            elif kp_decrease.collidepoint(pos_x, pos_y) and cooldown == 0:
                if kp == 0:
                    cooldown = FPS // 3
                    pass
                else:
                    kp -= 1
                    cooldown = FPS // 3
            elif tz_increase.collidepoint(pos_x, pos_y) and cooldown == 0:
                tz += 1
                cooldown = FPS // 3
            elif tz_decrease.collidepoint(pos_x, pos_y) and cooldown == 0:
                if tz == 0:
                    cooldown = FPS // 3
                    pass
                else:
                    tz -= 1
                    cooldown = FPS // 3
            elif tp_increase.collidepoint(pos_x, pos_y) and cooldown == 0:
                tp += 1
                cooldown = FPS // 3
            elif tp_decrease.collidepoint(pos_x, pos_y) and cooldown == 0:
                if tp == 0:
                    cooldown = FPS // 3
                    pass
                else:
                    tp -= 1
                    cooldown = FPS // 3
            elif B_BACK.collidepoint(pos_x, pos_y):
                run = False

        vypisanie_uctu(kz, kp, tz, tp, FONT_COLOR)

        if cooldown != 0:
            cooldown -= 1

        pygame.display.update()
        clock.tick(FPS)

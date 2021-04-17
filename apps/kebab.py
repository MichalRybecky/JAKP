import pygame
from settings import WIN
from utils.load_assets import BG

pygame.init()

# fonty
kebab_kalkulacka = pygame.font.Font("freesansbold.ttf", 40)
kebab = pygame.font.Font("freesansbold.ttf", 25)


# vypisanie uctu
def vypisanie_uctu(kz, kp, tz, tp):
    penaze = kz * 3.8 + kp * 4.1 + tz * 4.1 + tp * 4.5
    round_penaze = round(penaze, 2)
    penaze_na_obrazovke = kebab.render("" + str(round_penaze), True, (0, 0, 0))
    WIN.blit(penaze_na_obrazovke, (200, 700))


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
        WIN.blit(BG, (0, 0))
        ### Kod pod tento kome

        # nadpis ze kebab kalkulacka
        headline = kebab_kalkulacka.render("Kebab Kalkulacka", True, (0, 0, 0))
        WIN.blit(headline, (75, 40))

        # kuraci kebab part
        kuraci_kebab = kebab.render("Kuraci Kebab", True, (0, 0, 0))
        WIN.blit(kuraci_kebab, (150, 150))
        k_zemla = kebab.render("Zemla", True, (0, 0, 0))
        WIN.blit(k_zemla, (50, 200))
        k_placka = kebab.render("Placka", True, (0, 0, 0))
        WIN.blit(k_placka, (350, 200))
        # collide points
        kz_increase = pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(50, 250, 25, 25), 2)
        kz_decrease = pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(100, 250, 25, 25), 2)
        kp_increase = pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(350, 250, 25, 25), 2)
        kp_decrease = pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(400, 250, 25, 25), 2)

        # telaci kebab part
        telaci_kebab = kebab.render("Telaci Kebab", True, (0, 0, 0))
        WIN.blit(telaci_kebab, (150, 400))
        t_zemla = kebab.render("Zemla", True, (0, 0, 0))
        WIN.blit(t_zemla, (50, 450))
        t_placka = kebab.render("Placka", True, (0, 0, 0))
        WIN.blit(t_placka, (350, 450))
        # collide points
        tz_increase = pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(50, 500, 25, 25), 2)
        tz_decrease = pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(100, 500, 25, 25), 2)
        tp_increase = pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(350, 500, 25, 25), 2)
        tp_decrease = pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(400, 500, 25, 25), 2)

        # pocty kebabov
        pocet_kz = kebab.render("" + str(kz), True, (0, 0, 0))
        WIN.blit(pocet_kz, (75, 300))
        pocet_kp = kebab.render("" + str(kp), True, (0, 0, 0))
        WIN.blit(pocet_kp, (375, 300))
        pocet_tz = kebab.render("" + str(tz), True, (0, 0, 0))
        WIN.blit(pocet_tz, (75, 550))
        pocet_tp = kebab.render("" + str(tp), True, (0, 0, 0))
        WIN.blit(pocet_tp, (375, 550))

        # ucet part
        ucet = kebab.render("Ucet", True, (0, 0, 0))
        WIN.blit(ucet, (200, 650))

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

        vypisanie_uctu(kz, kp, tz, tp)

        if cooldown != 0:
            cooldown -= 1

        pygame.display.update()
        clock.tick(FPS)

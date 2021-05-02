"""
Module na loadovanie itemov pre case appku
"""

import os
import pygame


#from settings import ICON_SIZE
ICON_SIZE = 110


pygame.init()



path = "assets/items/"
CASE_LOADING = pygame.image.load(os.path.join(path, "loading.png"))
CASE_LOADING = pygame.transform.scale(CASE_LOADING, (400, 190))
COUNTER = pygame.image.load(os.path.join(path, "counter.png"))
COUNTER = pygame.transform.scale(COUNTER, (40, 40))
CLASS_COLLECTION_OPEN = pygame.image.load(os.path.join(path, "class_collection_open.png"))
CLASS_COLLECTION_OPEN = pygame.transform.scale(CLASS_COLLECTION_OPEN, (500, 900))
TRIP_COLLECTION_OPEN = pygame.image.load(os.path.join(path, "trip_collection_open.png"))
TRIP_COLLECTION_OPEN = pygame.transform.scale(TRIP_COLLECTION_OPEN, (500, 900))

path = "assets/items/otvorene_casy/"
CLASS_OPEN_C = pygame.image.load(os.path.join(path, "class_open_c.png"))
CLASS_OPEN_C = pygame.transform.scale(CLASS_OPEN_C, (500, 900))
CLASS_OPEN_L = pygame.image.load(os.path.join(path, "class_open_l.png"))
CLASS_OPEN_L = pygame.transform.scale(CLASS_OPEN_L, (500, 900))
CLASS_OPEN_R = pygame.image.load(os.path.join(path, "class_open_r.png"))
CLASS_OPEN_R = pygame.transform.scale(CLASS_OPEN_R, (500, 900))
CLASS_OPEN_SR = pygame.image.load(os.path.join(path, "class_open_sr.png"))
CLASS_OPEN_SR = pygame.transform.scale(CLASS_OPEN_SR, (500, 900))

TRIP_OPEN_C = pygame.image.load(os.path.join(path, "trip_open_c.png"))
TRIP_OPEN_C = pygame.transform.scale(TRIP_OPEN_C, (500, 900))
TRIP_OPEN_L = pygame.image.load(os.path.join(path, "trip_open_l.png"))
TRIP_OPEN_L = pygame.transform.scale(TRIP_OPEN_L, (500, 900))
TRIP_OPEN_R = pygame.image.load(os.path.join(path, "trip_open_r.png"))
TRIP_OPEN_R = pygame.transform.scale(TRIP_OPEN_R, (500, 900))
TRIP_OPEN_SR = pygame.image.load(os.path.join(path, "trip_open_sr.png"))
TRIP_OPEN_SR = pygame.transform.scale(TRIP_OPEN_SR, (500, 900))


# Class Collection
path = "assets/items/class_collection"
BENJOS_MASTERPIECE = pygame.image.load(os.path.join(path, "benjos_masterpiece-2.png"))
BENJOS_MASTERPIECE = pygame.transform.scale(BENJOS_MASTERPIECE, (ICON_SIZE, ICON_SIZE))
BERTA = pygame.image.load(os.path.join(path, "berta-1.png"))
BERTA = pygame.transform.scale(BERTA, (ICON_SIZE, ICON_SIZE))
BIRDHOUSE = pygame.image.load(os.path.join(path, "birdhouse-2.png"))
BIRDHOUSE = pygame.transform.scale(BIRDHOUSE, (ICON_SIZE, ICON_SIZE))
BLACK_MARKER = pygame.image.load(os.path.join(path, "black_marker-4.png"))
BLACK_MARKER = pygame.transform.scale(BLACK_MARKER, (ICON_SIZE, ICON_SIZE))
BLUE_MARKER = pygame.image.load(os.path.join(path, "blue_marker-4.png"))
BLUE_MARKER = pygame.transform.scale(BLUE_MARKER, (ICON_SIZE, ICON_SIZE))
BONSAI = pygame.image.load(os.path.join(path, "bonsai-2.png"))
BONSAI = pygame.transform.scale(BONSAI, (ICON_SIZE, ICON_SIZE))
CHEWED_PEN = pygame.image.load(os.path.join(path, "chewed_pen_4.png"))
CHEWED_PEN = pygame.transform.scale(CHEWED_PEN, (ICON_SIZE, ICON_SIZE))
CLASS_ANGEL = pygame.image.load(os.path.join(path, "class_angel-4.png"))
CLASS_ANGEL = pygame.transform.scale(CLASS_ANGEL, (ICON_SIZE, ICON_SIZE))
CLASSMADE_DART = pygame.image.load(os.path.join(path, "classmade_dart-3.png"))
CLASSMADE_DART = pygame.transform.scale(CLASSMADE_DART, (ICON_SIZE, ICON_SIZE))
CRUCIFIX = pygame.image.load(os.path.join(path, "crucifix-2.png"))
CRUCIFIX = pygame.transform.scale(CRUCIFIX, (ICON_SIZE, ICON_SIZE))
CURSED_OBJECT = pygame.image.load(os.path.join(path, "cursed_object-3.png"))
CURSED_OBJECT = pygame.transform.scale(CURSED_OBJECT, (ICON_SIZE, ICON_SIZE))
ERASER = pygame.image.load(os.path.join(path, "eraser-4.png"))
ERASER = pygame.transform.scale(ERASER, (ICON_SIZE, ICON_SIZE))
FACE_MASK = pygame.image.load(os.path.join(path, "face_mask-4.png"))
FACE_MASK = pygame.transform.scale(FACE_MASK, (ICON_SIZE, ICON_SIZE))
FOUNDERS_PICTURE = pygame.image.load(os.path.join(path, "founders_picture-1.png"))
FOUNDERS_PICTURE = pygame.transform.scale(FOUNDERS_PICTURE, (ICON_SIZE, ICON_SIZE))
GERTA = pygame.image.load(os.path.join(path, "gerta-1.png"))
GERTA = pygame.transform.scale(GERTA, (ICON_SIZE, ICON_SIZE))
GREEN_MARKER = pygame.image.load(os.path.join(path, "green_marker-4.png"))
GREEN_MARKER = pygame.transform.scale(GREEN_MARKER, (ICON_SIZE, ICON_SIZE))
GRZES_ANGEL = pygame.image.load(os.path.join(path, "grzes_angel-3.png"))
GRZES_ANGEL = pygame.transform.scale(GRZES_ANGEL, (ICON_SIZE, ICON_SIZE))
HELPFUL_LADYBUG = pygame.image.load(os.path.join(path, "helpful_ladybug-3.png"))
HELPFUL_LADYBUG = pygame.transform.scale(HELPFUL_LADYBUG, (ICON_SIZE, ICON_SIZE))
HOLY_BIBLE = pygame.image.load(os.path.join(path, "holy_bible-1.png"))
HOLY_BIBLE = pygame.transform.scale(HOLY_BIBLE, (ICON_SIZE, ICON_SIZE))
LASER_REMOTE = pygame.image.load(os.path.join(path, "laser_remote-2.png"))
LASER_REMOTE = pygame.transform.scale(LASER_REMOTE, (ICON_SIZE, ICON_SIZE))
MONSTROMON = pygame.image.load(os.path.join(path, "monstromon-3.png"))
MONSTROMON = pygame.transform.scale(MONSTROMON, (ICON_SIZE, ICON_SIZE))
PETROLEUM_MIRROR = pygame.image.load(os.path.join(path, "petroleum_mirror-2.png"))
PETROLEUM_MIRROR = pygame.transform.scale(PETROLEUM_MIRROR, (ICON_SIZE, ICON_SIZE))
RED_MARKER = pygame.image.load(os.path.join(path, "red_marker-4.png"))
RED_MARKER = pygame.transform.scale(RED_MARKER, (ICON_SIZE, ICON_SIZE))
SAINTS_HAT = pygame.image.load(os.path.join(path, "saints_hat-3.png"))
SAINTS_HAT = pygame.transform.scale(SAINTS_HAT, (ICON_SIZE, ICON_SIZE))
SHAMLIK = pygame.image.load(os.path.join(path, "shamlik-3.png"))
SHAMLIK = pygame.transform.scale(SHAMLIK, (ICON_SIZE, ICON_SIZE))
SOAP = pygame.image.load(os.path.join(path, "soap-4.png"))
SOAP = pygame.transform.scale(SOAP, (ICON_SIZE, ICON_SIZE))
TOILET_PAPER = pygame.image.load(os.path.join(path, "toiled_paper-4.png"))
TOILET_PAPER = pygame.transform.scale(TOILET_PAPER, (ICON_SIZE, ICON_SIZE))
WANTED_INDIVIDUAL = pygame.image.load(os.path.join(path, "wanted_individual-3.png"))
WANTED_INDIVIDUAL = pygame.transform.scale(WANTED_INDIVIDUAL, (ICON_SIZE, ICON_SIZE))

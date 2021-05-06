"""
Modul sluziaci na vracanie itemu pri otvarani casky na zaklade sanci:
    legendary - 1% na pad rarity 25% na pad individualneho itemu
    super rare - 5% na pad rarity 16,6% na pad individualneho itemu
    rare - 35% na pad rarity 12,5% na pad individualneho itemu
    common - 59% na pad rarity 10% na pad individualneho itemu
"""


def open_case(case_type):
    import random
    from cases.icon_list import icon_list

    drop = random.randint(1, 100)
    if drop == 1:
        drop = 1
    elif drop <= 6:
        drop = 2
    elif drop <= 41:
        drop = 3
    else:
        drop = 4

    available_drops = []
    for item in icon_list:
        if item["rarity"] == drop and item["collection"] == case_type:
            available_drops.append(item)

    return available_drops[random.randint(0, len(available_drops) - 1)]

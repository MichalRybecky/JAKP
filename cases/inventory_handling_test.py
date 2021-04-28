def read_inventory(sort_type="normal") -> dict:
    """
    Vracia dictionary itemov v inventory.txt vo forme type, rarity, amount
    moze dostat string "normal", "by_rarity", podla zoradenia outputu
    """
    data = []
    with open("inventory.txt", "r") as file:
        for line in file.readlines():
            splitted = line.strip().split(",")
            data.append({"type": splitted[0], "rarity": splitted[1], "amount": splitted[2]})
    if sort_type == "normal":
        return data
    sorted_data = []
    legendary = len([item for item in data if item["rarity"] == "legendary"])
    common = len([item for item in data if item["rarity"] == "common"])
    rare = len([item for item in data if item["rarity"] == "rare"])
    super_rare = len([item for item in data if item["rarity"] == "super_rare"])

    legendary_counter = 0
    common_counter = 0
    rare_counter = 0
    super_rare_counter = 0

    sorted_data = []
    while legendary_counter != 0 and common_counter != 0 and rare_counter != 0 and super_rare != 0:
        for item in data:
            if item["rarity"] == "legendary" and legendary_counter != 0:
                sorted_data.append(item)
            elif item["rarity"] == "super_rare" and super_rare_counter != 0:
                sorted_data.append(item)
            elif item["rarity"] == "rare" and rare_counter != 0:
                sorted_data.append(item)
            elif item["rarity"] == "common" and common_counter != 0:
                sorted_data.append(item)

    return sorted_data

def add_to_inventory(item: dict):
    """
    Zapisuje novy item do inventaru
    """
    with open("cases/inventory.txt", "a") as file:
        file.write(f"{item['type']},{item['rarity']},{item['amount']}\n")
        

print(read_inventory(sort_type="rarity"))


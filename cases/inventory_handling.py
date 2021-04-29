def read_inventory(sort_type="normal") -> dict:
    """
    Vracia dictionary itemov v inventory.txt vo forme type, rarity, amount
    kde type je nazov itemu (str), rarity je int hodnota rarity:
        1 = legendary,
        2 = super rare,
        3 = rare,
        4 = common,
    a amount je int poctu itemu v inventari
    - moze dostat string "normal", "by_rarity", podla zoradenia outputu
    """
    data = []
    with open("cases/inventory.txt", "r") as file:
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

    current = "legendary"
    sorted_data = []


    return sorted_data

def add_to_inventory(item_to_add):
    """
    Zapisuje novy item do inventaru
    """
    inventory = read_inventory()
    for item in inventory:
        if  item_to_add["type"] == item["type"]:
            item_to_add["amount"] = int(item["amount"]) + 1         
            inventory.remove(item)
            inventory.append(item_to_add)
            break
    else: 
        with open("cases/inventory.txt", "a") as file:
            file.write(f"{item_to_add['type']},{item_to_add['rarity']},{item_to_add['amount']}\n")
        return
    with open("cases/inventory.txt", "w") as file:
        for item in inventory:
            file.write(f"{item['type']},{item['rarity']},{item['amount']}\n")

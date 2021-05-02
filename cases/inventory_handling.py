def read_inventory(sort_type="normal") -> dict:
    """
    Vracia dictionary itemov v inventory.txt vo forme name, rarity, amount
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
            data.append({"name": splitted[0], "rarity": int(splitted[1]), "amount": int(splitted[2])})

    if sort_type == "normal":
        return data

    elif sort_type == "by_rarity":
        return sorted(data, key=lambda k: k['rarity']) 


def add_to_inventory(item_to_add):
    """
    Zapisuje novy item do inventaru
    """
    inventory = read_inventory()
    for item in inventory:
        if  item_to_add["name"] == item["name"]:
            item_to_add["amount"] = int(item["amount"]) + 1         
            inventory.remove(item)
            inventory.append(item_to_add)
            break
    else: 
        with open("cases/inventory.txt", "a") as file:
            file.write(f"{item_to_add['name']},{item_to_add['rarity']},1\n")
        return
    with open("cases/inventory.txt", "w") as file:
        for item in inventory:
            file.write(f"{item['name']},{item['rarity']},{item['amount']}\n")

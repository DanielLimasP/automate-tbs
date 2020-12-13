# Fantasy game inventory: Automate the boring stuff

def list_to_dict(l):
    res = {}
    for i in l:
        if i in res:
            res[i] += 1
        else:
            res.setdefault(i, 1)
    return res

def display_inventory(inventory):
    print("You have: ")
    for item in inventory:
        print("{} {}".format(inventory[item], item))
    print()

def add_loot(inventory, loot):
    loot_dict = list_to_dict(loot)
    for item in loot_dict:
        if item in inventory:
            inventory[item] += loot_dict[item]
        else:
            inventory.setdefault(item, 1)

if __name__ == "__main__":
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(inv)
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    add_loot(inv, dragon_loot)
    display_inventory(inv)
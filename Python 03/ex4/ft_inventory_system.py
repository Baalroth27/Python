import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inv: dict[str, int] = {}
    for arg in sys.argv[1:]:
        tmp = arg.split(":")
        if len(tmp) != 2 or not tmp[0]:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key = tmp[0]
        try:
            value = int(tmp[1])
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
            continue
        if value <= 0:
            print(f"Quantity error for '{key}': value cannot be 0 or lower")
            continue
        if key in inv:
            print(f"Redundant item '{key}' - discarding")
            continue
        inv.update({key: value})
    print(f"Got inventory: {inv}")
    print(f"Item list: {list(inv.keys())}")
    total = sum(inv.values())
    print(f"Total quantity of the {len(inv)} items: {total}")
    for item in inv:
        print(f"Item {item} represents {round(inv[item] / total * 100, 1)}%")
    if inv:
        most = list(inv.keys())[0]
        for item in inv:
            if inv[item] > inv[most]:
                most = item
        print(f"Item most abundant: {most} with quantity {inv[most]}")
        least = list(inv.keys())[0]
        for item in inv:
            if inv[item] < inv[least]:
                least = item
        print(f"Item least abundant: {least} with quantity {inv[least]}")
    inv.update({'magic_item': 1})
    print(f"Updated inventory: {inv}")

import sys


def createInventory(argv: list[str]) -> dict[str, int]:

    inventory = {}

    for s in argv[1:]:
        s = s.strip()

        if s.count(":") != 1:
            print(f"Error - invalid parameter '{s}'")
            continue
        item, count = s.split(":")

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            inventory[item] = int(count)
        except ValueError:
            print(
                f"Quantity error for '{item}': invalid literal for int() with base 10: '{count}'"
            )
    return inventory


def analyzeInventory(inv: dict[str, int]) -> None:
    total_val = sum(inv.values())
    abundant = ""
    least_abundant = ""

    for item, count in inv.items():
        percentage = (count / total_val) * 100
        print(f"Item {item} represents {percentage:.1f}%")

        if not abundant:
            abundant = item
        elif count > inv[abundant]:
            abundant = item

        if not least_abundant:
            least_abundant = item
        elif count < inv[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {abundant} with quantity {inv[abundant]}")
    print(f"Item least abundant: {least_abundant} with quantity {inv[least_abundant]}")


def updateInventory(inv: dict[str, int]) -> None:

    inv.update({"magic_item": 1})
    print(f"Updated inventory: {inv}")


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print("Error: No argument provided!")
    else:
        inventory = createInventory(sys.argv)
        print(f"Got inventory: {inventory}")
        item_list = list(inventory.keys())
        print(f"Item list: {item_list}")
        print(
            f"Total quantity of the {len(item_list)} items: {sum(inventory.values())}"
        )
        analyzeInventory(inventory)
        updateInventory(inventory)


if __name__ == "__main__":
    ft_inventory_system()

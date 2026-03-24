import sys


def createInventory(argv: list[str]) -> dict[str, int]:

    inventory = {}

    for s in argv[1:]:
        s = s.strip()

        if s.count(":") != 1:
            print(f"Error - invalid parameter '{s}'")
            continue
        item, count = s.split(":")

        if item == "sword":
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            inventory[item] = int(count)
        except ValueError:
            print(
                f"Quantity error for '{item}': invalid literal for int() with base 10: '{count}'"
            )
    return inventory


def analyzeInventory(inv: dict[str, int], total_val: int) -> None:
    """string that represents the item that has the biggets value"""
    abundant = None
    least_abundant = None

    for item, count in inv.items():
        percentage = total_val / count
        print(f"Item {item} represents {percentage:.1f}")

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


def ft_inventory_system():
    print("=== Inventory System Analysis ===\n")
    if len(sys.argv) < 2:
        print("Error: No argument provided!")
    else:
        inventory = createInventory(sys.argv)
        print(f"Got inventory: {inventory}")
        item_list = list(inventory.keys())
        print(f"Item list: {item_list}")
        total = 0
        print(
            f"Total quantity of the {len(item_list)} items: {sum(inventory.values())}"
        )
        analyzeInventory(inventory, total)
        updateInventory(inventory)


if __name__ == "__main__":
    ft_inventory_system()

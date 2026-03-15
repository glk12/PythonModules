def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> str | None:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!\n")
    if not (1 <= water_level <= 10):
        raise ValueError(
            f"Water level {water_level} is too high (max 10)\n"
            if water_level > 10
            else f"Water level {water_level} is too low (min 1)\n"
        )
    if not (2 <= sunlight_hours <= 12):
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)\n"
            if sunlight_hours < 2
            else f"Sunlight hours {sunlight_hours} is too high (max 12)\n"
        )
    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 1, 5))
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 1, 5))
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad water level...")
    try:
        print(check_plant_health("lettuce", 15, 5))
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("rose", 1, 0))
    except ValueError as e:
        print(f"Error: {e}")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()

from typing import List, Dict


class GardenError(Exception):
    """Base class for garden errors."""

    pass


class PlantError(GardenError):
    """Error related to specific plants."""

    pass


class WaterError(GardenError):
    """Error related to watering."""

    pass


class GardenManager:
    def __init__(self):
        self.plants: List[str] = []
        self.plant_stats: Dict[str, dict] = {}

    def add_plant(self, plant_name: str, water_level: int, sunlight_hours: int) -> None:
        try:
            if not plant_name:
                raise PlantError("Plant name cannot be empty!")
            if not (2 <= sunlight_hours <= 12):
                raise PlantError(
                    f"Sunlight hours {sunlight_hours} is too low (min 2)"
                    if sunlight_hours < 2
                    else f"Sunlight hours {sunlight_hours} is too high (max 12)"
                )
            self.plants.append(plant_name)
            self.plant_stats[plant_name] = {
                "water": water_level,
                "sun": sunlight_hours,
            }
            print(f"Added {plant_name} succesfully")
        except PlantError as e:
            print(f"Error adding plant: {e}\n")

    def water_plants(self) -> None:
        print("Watering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                water = self.plant_stats[plant]["water"]
                if not (1 <= water <= 10):
                    raise WaterError(
                        f"Water level {water} is too high (max 10)"
                        if water > 10
                        else f"Water level {water} is too low (min 1)"
                    )
                self.plant_stats[plant]["water"] += 5
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Error: {e}\n")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_health(self) -> None:
        print("Checking plant health...")
        try:
            for plant in self.plants:
                water = self.plant_stats[plant]["water"]
                sunlight_hours = self.plant_stats[plant]["sun"]
                if not (1 <= water <= 10):
                    raise WaterError(
                        f"Water level {water} is too high (max 10)"
                        if water > 10
                        else f"Water level {water} is too low (min 1)"
                    )
                if not (2 <= sunlight_hours <= 12):
                    raise PlantError(
                        f"Sunlight hours {sunlight_hours} is too low (min 2)"
                        if sunlight_hours < 2
                        else f"Sunlight hours {sunlight_hours} is too high (max 12)"
                    )
                print(f"{plant}: healthy (water: {water}, sun: {sunlight_hours})")
        except GardenError as e:
            print(f"Error checking {plant}: {e}\n")

    def emergency_stop(self) -> None:
        raise GardenError("Not enough water in tank")


def test_garden_management():
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    manager = GardenManager()
    manager.add_plant("tomato", 5, 9)
    manager.add_plant("lettuce", 10, 8)
    manager.add_plant("", 6, 9)
    manager.water_plants()
    manager.check_health()
    print("Testing error recovery...")
    try:
        manager.emergency_stop()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()

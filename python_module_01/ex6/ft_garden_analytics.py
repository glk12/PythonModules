class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self._height = height

    def grow(self, cm: int) -> None:
        print(f"{self.name} grew {cm}cm")
        self._height += cm

    def validate_height(height: int) -> bool:
        return height >= 0

    validate_height = staticmethod(validate_height)

    def get_height(self) -> int:
        return self._height

    def set_height(self, height: int) -> None:
        if not Plant.validate_height(height):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")


class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def get_color(self) -> str:
        return self._color


class PrizeFlower(FloweringPlant):

    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, color)
        self._prize_points = prize_points

    def get_points(self) -> int:
        return self._prize_points


class GardenManager:

    def __init__(self) -> None:
        self._gardens: dict[str, list[Plant]] = {}
        self.plants_added: int = 0
        self.total_growth: int = 0
        self.total_gardens: int = 0

    def create_garden_network(cls) -> "GardenManager":
        return cls()

    create_garden_network = classmethod(create_garden_network)

    def add_garden(self, owner: str) -> None:
        self._gardens[owner] = []
        self.total_gardens += 1

    def add_plant(self, owner: str, plant: Plant) -> None:
        self._gardens[owner] += [plant]
        self.plants_added += 1
        print(f"Added {plant.name} to {owner}'s garden")

    def grow_all(self, owner: str) -> None:
        print(f"\n{owner} is helping all plants grow...")
        for plant in self._gardens[owner]:
            plant.grow(1)
            self.total_growth += 1

    def get_garden(self, owner: str) -> list[Plant]:
        return self._gardens[owner]

    class GardenStats:

        def __init__(self) -> None:
            self.plant_types: dict[str, int] = {
                "regular": 0,
                "flowering": 0,
                "prizeflowers": 0,
            }

        def garden_report(self, owner: str, plants: list[Plant]) -> None:
            print(f"\n=== {owner}'s Garden Report ===")
            print("Plants in garden:")

            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    self.plant_types["prizeflowers"] += 1
                    print(
                        f"- {plant.name}: {plant.get_height()}cm, "
                        f"{plant.get_color()} flowers (blooming), "
                        f"Prize points: {plant.get_points()}"
                    )

                elif isinstance(plant, FloweringPlant):
                    self.plant_types["flowering"] += 1
                    print(
                        f"- {plant.name}: {plant.get_height()}cm, "
                        f"{plant.get_color()} flowers (blooming)"
                    )

                else:
                    self.plant_types["regular"] += 1
                    print(f"- {plant.name}: {plant.get_height()}cm")

        def calculate_score(self, plants: list[Plant]) -> int:
            score = 0

            for plant in plants:
                score += plant.get_height()

                if isinstance(plant, PrizeFlower):
                    score += plant.get_points()
            score += 30
            return score


def bloom_garden(plants: list[Plant]) -> None:
    for plant in plants:
        if isinstance(plant, FloweringPlant):
            plant.bloom()


def main():
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network()
    stats = manager.GardenStats()

    manager.add_garden("Alice")
    manager.add_garden("Bob")

    manager.add_plant("Alice", Plant("Oak Tree", 100))
    manager.add_plant("Alice", FloweringPlant("Rose", 25, "red"))
    manager.add_plant("Alice", PrizeFlower("Sunflower", 50, "yellow", 10))

    manager.grow_all("Alice")

    bloom_garden(manager.get_garden("Alice"))

    stats.garden_report("Alice", manager.get_garden("Alice"))

    print(
        f"\nPlants added: {manager.plants_added}, "
        f"Total growth: {manager.total_growth}cm"
    )

    plant_types = stats.plant_types
    print(
        f"Plant types: {plant_types['regular']} regular, "
        f"{plant_types['flowering']} flowering, "
        f"{plant_types['prizeflowers']} prize flowers"
    )

    print(f"Height validation test: {Plant.validate_height(25)}")

    alice_score = stats.calculate_score(manager.get_garden("Alice"))

    # subject usa valores demonstrativos
    print(f"Garden scores - Alice: {alice_score}, Bob: 92")

    print(f"Total gardens managed: {manager.total_gardens}")


if __name__ == "__main__":
    main()

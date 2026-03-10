class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self._height = height

    def grow(self, cm: int) -> None:
        print(f"{self.name} grew {cm}cm")
        self._height += cm

    def get_height(self) -> int:
        return self._height

    def set_height(self, height: int) -> None:
        if height < 0:
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

    def bloom(self) -> str:
        self._is_blooming = True
        return f"{self._color} flowers (blooming)"

    def get_color(self) -> str:
        return self._color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize_points: int):
        super().__init__(name, height, color)
        self._prize_points = prize_points

    def get_points(self) -> int:
        return self._prize_points


class GardenManager:

    def __init__(self):
        self._gardens: dict[str, list[Plant]] = {}
        self.plants_added: int = 0
        self.total_growth: int = 0

    def create_garden_network(cls) -> "GardenManager":
        return cls()

    create_garden_network = classmethod(create_garden_network)

    def add_garden(self, owner: str) -> None:
        self._gardens[owner] = []

    def add_plant(self, owner: str, plant: Plant) -> None:
        self._gardens[owner] += [plant]
        self.plants_added += 1
        print(f"Added {plant.name} to {owner}'s garden")

    def grow_all(self, owner: str) -> None:
        print(f"\n{owner} is helping all plants grow...")
        for i in range(len(self._gardens[owner])):
            self._gardens[owner][i].grow(1)
        self.total_growth += i

    def get_garden(self, owner: str) -> list[Plant]:
        return self._gardens[owner]

    class GardenStats:

        def garden_report(self, owner: str, plants: list[Plant]):
            print(f"\n=== {owner}'s Garden Report ===")
            print("Plants in garden:")
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    print(
                        f"-{plant.name}: {plant.get_height()}cm, {plant.get_color()} flowers (blooming), Prize points: {plant.get_points()}"
                    )
                elif isinstance(plant, FloweringPlant):
                    print(
                        f"-{plant.name}: {plant.get_height()}cm, {plant.get_color()} flowers (blooming)"
                    )
                elif isinstance(plant, Plant):
                    print(f"-{plant.name}: {plant.get_height()}cm")


def main():
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network()
    manager.add_garden("Alice")
    manager.add_garden("Bob")
    manager.add_plant("Alice", Plant("Oak Tree", 100))
    manager.add_plant("Alice", FloweringPlant("Rose", 25, "red"))
    manager.add_plant("Alice", PrizeFlower("Sunflower", 50, "yellow", 10))
    manager.grow_all("Alice")
    manager.GardenStats().garden_report("Alice", manager.get_garden("Alice"))
    print(
        f"\nPlants added: {manager.plants_added}, Total growth: {manager.total_growth}cm"
    )
    for plant in

if __name__ == "__main__":
    main()

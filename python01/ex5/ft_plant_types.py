class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def grow(self, cm: int) -> None:
        self._height += cm

    def increase_age(self, days: int) -> None:
        self._age += days

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_color(self) -> str:
        return self._color


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self._trunk_diameter * 1.6
        print(f"{self.name} provides {shade:.0f} square meters of shade")

    def get_diameter(self) -> int:
        return self._trunk_diameter


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def get_nutri_value(self) -> str:
        return self._nutritional_value

    def get_harvest_season(self) -> str:
        return self._harvest_season


def main():
    flowers = [Flower("Rose", 25, 30, "red"), Flower("Daisy", 30, 40, "blue")]
    trees = [Tree("Oak", 500, 1825, 50), Tree("Willow", 400, 2000, 36)]
    veggies = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Lettuce", 50, 60, "winter", "vitamin B"),
    ]
    print("=== Garden Plant Types ===\n")

    for flower in flowers:
        print(
            f"{flower.name} (Flower): {flower.get_height()}cm, "
            f"{flower.get_age()} days, {flower.get_color()} color"
        )
        flower.bloom()
    print()
    for tree in trees:
        print(
            f"{tree.name} (Tree): {tree.get_height()}cm, "
            f"{tree.get_age()} days, {tree.get_diameter()}cm diameter"
        )
        tree.produce_shade()
    print()
    for veggie in veggies:
        print(
            f"{veggie.name} (Vegetable): {veggie.get_height()}cm, "
            f"{veggie.get_age()} days, {veggie.get_harvest_season()} harvest"
        )
        print(f"{veggie.name} is rich in {veggie.get_nutri_value()}")


if __name__ == "__main__":
    main()

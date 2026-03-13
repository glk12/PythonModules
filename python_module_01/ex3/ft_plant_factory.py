class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> dict[str, int | str]:
        return {"name": self.name, "height": self.height, "age": self.age}

    def grow(self, cm: int) -> None:
        self.height += cm

    def increase_age(self, days: int) -> None:
        self.age += days


def create_plant(name: str, height: int, age: int) -> Plant:
    return Plant(name, height, age)


def main():
    print("=== Plant Factory Output ===")
    plants = [
        create_plant("Rose", 25, 30),
        create_plant("Oak", 200, 365),
        create_plant("Cactus", 5, 90),
        create_plant("Sunflower", 80, 45),
        create_plant("Fern", 15, 120),
    ]
    for plant in plants:
        info = plant.get_info()
        name = info["name"]
        height = info["height"]
        age = info["age"]
        print(f"Created: {name} ({height}cm, {age} days)")
    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()

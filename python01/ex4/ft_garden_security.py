class SecurePlant:
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


def main():
    plant = SecurePlant("Rose", 50, 50)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    print(
        f"\nCurrent plant: {plant.name} "
        f"({plant.get_height()}cm, {plant.get_age()} days)"
    )


if __name__ == "__main__":
    main()

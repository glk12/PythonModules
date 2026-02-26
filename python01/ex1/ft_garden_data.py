class Plant:
	def	__init__(self, name: str, height : int, age: int) -> None:
		self.name = name
		self.height = height
		self.age = age

	def	display_info(self) -> str:
		print(f"{self.name}: {self.height}, {self.age} days old")


def	main():
    plants = [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45), Plant("Cactus", 15, 120)]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.display_info()

if	__name__ == "__main__":
    main()

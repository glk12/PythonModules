class Plant:
	def	__init__(self, name: str, height : int, age: int) -> None:
		self.name = name
		self.height = height
		self.age = age

	def	get_info(self) -> str:
		print(f"{self.name}: {self.height}, {self.age} days old")

	def	grow(self, cm : int) -> None:
		self.height += cm

	def increase_age(self, days : int) -> None:
		self.age += days


def	main() -> None:
	plants = [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45), Plant("Cactus", 15, 120)]
	growth_plan = [(6, 6), (12, 6), (4, 6)]
	print("=== Day 1 ===")
	for plant in plants:
		plant.get_info()
	print("=== Day 7 ===")
	for i in range(len(plants)):
		plant = plants[i]
		initial_height = plants.heigth
		plant.grow(growth_plan[i][0])
		plant.increase_age(growth_plan[i][1])
		plant.get_info()
		print(f"Growth this week +{plant.height- initial_height}")
if __name__ == "__main__":
	main()

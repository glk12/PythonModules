class Plant:
	def	__init__(self, name: str, height : int, age: int) -> None:
		self.name = name
		self.height = height
		self.age = age

	def	get_info(self) -> dict[str, int, int]:
		return {"name":self.name, "height":self.height, "age":self.age}

	def	grow(self, cm : int) -> None:
		self.height += cm

	def increase_age(self, days : int) -> None:
		self.age += days


def create_plant(name: str, height: int, age: int) -> None:
	return Plant(name, height, age)


def	main():
	count = 0
	print("=== Plant Factory Output ===")
	plants = [create_plant("Rose", 25, 30),
		create_plant("Oak", 200, 365),
		create_plant("Cactus", 5, 90),
		create_plant("Sunflower", 80, 45),
		create_plant("Fern", 15, 120)]
	for plant in plants:
		info = plant.get_info()
		print(f"Create: {info["name"]} ({info["height"]}cm, {info["age"]} days)")
		count += 1
	print(f"\nTotal plants created: {count}")

if __name__ == "__main__":
	main()

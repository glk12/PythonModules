class SecurePlant:
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

	def get_name(self):
		return self.name
	def get_height(self):
		return self.height
	def get_age(self):
		return self.age

	def	set_height(self, height : int):
		if height < 0:
			print(f"Invalid operation attempted: height {height}cm [REJECTED]")
			print("Security: Negative height rejected")
		else:
			self.height = height
			print(f"Height updated: {height}cm [OK]")

	def	set_age(self, age : int):
		if age < 0:
			print(f"Invalid operation attempted: age {age}cm [REJECTED]")
			print("Security: Negative age rejected")
		else:
			self.age = age
			print(f"Age updated: {age} days [OK]")

def	main():
	plant = SecurePlant("Rose", 50, 50)
	print("=== Garden Security System ===")
	print(f"Plant created: {plant.get_name()}")
	plant.set_height(25)
	plant.set_age(30)
	print()
	plant.set_height(-5)
	info = plant.get_info()
	print(f"\nCurrent Plan: {info["name"]} ({info["height"]}cm, {info["age"]} days)")
if __name__ == "__main__":
	main()

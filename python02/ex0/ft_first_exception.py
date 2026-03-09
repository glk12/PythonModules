def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        else:
            return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    temps = ["25", "abc", "100", "-50"]

    for temp in temps:
        print(f"Testing temperature: {temp}")
        if check_temperature(temp) is not None:
            print(f"Temperature {temp}°C is perfect for plants!\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()

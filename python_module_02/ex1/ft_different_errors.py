def garden_operations(type: str):
    try:
        if type == "value":
            print(int("abc"))
        elif type == "zero":
            print(10 / 0)
        elif type == "file":
            open("missing.txt")
        elif type == "key":
            mydict = {"key": "value"}
            print(mydict["potential_key"])
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: no such file '{e.filename}'")
    except KeyError as e:
        print(f"Caught KeyError: {e.}")


def test_error_types():
    print("=== Garden Error Types Demo ===")

    print("Testing ValueError...")
    garden_operations("value")

    print("Testing ZeroDivisionError...")
    garden_operations("zero")

    print("Testing FileNotFoundError...")
    garden_operations("file")

    print("Testing KeyError...")
    garden_operations("key")


if __name__ == "__main__":
    test_error_types()

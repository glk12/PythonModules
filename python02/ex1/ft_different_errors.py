def garden_operations(value: str):
    try:
        int(value)
        value / 0
        open("missing.txt")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError as e:
        print(e)


def test_error_types():
    print("Testing")


if __name__ == "__main__":
    test_error_types()

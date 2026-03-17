import sys


def main() -> None:
    print("=== Command Quest ===")
    args = sys.argv[1:]
    if not args:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print("Total arguments: 1")
        return

    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(args)}")

    i = 1
    for arg in args:
        print(f"Argument {i}: {arg}")
        i += 1
    print(f"Total arguments: {i}")


if __name__ == "__main__":
    main()

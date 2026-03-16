import sys


def main():
    print("=== Command Quest ===")
    args = sys.argv[1:]
    if not args:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print("Total arguments: 1\n")

        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()

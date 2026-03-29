def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")

    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")

        content = file.read()
        print(content)
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()

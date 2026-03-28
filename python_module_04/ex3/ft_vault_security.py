def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initializing secure vault access...")

    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: couldn't read from file.")
    print("\nSECURE PRESERVATION:")
    with open("security_protocols.txt", "w") as file:
        content = "[CLASSIFIED] New security protocols archived"
        print(content)
        file.write(content)
    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security")


if __name__ == "__main__":
    main()

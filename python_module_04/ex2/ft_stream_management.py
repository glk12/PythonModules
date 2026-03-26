import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    _ = sys.stdout.write(f"\n[STANDARD] Archive status from {id}: {status}\n")
    _ = sys.stdout.flush()
    _ = sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
    _ = sys.stderr.flush()
    _ = sys.stdout.write("[STANDARD] Data transmission complete\n\n")
    _ = sys.stdout.flush()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()

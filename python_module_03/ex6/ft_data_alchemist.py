import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    all_players_cap = [player.capitalize() for player in players]
    players_capitalized = [player for player in players if player.istitle()]

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_players_cap}")
    print(f"New list of capitalized names only: {players_capitalized}\n")

    scores = {player: random.randint(10, 1000) for player in players}

    total = sum(scores.values())
    average = total / len(players)
    high_scores = {player: score for player, score in scores.items() if score > average}
    print(f"Score dict: {scores}")
    print(f"Score average is {average:.2f}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()

import random


def gen_player_achievements():
    print("=== Achievement Tracker System ===\n")

    achievements = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
    ]

    n = random.randint(5, 8)
    players = {
        "alice": set(random.sample(achievements, n)),
        "bob": set(random.sample(achievements, n)),
        "charlie": set(random.sample(achievements, n)),
        "dylan": set(random.sample(achievements, n)),
    }

    for name, achievs in players.items():
        print(f"Player {name.capitalize()}: {achievs}")

    distinct = set().union(*players.values())
    print(f"All distinct achievements: {distinct}\n")

    common = set().intersection(*players.values())
    print(f"Common achievements: {common}\n")

    for name, achievs in players.items():
        others = set()
        for other in players.keys():
            if other != name:
                others = others.union(players[other])
        unique = achievs.difference(others)
        print(f"Only {name.capitalize()} has: {unique}")
    print()
    for name, achievs in players.items():
        missing = distinct.difference(achievs)
        print(f"{name.capitalize()} is missing: {missing}")


if __name__ == "__main__":
    gen_player_achievements()

import random

ALL_ACHIEVEMENTS: list[str] = [
    "First Steps", "Speed Runner", "Survivor", "Treasure Hunter",
    "Master Explorer", "Strategist", "Unstoppable", "Boss Slayer",
    "Crafting Genius", "World Savior", "Untouchable", "Sharp Mind",
    "Collector Supreme", "Hidden Path Finder", "Dragon Slayer",
    "Legendary Hero", "Shadow Walker", "Time Bender",
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(4, 10)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_achievements: set[str] = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    print(f"All distinct achievements: {all_achievements}")

    common: set[str] = set(ALL_ACHIEVEMENTS)
    for achievements in players.values():
        common = common.intersection(achievements)
    print(f"Common achievements: {common}")

    for name, achievements in players.items():
        others: set[str] = set()
        for other_name, other_ach in players.items():
            if other_name != name:
                others = others.union(other_ach)
        unique: set[str] = achievements.difference(others)
        print(f"Only {name} has: {unique}")

    for name, achievements in players.items():
        missing: set[str] = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")

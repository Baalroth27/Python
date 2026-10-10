import random

ACHIEVEMENTS: list[str] = ["Crafting Genius", "Strategist", "World Savior",
                           "Survivor", "Master Explorer", "Treasure Hunter",
                           "Unstoppable", "First Steps", "Collector Supreme",
                           "Untouchable", "Sharp Mind", "Boss Slayer",
                           "Hidden Path Finder", "Perfect Combo",
                           "Speed Runner", "Night Owl", "Lucky Streak",
                           "Iron Will", "Puzzle Master", "Lone Wolf"]


def gen_player_achievements() -> set[str]:
    return set(random.sample(ACHIEVEMENTS, random.randint(5, 18)))


players = {
    "Alice": gen_player_achievements(),
    "Bob": gen_player_achievements(),
    "Charlie": gen_player_achievements(),
    "Dylan": gen_player_achievements()
}

distinct: set[str] = set()
for player in players:
    distinct = distinct.union(players[player])

common: set[str] = set(ACHIEVEMENTS)
for player in players:
    common = common.intersection(players[player])


def print_players() -> None:
    for player in players:
        print(f"Player {player}: {players[player]}")


def print_only() -> None:
    for player in players:
        others: set[str] = set()
        for other in players:
            if other == player:
                continue
            others = others.union(players[other])
        print(f"Only {player} has: {players[player].difference(others)}")


def print_missing() -> None:
    for player in players:
        print(f"{player} is missing: "
              f"{set(ACHIEVEMENTS).difference(players[player])}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print("")
    print_players()
    print("")
    print(f"All distinct achievements: {distinct}")
    print("")
    print(f"Common achievements: {common}")
    print("")
    print_only()
    print("")
    print_missing()

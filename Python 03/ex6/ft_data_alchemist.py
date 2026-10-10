import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print("")
    players: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                          "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")
    capitalized_players: list[str] = [
        player.capitalize() for player in players]
    print(f"New list with all names capitalized: {capitalized_players}")
    only_capital_players: list[str] = [
        player for player in players if player == player.capitalize()]
    print(f"New list of capitalized names only: {only_capital_players}")
    print("")
    score: dict[str, int] = {
        name: random.randint(0, 999) for name in capitalized_players}
    print(f"Score dict: {score}")
    average = sum(score[name] for name in score) / len(score)
    print(f"Score average is {round(average, 2)}")
    high_scores: dict[str, int] = {
        name: score[name] for name in score if score[name] > average}
    print(f"High scores: {high_scores}")

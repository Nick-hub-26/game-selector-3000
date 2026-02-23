import time
import random
print("GAME SELECTOR 3000")

user_games = input("\nPlease enter the games (seperated by commas): ")

games_list = [game.strip() for game in user_games.split(',')]

while True:
    result = random.choice(games_list).upper()

    print("\nSelecting a game from your list...")
    time.sleep(3)
    print("\nI got it!")
    time.sleep(1.5)
    print(f"\nYou should play {result}")
    time.sleep(1)
    again = input("\nDo you want to pick another game? (y/n): ").strip().lower()
    if again != "y":
        time.sleep(0.5)
        print("\nThank you for using the Game Selector 3000")
        time.sleep(0.5)
        print("Happy Gaming and Goodbye!")
        break
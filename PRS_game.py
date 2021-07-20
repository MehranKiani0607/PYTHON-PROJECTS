import random
from config_PRS import GAME_CHOICES, RULES, scoreboard
from datetime import datetime
from decorators import pow2, is_even
from decorators import log_time

def get_user_choice():
    """
    get player input
    """
    user_input = input("Enter your choice please (r, p, s): ")
    if user_input not in GAME_CHOICES:
        print("wrong choice, try again")
        return get_user_choice()
    return user_input


def get_system_choice():
    """
    choice random from GAME_CHOICES
    """
    return random.choice(GAME_CHOICES)


def find_winner(user, system):
    """
    receive user and system choice and compare with game rules and find winner
    """
    match = {user, system}

    if len(match) == 1:
        return None

    return RULES[tuple(sorted(match))]


def update_scoreboard(result):
    """
    update scoreboard after each game and show live result
    """
    if result["user"] == 3:
        scoreboard["user"] += 1
        msg = 'You win'
    elif result["system"] == 3:
        scoreboard["system"] += 1
        msg = "You lose"
    print("#" * 20)
    print("##", f"user: {scoreboard['user']}".ljust(16))
    print("##", f"system: {scoreboard['system']}".ljust(16))
    print("##", f"last game {msg}".ljust(16))
    print("#" * 20)

def play_again():
    return input("Dou you want to play again? (y/n)")


def play_one_hand():
    """
    main play ground handler
    """
    result = {"user": 0, "system": 0}
    while result["user"] < 3 and result["system"] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)

        if winner == user_choice:
            msg ="You are winner"
            result["user"] += 1
        elif winner == system_choice:
            msg = "You are loser"
            result["system"] += 1
        else:
            msg = "Result is draw"

        print(f"user: {user_choice}\t system: {system_choice}\t result: {msg}")

    new_scoreboard = update_scoreboard(result)
    print(new_scoreboard)
    new_game = play_again()
    if new_game == 'y':
        play_one_hand()

@log_time
def play():
    play_one_hand()

if __name__ == "__main__":
    # start_time = datetime.now()
    play()
    # end_time = datetime.now()
    # duration = end_time - start_time
    # print(
    #     f"Total time: {duration.seconds // 3600} : {duration.seconds // 60}"
    #     f" : {duration.seconds % 60}")
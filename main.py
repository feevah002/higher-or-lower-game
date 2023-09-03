# random integer module
from random import randint
from game_data import data
import art
import os

def clear_screen():
    """
    clear the console
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def display_game_logo():
    '''
    print game logo
    '''
    print(art.logo)

def display_vs_logo():
    '''
    prints vs logo
    '''
    return art.vs

def get_random_celebrity():
    '''
    get random celebrities from the module
    '''
    celebrity = data[randint(0, len(data)-1)]
    return celebrity


def game_question(celebrity_one, celebrity_two):
    '''
    print question to user
    '''
    question_one = f"Compare A: {celebrity_one['name']}, a {celebrity_one['description']}, from {celebrity_one['country']} \n{display_vs_logo()}"

    question_two = f"Compare B: {celebrity_two['name']}, a {celebrity_two['description']}, from {celebrity_two['country']}"
    return question_one + question_two

def check_answer(user_answer, celebrity_one, celebrity_two):
    '''
    Returns True if player is correct else returns False
    '''
    higher_following = celebrity_one
    if celebrity_one['follower_count'] < celebrity_two['follower_count']:
        higher_following = celebrity_two
    if user_answer == higher_following:
        return True
    else:
        return False

def collect_user_input():
        user_answer = input("Who has more followers? Type 'A' or 'B': ")
        return user_answer.lower()

def play_game():
    display_game_logo()
    game_end = False
    previous = ''
    user_score = 0
    while not game_end:
        # get random celebrities from our module
        compare_one = get_random_celebrity()
        compare_two = get_random_celebrity()
        # handles situation where 2 random generated celebrities are the same
        while compare_one == compare_two:
            compare_two = get_random_celebrity()
        if user_score > 0:
            # replacing celebrity with previous if user has passed a question
            compare_one = previous
        # game question to user
        print(game_question(compare_one, compare_two))
        # user input
        user_answer = collect_user_input()
        if user_answer == 'a':
            user_answer = compare_one
        elif user_answer == 'b':
            user_answer = compare_two
        else:
            print('invalid choice')
        # check if user answer is correct
        if check_answer(user_answer, compare_one, compare_two):
            user_score += 1
            print(f"You're right. Current score: {user_score}")
            print(user_score)
            # getting the previous celebrity used
            previous = compare_two
        else:
            clear_screen()
            print(f'Sorry, that\'s wrong. Final score: {user_score}')
            game_end = True

play_game()
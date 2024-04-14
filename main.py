# Requests library is the popular HTTP library for making HTTP requests.
# It supports various HTTP methods, handles cookies,
# provides convenient features for working with HTTP-related tasks.
# The requests library supports various HTTP methods such as GET, POST, PUT, DELETE, etc.
import requests
#the html module is particularly useful in web development scenarios
# where HTML content needs to be manipulated, displayed, or rendered in a secure way.
# It helps prevent security vulnerabilities by escaping potentially dangerous characters in user input,
# ensuring that the HTML content is safely handled and displayed.
# html module is to escape and unescape HTML entities,
# especially when dealing with user-generated content or
# when you need to ensure the proper rendering of HTML in a secure manner.
import html

#the random module is a built-in module that provides functions for generating random numbers.
import random

# the get_ques_pool function constructs a URL for the Open Trivia Database API,
# sends an HTTP GET request to retrieve trivia questions based on the specified parameters,
# and returns the list of trivia question results.
def get_ques_pool(amount: int,category: int)->list:
    url=f"https://opentdb.com/api.php?&amount={amount}&category={category}&difficulty=medium&type=multiple"
    response=requests.get(url)
    response_json=response.json()
    return response_json["results"]

# the shuffle_choices function takes a list of choices as input,
# shuffles the order of the elements in that list using the random.
# shuffle function, and then returns the modified list with the elements in a random order.
# This type of function is commonly used in scenarios where you want to randomize the order of items,
# such as shuffling answer choices in a multiple-choice question.

def shuffle_choices(choices:list)->list:
    random.shuffle(choices)
    return choices

# the print_choices function takes a list of choices, iterates through the list,
# unescapes HTML entities in each choice, and prints each choice to the console with its corresponding index.
# This function is suitable for displaying multiple-choice options in a human-readable format.

def print_choices(choices:list)->None:
    for choice_index,choice in enumerate(choices):
        print(f"{choice_index+1}. {html.unescape(choice)}")

# the get_user_choice function continuously prompts the user to enter a number of choice,
# validates the input to ensure it falls within the specified range,
# and returns the validated user choice (adjusted by subtracting 1) when a valid input is provided.
# The loop ensures that the user is prompted repeatedly until a valid choice is entered.

def get_user_choice()->int:
    while True:
        print(" ")
        user_choice=int(input("Enter number of choice:"))
        if user_choice in range(1,5):
            return user_choice-1
        else:
            print("Invalid input")

# the display_result function is responsible for presenting feedback to the user based on whether their choice was correct or incorrect.
# It prints messages to the console,
# and the returned boolean value can be used by the calling code to take further actions based on the correctness of the user's answer.
def display_result(is_correct, correct_choice_text, score):
    if is_correct:
        print("WOW! Correct")
        return True
    else:
        print(f"SAD! Incorrect. The correct answer is: {correct_choice_text}")
       # print(f"Your current score is: {score}")
        return False


#the play_game function orchestrates the process of playing the trivia game.
# It fetches questions, presents them to the player one by one,
# evaluates the correctness of the player's answers, updates the score,
# and displays the final score at the end of the game.
# The associated main section initializes the game with a default amount and category when the script is executed directly.

def play_game(amount:int,category:int)->None:

    question_pool=get_ques_pool(amount,category)
    score=0
    for question in question_pool:
        question_text=html.unescape(question["question"])
        print(question_text)
        choices=question["incorrect_answers"]
        choices.extend([question["correct_answer"]])
        shuffled_choices=shuffle_choices(choices)
        print_choices(shuffled_choices)
        user_choice_index=get_user_choice()
        user_choice_text=shuffled_choices[user_choice_index]
        correct_choice_text=html.unescape(question["correct_answer"])
        print(" ")
        if display_result(user_choice_text == correct_choice_text, correct_choice_text, score):
            score += 1
        print(" ")

    print(f"Your final score is {score} out of 10 trivia questions." )



if __name__=="__main__":
    print(input("Enter your name: "))
    print(" ")
    amount=10
    category=9
    play_game(amount,category)




import random
import json
import os
from datetime import datetime


account_file = "account.json"


def load_accounts():
    if os.path.exists(account_file):
        with open(account_file, "r") as f:
            return json.load(f)
    return {}


def save_accounts(accounts):
    with open(account_file, "w") as f:
        json.dump(accounts, f, indent=2)


def login():
    accounts = load_accounts()
    print("Welcome to the very interesting Quiz!")

    while True:
        print("Press [Enter] to create a new account or type your username to log in.")
        username = input("Username: ").strip().lower()

                

        if username == "":
           
            while True:
                new_username = input(" Choose a username: ").strip().lower()
                if new_username in accounts:
                    print("Username already exists.")
                elif new_username == "":
                    print("Username can't be blank.")
                else:
                    break
                username = input("Username: ").strip().lower()



                
            password = input("Create a password: ").strip()
            accounts[new_username] = {"password": password}
            save_accounts(accounts)
            print(f"Account '{new_username}' created!")
            return new_username

        elif username in accounts:
            password = input("Password: ").strip()
            if accounts[username]["password"] == password:
                print("Login successful!")
                return username
            else:
                print("Incorrect password.")
        else:
            print("Username not found. Press Enter to make a new one.")


flashcards = [
    {"question": "who is in paris?", "answer": "Kanye and JayZ", "choices": ["Cod word", "homies", "neighbors"]},
    {"question": "9 + 10 =", "answer": "21", "choices": ["19", "20", "22"]},
    {"question": "aint no party like a 'blank' party", "answer": "tea", "choices": ["pizza", "birthday", "lebron"]},
    {"question": "is luigi mangione innocent?", "answer": "no", "choices": ["yes", "maybe", "idk"]},
    {"question": "ain't nothing but a blank ache", "answer": "heart", "choices": ["hand", "pancreas", "placenta"]},
    {"question": "if a child falls into a lake, what do you do", "answer": "hit the griddy", "choices": ["run away", "call local authorities", "eat it"]},
    {"question": "which videogame has good plot", "answer": "Cyberpunk 2077", "choices": ["ghost of tsushima", "minecraft", "fortnite"]},
    {"question": "what is the best videogame", "answer": "Cyberpunk", "choices": ["fortnite", "minecraft", "risk of rain"]},
    {"question": "Why is cyberpunk 2077 a good game", "answer": "depressing plot", "choices": ["graphics", "choices dictate entire game from the start", "combat"]},
    {"question": "capital of thailand", "answer": "Bangkok", "choices": ["bangkok", "BANGKOK", "BANGkok"]},
    {"question": "2 + 2 =", "answer": "fish", "choices": ["2", "100", "400"]},
    {"question": "what is not found in tea", "answer": "all of the above", "choices": ["leaves", "flowers", "orange peel"]},
    {"question": "how many fingers are on your hand", "answer": "4", "choices": ["3", "5", "2"]},
    {"question": "how do you describe the color blue to a blind person", "answer": "you don't", "choices": ["brail", "voice", "open your eyes"]},
    {"question": "what is the capital of japan", "answer": "all of the above", "choices": ["tokyo", "osaka", "kyoto"]},
    {"question": "hot lava and Blank", "answer": "chicken", "choices": ["pork", "beef", "foul"]},
    {"question": "solve first derivative of x^2", "answer": "2x", "choices": ["69", "2x^2", "4x"]},
    {"question": "what color is the oldest described", "answer": "black ", "choices": ["red", "blue", "green"]},
    {"question": "what happened in tian an men square june 4th 1989", "answer": "nothing happened", "choices": ["something happened"]},
    {"question": "which of the following is a new color", "answer": "blue", "choices": ["black", "red", "green"]}
]


def load_data(datafile):
    if os.path.exists(datafile):
        with open(datafile, "r") as file:
            return json.load(file)
    return {"history": []}


def save_data(datafile, data):
    with open(datafile, "w") as file:
        json.dump(data, file, indent=2)


def show_summary(data):
    print(" Previous Session Summary:")
    if data["history"]:
        last = data["history"][-1]
        print(f"Date: {last['timestamp']}")
        print(f"Score: {last['score']}/{last['total']}")
        print(f"Accuracy: {last['accuracy']}%")
    else:
        print("No previous data found.")

    print("Overall Performance Summary:")
    if data["history"]:
        scores = [h["score"] for h in data["history"]]
        totals = [h["total"] for h in data["history"]]
        avg = round(sum(scores) / len(scores), 2)
        print(f"Total Sessions: {len(data['history'])}")
        print(f"Average Score: {avg}/{totals[0]}")
    else:
        print("No performance data yet.")


def adapt_flashcards(data):
    wrong_counts = {}
    for history in data["history"]:
        for missed in history.get("wrong", []):
            wrong_counts[missed] = wrong_counts.get(missed, 0) + 1
            if wrong_counts[missed] > 10:
                print("You've missed this one a lot. Focus!")

    def card_sort(card):
        return -wrong_counts.get(card["question"], 0) + random.random()

    return sorted(flashcards, key=card_sort)


def run_quiz():
    username = login()
    datafile = f"{username}_performance.json"
    data = load_data(datafile)
    show_summary(data)

    questions = adapt_flashcards(data)
    random.shuffle(questions)

    score = 0
    wrong = []
    total = min(20, len(questions))

    print(" Starting Multiple Choice Quiz:")

    for i, card in enumerate(questions[:total], 1):
        correct_answer = card["answer"]
        custom_wrong_choices = card.get("choices", [])
        choices = custom_wrong_choices + [correct_answer]
        random.shuffle(choices)

        option_labels = ["A", "B", "C", "D"]
        option_map = dict(zip(option_labels, choices))

        print(f"Q{i}: {card['question']}")
        for label in option_labels:
            print(f"  {label}) {option_map[label]}")

        while True:
            user_choice = input("Your answer (A/B/C/D): ").strip().upper()
            if user_choice in option_map:
                break
            print("Invalid input. Please enter A, B, C, or D.")

        if option_map[user_choice].lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")
            wrong.append(card["question"])

    accuracy = round((score / total) * 100, 2)

    print("Quiz Finished!")
    print(f"Score: {score}/{total}")
    print(f"Accuracy: {accuracy}%")
    if accuracy < 50:
        print("study harder!!")

    data["history"].append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score": score,
        "total": total,
        "accuracy": accuracy,
        "wrong": wrong
    })

    save_data(datafile, data)


run_quiz()

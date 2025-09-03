# ------ Exercise 1

data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]


def play_quiz():
    correct_count = 0
    incorrect_count = 0
    wrong_answers = []

    print("🌌 Welcome to the Star Wars Quiz! 🌌\n")

    for item in data:
        user_answer = input(item["question"] + " ").strip()

        if user_answer.lower() == item["answer"].lower():
            print("✅ Correct!\n")
            correct_count += 1
        else:
            print(f"❌ Nope! The correct answer was: {item['answer']}\n")
            incorrect_count += 1
            wrong_answers.append({
                "question": item["question"],
                "your_answer": user_answer,
                "correct_answer": item["answer"]
            })

    show_results(correct_count, incorrect_count, wrong_answers)


def show_results(correct_count, incorrect_count, wrong_answers):
    print("📊 Quiz Results 📊")
    print(f"Correct answers: {correct_count}")
    print(f"Incorrect answers: {incorrect_count}\n")

    if wrong_answers:
        print("Here are the ones you missed:")
        for item in wrong_answers:
            print(f"❓ Question: {item['question']}")
            print(f"   Your answer: {item['your_answer']}")
            print(f"   Correct answer: {item['correct_answer']}\n")

    if incorrect_count > 3:
        retry = input(f"You missed more than 3... want to try again? (yes/no) ").strip().lower()
        if retry == "yes":
            play_quiz()
        else:
            print("May the Force be with you!")
    else:
        print("Great job, young Padawan! ✨")


# Start the game
play_quiz()


# ------ Exercise 2

# Dictionary with names and birthdays
birthdays = {
    "Yassine": "Mars 16",
    "Adnane": "Mars 13",
    "Baba": "Janvier 1"
}

# Step 1: Print all available names
print("We have birthday information for:")
for name in birthdays:
    print(f"- {name}")

# Step 2: Ask the user for a name
person = input("\nEnter the name of the person: ")

# Step 3 & 4: Check if the name exists
if person in birthdays:
    print(f"{person}'s birthday is on {birthdays[person]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {person}.")


# ------ Exercise 3

X = 10
expression = str(X) + " + " + str(X)*2 + " + " + str(X)*3 + " + " + str(X)*4
print(expression)

# ------ Exercise 4

import random

def throw_dice():
    """Simulate throwing a dice and return a value between 1 and 6."""
    return random.randint(1, 6)

def throw_until_doubles():
    """Throw two dice until doubles occur, return number of throws."""
    count = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        count += 1
        if die1 == die2:
            break
    return count

def main():
    throws_list = []

    for _ in range(100):  # Repeat 100 times
        throws = throw_until_doubles()
        throws_list.append(throws)

    total_throws = sum(throws_list)
    average_throws = total_throws / len(throws_list)

    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

# Run the program
if __name__ == "__main__":
    main()


# ------ Exercise 5

# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8

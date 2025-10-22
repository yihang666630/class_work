# Welcome the user to the quiz program
# Explain that they will answer multiple-choice questions

# Initialize a score counter to keep track of correct answers

# Present the first question
# Display the question text and the multiple-choice answers
# you can think of questions yourself, or find them online

# Get the user's input for their answer to the first question

# Check if the answer is correct
# If the answer is correct, print a success message and increase the score
# If the answer is incorrect, print the correct answer

# Repeat the above steps for additional questions (Question 2, Question 3, etc.)

# After all questions are answered, display the final score to the user
# Thank them for participating in the quiz

###### Extensions ######

# Use a loop to let people re-try the quiz
# create a leaderboard which stores users with the highest score
# Create a menu to let people access the leaderboard or the quiz
# Modularise the code to make it shorter and more maintainable
print("Welcome to the quiz program!")
print("You will answer multiple-choice questions")
print("The quiz will end when you answer all questions")
score = 0
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "What is the capital of Germany?",
        "options": ["Berlin", "London", "Madrid", "Paris"],
        "correct_answer": "Berlin"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ["Rome", "London", "Madrid", "Paris"],
        "correct_answer": "Rome"
    },
    {
        "question": "What is the capital of Spain?",
        "options": ["Madrid", "London", "Paris", "Rome"],
        "correct_answer": "Madrid"
    }
]

for i in range(len(questions)):
    question = questions[i]
    print(f"Question {i+1}: {question['question']}")
    for option in question["options"]:
        print(option)
    answer = input("Enter your answer: ").strip().lower()
    if answer == question["correct_answer"].strip().lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is {question['correct_answer']}")
print(f"Your score is {score}")
print("Thank you for participating in the quiz!")
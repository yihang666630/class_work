# Step 1: Create an empty list to hold quiz questions.

# Step 2: Define a function to add a new quiz question.
# This function should prompt the user for the question, options, and the correct answer.
# Store each question as a dictionary in the list.
# hint: dictionary could have keys like 'question', 'options', 'correct_answer'
# hint: options could be stored as a list of strings

# Step 3: Define a function to write the quiz questions to a file called 'quiz_questions.txt'.
# Format the questions nicely for readability, including the question text and possible answers.
# hint: loop through your list of dictionaries
# hint: use \n for formatting and spacing between questions

# Step 4: Define a function to display all current quiz questions in the console.
# hint: similar to step 3, but use print() instead of file writing

# Step 5: In the main part of the program:
# - Call the function to add questions in a loop until the user decides to stop.
# - After finishing, call the function to write all questions to 'quiz_questions.txt' in a nice, human-readable format
# - Optionally, display the questions on the console before writing them to the file.
# hint: use a while loop and you could ask user if they want to continue after each question
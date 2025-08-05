# List of dictionaries where each dictionary holds a true/false question and its correct answer
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


# This class represents a single question in the quiz
class Question:
    def __init__(self, q_text, q_answer):
        # Store the question text
        self.text = q_text
        # Store the correct answer (True or False)
        self.answer = q_answer


# This class manages the overall quiz behavior
class QuizzBrain:
    def __init__(self, q_list):
        # Start from the first question
        self.question_number = 0
        # Start with a score of 0
        self.score = 0
        # Store all the question objects in a list
        self.question_list = q_list

    # This function asks the next question in the list
    def next_question(self):
        # Get the current question based on the index
        current_question = self.question_list[self.question_number]
        # Move to the next question for the next round
        self.question_number += 1
        # Ask the user for input and store the answer
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Check whether the user gave the correct answer
        self.check_answer(user_input, current_question.answer)

    # This function checks whether there are still questions left
    def still_has_questions(self):
        # Returns True if the current index is less than the total number of questions
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    # This function compares the user's answer to the correct one
    def check_answer(self, user_input, correct_answer): 
        # If the answer is correct (case-insensitive), increase the score
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("You Got It Right!")
        else:
            # If the answer is wrong, inform the user
            print("That's wrong!")
        # Always show the correct answer
        print(f"Correct Answer is {correct_answer}.")
        # Show the user's current score and how many questions they've attempted
        print(f"Your Current Score is {self.score}/{self.question_number}")
        print("\n")  # Print a blank line for spacing


# Create an empty list to store question objects
question_bank = []

# Loop through each question dictionary in the original data
for question in question_data:
    # Get the question text and the correct answer
    question_text = question["text"]
    answer_text = question["answer"]
    # Create a Question object using the class
    new_question = Question(question_text, answer_text)
    # Add the question object to the list
    question_bank.append(new_question)  # we transformed the data into objects


# Create the QuizBrain object and pass it the list of Question objects
quiz = QuizzBrain(question_bank)

# Keep running the quiz as long as there are questions remaining
while quiz.still_has_questions():
    quiz.next_question()

# Once the quiz is over, print the final score
print("You Completed The Quiz!")
print(f"Your Final Score is: {quiz.score}/{quiz.question_number}")

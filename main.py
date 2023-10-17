import random
import time

# Ask user how many questions they want to answer
# show question 1 at a time and wait for user to enter their answer
# after given amount of questions, provide the user with the time and number of correct answers they knew.

print('Welcome to the rapid fire maths quiz!')
print('The aim of this game is to get as many questions right in the quickest possible time')

# Variables to set the minimum and maximum number range
min_num = 0
max_num = 10

def question_generator(min_num, max_num):
    # Setting variables to track data within the loop
    question_number = 0
    correct_responses = 0
    start_time = time.time()
   
    while question_number < 3:
        # Generate two random numbers and an opperator to create a maths problem
        num_1 = random.randint(min_num, max_num)
        num_2 = random.randint(min_num, max_num)
        opperator = random.choice(['+', '-', '*'])
        
        # Format and print the problem to the terminal for the user to read and respond to
        problem = f'{num_1} {opperator} {num_2}'
        print(problem)
        user_response = int(input('Type your answer: '))
        
        # Calculate the correct answers
        if opperator == '+':
            answer = num_1 + num_2
        elif opperator == '-':
            answer = num_1 - num_2
        elif opperator == "*":
            answer = num_1 * num_2

        # Compare the user response to the correct answer and provide feedback
        if user_response == answer:
            correct_responses += 1  
            print('Correct!')
        else:
            print('Incorrect!')
        
        # Loop counter to track how many questions have been asked
        question_number +=1 
    
    # Calculate the total time and print performance data to the terminal
    finish_time = time.time()
    elapsed_time = finish_time - start_time
    print(f'You answered {correct_responses} questions correct in {elapsed_time:.2f} seconds')
        

# Calls the question generator function and passes in the number range
question_generator(min_num, max_num)

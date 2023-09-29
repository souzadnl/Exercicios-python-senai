# Opa, tudo bem, Marcia? Espero que sim hahaha. Então, eu alterei algumas práticas minhas, por isso essa atividade está levemente diferente!
#Estarei escrevendo os códigos em inglês para praticar. Além disso, usarei o snake_case e implementarei funcionalidades extras! :)

"""
# Counter 1-10
for x in range(1,11):
    print(x)"""

"""
# Sum of natural numbers
chosen_number = int(input("Enter the number of times you want to add the natural numbers! (Starting by 0)\n"))
counter = 0
sum_numbers = 0
while(counter<chosen_number):
    sum_numbers += counter
    print(sum_numbers)
    counter+=1"""

"""
# Fibonacci Sequence
def calculate_fibonacci(position):
    fibonacci_sequence = []
    counter = 2
    fibonacci_sequence.append(0)
    fibonacci_sequence.append(1)
    while(counter<position):
        next_number = fibonacci_sequence[counter-1]+fibonacci_sequence[counter-2]
        fibonacci_sequence.append(next_number)
        counter+=1
    counter = 0
    for x in fibonacci_sequence:
        print(f"{counter+1}° position: {x}")
        counter+=1

print("Fibonacci sequence!")
position = int(input("Insert the position of Fibonacci's sequence and we'll show for you! (Starting by 0 -> [0, 1, 1, 2, 3...])\n"))
calculate_fibonacci(position)"""

"""
# Multiplication Table
chosen_number = int(input("Enter a number to see it's multiplication table!\n"))
for x in range(1,11):
    print(f"{chosen_number} x {x} = {chosen_number*x}")"""

"""
# Factorial
def factorial(result, factorial_number, counter):
    if(counter == 0):
        result = factorial_number
    else:
        print(f"{result} x {factorial_number-counter} =", end=" ")
        result*=factorial_number-counter
        print(f"{result}")
    counter+=1
    
    if(counter == factorial_number):
        return
    else:
        return factorial(result, factorial_number, counter)

start_value = 0
counter = 0
factorial_number = int(input("Enter the number to discover its factorial!\n"))
factorial(start_value, factorial_number, counter)"""

"""
# TEST Factorial ------------------ Just a test. I didn't use it because I preferred to save the numbers in an array to be displayed easily --------------
def factorial(chosen_number):
    if(chosen_number == 0):
        return 1
    return chosen_number * factorial(chosen_number-1)

chosen_number = int(input("Enter a number to discover its factorial!"))
print(factorial(chosen_number))"""


"""
# Even Numbers
chosen_number = int(input("Enter a number to see all even numbers until it!\n"))
for x in range(0, chosen_number+1, 2):
    print(x)"""

"""
# Largest and Lowest numbers
numbers = []
counter = 0
amount_numbers = int(input("Enter the amount of numbers you want to insert: \n"))
while(counter<amount_numbers):
    numbers.append(int(input(f"Enter the {counter+1}° number!\n")))
    if(counter == 0):
        largest_number = numbers[counter]
        lowest_number = numbers[counter]
    else:
        if(numbers[counter]>largest_number):
            largest_number = numbers[counter]

        if(numbers[counter]<lowest_number):
            lowest_number = numbers[counter]
    counter+=1

print(f"The largest number is: {largest_number}")
print(f"The lowest number is: {lowest_number}")"""

""" Sum of digits
chosen_number = input("Enter a number to sum its digits!\n")
sum_numbers = 0
for number in chosen_number:
    number = int(number)
    sum_numbers += number
print(f"The sum of digits in {chosen_number} is: {sum_numbers}")"""

# --------------------------------------------------------------------------------------

""" Hangman game
# Hangman game - Challenge
from os import system

# CHANGING SPACES OF WORD
def change_spaces(spaces, word, index, attempt, wrong_attempt):
    # CASE LIST SPACE DON'T HAVE ITENS YET
    if(spaces == []):
        for letter in range(0, len(word)):
            spaces.append("_")
        print(" ".join(spaces))
        if(wrong_attempt != []):
            print(f"Wrong attempts: {wrong_attempt}")
        print("===========================================================================")
        return spaces
    
    # CASE INDEX LENGTH < 0 MEANS THAT THE LETTER ISN'T AT THE WORD
    elif(len(index)<0):
        print(" ".join(spaces))   
        if(wrong_attempt != []):
            print(f"Wrong attempts: {wrong_attempt}")
        print("===========================================================================")
        return spaces 

    # CASE INDEX LENGTH < 0 MEANS THAT THE LETTER ISN'T AT THE WORD 
    else:
        counter = 0
        for element in index:
            spaces[element] = attempt
        print(" ".join(spaces))
        if(wrong_attempt != []):
            print(f"Wrong attempts: {wrong_attempt}")
        print("===========================================================================")
        return spaces   

# HERE I'M DOING THE INTERFACE DESIGN PART
def drawing(allowed_errors, word, spaces=[], index=[], attempt='', wrong_attempt=[]):
    if(allowed_errors == 6):
        print("________ ")
        print("|    | ")
        print("| ")
        print("| ")
        print("| ")
        print("| ")
    elif(allowed_errors == 5):
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("| ")
        print("| ")
        print("| ")
    elif(allowed_errors == 4):
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("|    | ")
        print("| ")
        print("| ")
    elif(allowed_errors == 3):
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("|   /| ")
        print("| ")
        print("| ")
    elif(allowed_errors == 2):
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|    ")
        print("| ")
    elif(allowed_errors == 1):
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|   /")
        print("| ")
    else:
        print("________ ")
        print("|    | ")
        print("|    0 ")
        print("|   /|\ ")
        print("|   //")
        print("| ")
        print("Oh no! Your attempts are over! Finishing... :(")
        return

    return change_spaces(spaces, word, index, attempt, wrong_attempt)

def check_attempt(word, allowed_errors, spaces, attempt, wrong_attempt):
    counter = 0
    index = []
    index_find = word.find(attempt)
    # Check if 
    try:
        if(index_find>=0):
            spaces.index(attempt)
        else:
            wrong_attempt.index(attempt)
        print("\n----------> This letter was already entered! Try another letter <----------")
        return index, allowed_errors, wrong_attempt
    except:
        if(index_find>=0):
            for letter in range(0, len(word)):
                if(word[counter]==attempt):
                    index.append(counter)
                counter+=1

            print(f"\nYou're correct! This letter ({attempt}) is in the word! \nAllowed errors: {allowed_errors}")
            return index, allowed_errors, wrong_attempt
        else:
            allowed_errors-=1
            print(f"\nYou're wrong! This letter ({attempt}) isn't in the word! \nAllowed errors: {allowed_errors}")
            wrong_attempt.append(attempt)
            return index, allowed_errors, wrong_attempt
        

print("Hangman Game!")
print("Rules: One person will write a word and the other will try to get the word right! You have 6 allowed errors!")
word = input("Enter a word to the Hangman Game: \n").upper()
hint = input("Enter a hint about the word you chose: \n")
allowed_errors = 6
wrong_attempt = []
first_time = True
system('cls')
print("Well, let's play the game!")
print(f"Hint about the word: {hint}")
# First time
spaces = drawing(allowed_errors, word)
while(allowed_errors>=0):
    if(not first_time):
        spaces = drawing(allowed_errors, word, spaces, index, attempt, wrong_attempt)
        if(allowed_errors>0):
            try:
                spaces.index('_')
            except:
                print("You won! Congratulation! :)")
                print(f"The word was: {word}")
                exit()

            attempt = input("Type a letter so we can check if it's in the word: \n").upper()
            index, allowed_errors, wrong_attempt = check_attempt(word, allowed_errors, spaces, attempt, wrong_attempt)
        else:
            allowed_errors-=1
    else:
        attempt = input("Type a letter so we can check if it's in the word: \n").upper()
        index, allowed_errors, wrong_attempt = check_attempt(word, allowed_errors, spaces, attempt, wrong_attempt)
        first_time = False"""

"""
# Rabbit population growth
print("Rabbits reproduce at a fixed rate each generation, and a percentage of them die each generation. Now we're going to calculate that!")
reproduction = int(input("Enter the percentage of the reproduction rate: \n"))
mortality = int(input("Enter the percentage of the mortality rate: \n"))
generation = int(input("Enter the generation you want to know about the number of rabbits: \n"))
start_value = int(input("Enter the starting number of rabbits: \n"))
counter = 0
while(counter<generation):
    if(counter==0):
        number_rabbits = start_value
    generation_number_rabbits = number_rabbits
    number_rabbits += number_rabbits*(reproduction/100)
    number_rabbits -= generation_number_rabbits*(mortality/100)
    print(f"{counter+1}° generation: {number_rabbits:.01f}")
    counter+=1
"""


def factorial(result, factorial_number, counter):
    if (counter == 0):
        result = factorial_number
    else:
        print(f"{result} x {factorial_number - counter} =", end=" ")
        result *= factorial_number - counter
        print(f"{result}")
    counter += 1

    if (counter == factorial_number):
        return
    else:
        return factorial(result, factorial_number, counter)


start_value = 0
counter = 0
factorial_number = int(input("Enter the number to discover its factorial!\n"))
factorial(start_value, factorial_number, counter)
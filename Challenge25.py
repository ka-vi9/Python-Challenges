print ("challenge 25")
import random
random_number = random.randint(1,5)
user_num = input("Guess a number between 1-5: ")
if ( user_num == random_number):
    print ("Congratulations! You got the correct number!")
else:
    print("Sorry, you didn't get the right number. You'll get it next time!")
    

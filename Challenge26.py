print("Challenge 26: Guessing Game II")
import random
random_number = random.randint(1,5)
user_num_1 = input("Guess a number between 1-5: ")
if ( user_num_1 == random_number):
    print ("Congratulations! You got the correct number!")
elif (int(user_num_1) > random_number):
        print("The number is less than your guess")
elif ( int (user_num_1) < random_number):
        print("The number is greater than your guess")
        
user_num_2 = input ("Try to guess the number again: ")
if ( user_num_2 == random_number):
    print ("Congratulations! You got the correct number!")
elif (int(user_num_2) > random_number):
        print("The number is less than your guess")
elif ( int (user_num_2) < random_number):
        print("The number is greater than your guess")

user_num_3 = input ("Try to guess the number again: ")
if ( user_num_3 == random_number):
    print ("Congratulations! You got the correct number!")
elif (int(user_num_3) > random_number):
        print("The number is less than your guess")
elif ( int (user_num_3) < random_number):
        print("The number is greater than your guess")

        


#random_number_2 = random.randint(1,5)
#user_num_2 = input("Guess a number between 1-5: ")
#if ( user_num_2 == random_number_2):
    #print ("Congratulations! You got the correct number!")
#elif (int(user_num_2) > random_number_2):
        #print("The number is less than your guess")
#elif ( int (user_num_2) < random_number_2):
        #print("The number is greater than your guess")

#random_number_2 = random.randint(1,5)
#user_num_2 = input("Guess a number between 1-5 again: ")
#if ( user_num_2 == random_number_2):
    #print ("Congratulations! You got the correct number!")
#elif (int(user_num_2) > random_number_2):
        #print("The number is less than your guess")
#elif ( int (user_num_2) < random_number_2):
        #print("The number is greater than your guess")

#random_number_3 = random.randint(1,5)
#user_num_3 = input("Guess a number between 1-5 again: ")
#if ( user_num_3 == random_number_3):
    #print ("Congratulations! You got the correct number!")
#elif (int(user_num_3) > random_number_3):
        #print("The number is less than your guess")
#elif ( int (user_num_3) < random_number_3):
        #print("The number is greater than your guess")


      

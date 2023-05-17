import random
import constants

def game_screen():
    playing = 'Y'
    
    while playing == 'Y':

        questions = open('questions.txt', 'r')
        solutions = open('answers.txt', 'r')

        answerkey = {}

        for i, prompt in enumerate(questions.readlines()):
            answerkey[prompt] = 1
            
            

    print(answerkey)
        

      


def start_screen():
    print("Hello! Lets play a quiz game! ")
    playing = input("Press Y to continue..Press N to quit: ")

    if playing != 'Y':
        quit()

    print("Lets get started! ")
    game_screen()




def main():
    start_screen()
    
    print(answerkey)



main()
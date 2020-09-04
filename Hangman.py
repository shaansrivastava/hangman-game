import time
import random

print("-----Welcome to Hangman Game-----")
name=input("Enter your name:")
print("Hello "+name+"! Best of luck!")
time.sleep(2)
print("The game is about to start")
time.sleep(3)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess=["apple","orange","water","banana","spinach","human"
                    ,"greedy","hungry","great","animals","plants"]
    word=random.choice(words_to_guess)
    length=len(word)
    count=0
    display='_'*length
    already_guessed=[]
    
def loop():
    global play_game
    play_game=input("Do you want to play again? y=yes, n=no:")
    while play_game not in ['y','Y','n','N']:
        play_game=input("Do you want to play again? y=yes, n=no:")
    if play_game=='y' or play_game=='Y':
        main()
    elif play_game=='n' or play_game=='N':
        print("Thanks for playing!!")
        
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit=5
    guess=input("Hangman word:"+display+"\nEnter your guess:")
  
    guess=guess.strip()
    if len(guess.strip())==0 or len(guess.strip())>=2 or guess<='9':
        print("Invalid input, Try a letter!!!")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index=word.find(guess)
        word=word[:index]+"_"+word[index+1:]
        display=display[:index]+guess+display[index+1:]
        print(display)
        
    elif guess in already_guessed:
        print("Try another letter.")
        
    else:
        count+=1
        if count==1:
            time.sleep(1)
            print("   _____ ")
            print("  |     ")
            print("  |     ")
            print("  |     ")
            print("  |     ")
            print("  |     ")
            print("  |     ")
            print("__|__")
            print("Wrong guess. "+str(limit-count)+" guesses remaining")
        elif count==2:
            time.sleep(1)
            print("   _____ ")
            print("  |     | ")
            print("  |     | ")
            print("  |       ")
            print("  |       ")
            print("  |       ")
            print("  |       ")
            print("__|__")
            print("Wrong guess. "+str(limit-count)+" guesses remaining")
        elif count==3:
            time.sleep(1)
            print("   _____ ")
            print("  |     | ")
            print("  |     |")
            print("  |     | ")
            print("  |      ")
            print("  |      ")
            print("  |      ")
            print("__|__")
            print("Wrong guess. "+str(limit-count)+" guesses remaining")
        elif count==4:
            time.sleep(1)
            print("   _____ ")
            print("  |     | ")
            print("  |     |")
            print("  |     | ")
            print("  |     o ")
            print("  |      ")
            print("  |      ")
            print("__|__")
            print("Wrong guess. "+str(limit-count)+" guesses remaining")
        elif count==5:
            time.sleep(1)
            print("   _____ ")
            print("  |     | ")
            print("  |     |")
            print("  |     | ")
            print("  |     o ")
            print("  |    /|\  ")
            print("__|__")
            print("Wrong guess. You are hanged!!!")
            print("The word was:",already_guessed,word)
            loop()

    if word=="_"*length:
        print("You have guessed correctly!!")
        loop()
    elif count!=limit:
        hangman()
main()
hangman()

import pyttsx3
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def winGame(comp, you):
    if comp == you:
        return None
    elif comp == 'p':
        if you == 'r':
            return False
        elif you =='s':
            return True

    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True

    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("Comp Turn: Rock(r), paper(p) or Scissors(s)\n")
speak("Computers Turn")
randNo = random.randint(1,3)
if randNo == 1:
     comp = "r"
elif randNo == 2:
     comp = "p"
elif randNo == 3:
     comp = "s"

speak("Your Turn")
you = input("Your Turn: Rock(r), paper(p) or Scissors(s)\n")
a = winGame(comp , you)
print(f"Computer choose::{comp}")
print(f"You Choose::{you}")

if a == None:
    print("The game is tie")
    speak("The game is tie")
elif a :
    print("You Won!!")
    speak("You Won!!")
else:
    print("You Lost!!")
    speak("You Lost!!")

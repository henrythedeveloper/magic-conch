#Arraylist
Magicconch = ["Yes", "No", "Try again", "Yikes not looking good", "Wait", "I need a break"]
#Randomizer for arraylist
import random
#takes a random arraylist element and strings it to 'conch' for output later
conch = random.choice(Magicconch)
#Return output
print(conch)


#Maybe do a while loop as long as user wants to use the 8-ball?


#Experimental
#Maybe tie additional outputs along with answers
#Example:
if conch == "Try again":
    print("Would you like to roll again?")

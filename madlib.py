#This is a Madlib project by Charles U.
#13th Nov. 2021

#Player is prompted for his name
player_name = input("Kindly enter you name: ")
player_name = player_name.capitalize()

#Player is welcomed
print(f"Welcome {player_name}!!!\nAt the prompt below, kindly provide inputs.\n")

#Game begins and player is prompted for inputs.
print("==========GAME BEGINS==========")
adj = input("Enter an adjective here: ")
adj2 = input("Enter another adjective here :")
bird = input("Enter the name of a bird: ")
room = input("Enter the name of a room in a house: ")
verb = input("Enter a verb (past tense): ")
verb2 = input("Enter a verb: ")
relative = input("Enter a relatives name: ")
noun = input("Enter a noun here: ")
liquid = input("Enter the name of a liquid here: ")
verb3 = input("Enter a verb ending with \"-ing\": ")
body = input("Enter the name of a body part here: ")
noun2 = input("Enter a plural noun here: ")
verb4 = input("Enter a verb ending with \"-ing\": ")
noun3 = input("Enter a noun here: ")

print("\n")
print("==========YOUR RESULT==========")
madlib = f"It was a {adj}, cold November day. I woke up to the {adj2} smell of {bird} roasting in the {room} downstairs. I {verb} down the stairs to see if I could help {verb2} the dinner. My mom said, \"See if {relative} needs a fresh {noun}.\" So I carried a tray of glasses full of {liquid} into the {verb3} room. When I  got there, I couldn't believe my {body}! There were {noun2} {verb4} on the {noun3}!"

#Completed madlib is printed and game ends
print(madlib + "\n")
print("==========GAME ENDS==========")
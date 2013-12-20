#hangman

import random

p0="""
10 false trys remaining






"""

p1="""
9 false trys remaining




  __
-/  \-
"""

p2="""
8 false trys remaining

   |
   |
   |
  _|_
-/   \-
"""

p3="""
7 false trys remaining
    _____
   |
   |
   |
  _|_
-/   \-
"""

p4="""
6 false trys remaining
    _____
   |     |
   |
   |
  _|_
-/   \-
"""

p5="""
5 false trys remaining
    _____
   |     |
   |     O
   |
  _|_
-/   \-
"""

p6="""
4 false trys remaining
    _____
   |     |
   |     O
   |     |
  _|_
-/   \-
"""

p7="""
3 false trys remaining
    _____
   |     |
   |     O
   |    \|
  _|_
-/   \-
"""


p8="""
2 false trys remaining
    _____
   |     |
   |     O
   |    \|/
  _|_
-/   \-
"""

p9="""
1 false try remaining
    _____
   |     |
   |     O
   |    \|/
  _|_  _/
-/   \-
"""

p10="""
YOU LOST!!!!!!!!!!
    _____
   |     |
   |     O
   |    \|/
  _|_  _/ \_
-/   \-
"""

pics=[p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

print ("type ENTER if you want to use a random word else type your word and press ENTER")
y=input(">>> ")
if y=="":
	words=["reindeers","elves","santaclaus","presents","christmastree",
			"candles","christmas","church","decoration","christday"]
else:
	words=[y]

print("\n"*40)
print("now turn the PC to the other player")
print()


display=[]

wrong=[]

correct=[]

goal=random.choice(words)
goal=list(goal)
howmany=len(goal)
for c in goal:
		display.append("_")
print("guess a word with ",howmany," chars")
print(display)
while True:
	if len(wrong)>11:
		break
	if not ("_" in display):
		break
	guess=input("please type a char: ")
	if guess in goal:
		correct.append(guess)
		pos = 0
		for x in goal:
			if x in correct:
				display[pos]=x
			pos+=1
	else:
		wrong.append(guess)
	print(pics[len(wrong)])
	print(display)
print("GAME OVER")

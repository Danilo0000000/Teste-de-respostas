
import random

print("-----------------")
print("Guessing Game")
print("-----------------")
attemps=0
secret_number=0
level=int(input("Which dificulty you want play?""\nType 1 for Easy (1/5 chance) \nType 2 for Medium (1/8 chance)\nType 3 for Hard (1/18 chance)\n"))
if (level==1):
    attemps=20
    secret_number=random.randrange(1,101)
    points=1000
    print("The number is beetwen 1 and 100")
else:
    if (level==2):
        attemps=12 
        secret_number=random.randrange(1,101)
        print("The number is between 1 and 100")
        points=1200
    else:
        if(level==3):
            attemps=5
            secret_number=random.randrange(1,91)
            print("The number is between 1 and 90")
            points=1800
tried_number=0
attemp_number=1
while (attemps>=attemp_number)and tried_number!=secret_number :
    print("Attemp {} of {}".format(attemp_number, attemps))
    tried_number=int(input('Try one number: '))
    if (level==1 or level==2) and (tried_number<0 or tried_number>100):
        print("You need to type a number between 1 and 100")
    else:  
        if(level==3 and tried_number<0 or tried_number>90):
            print("You need to type a number between 1 and 90")
            continue
    print("You typed number", tried_number)
    correct=tried_number==secret_number
    higher=tried_number>secret_number
    smaller=tried_number<secret_number
    if higher:
        print("Smaller number.")
    else:
        if smaller:
            print('Higher number.')
        else:
            if correct:
                print('Correctly.')
    attemp_number=attemp_number+1
if level==1:
    points=points-(attemp_number*10)
else:
    if level==2:
        points=points-(attemp_number*18)
    else:
        if level==3:
            points=points-(attemp_number*50)
if higher or smaller:
    print("Try on next, the number was",secret_number)
else: 
    print("Good job Genius")
    print("You did {} points".format (points))


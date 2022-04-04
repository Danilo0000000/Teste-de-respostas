
question_1=((input("Did you call the victim?(type T for yes F to no):")))
question_1=question_1.upper()
test_1= 1 if question_1=="T" else 0
question_2=((input("Were you at the crime scene?(type T for yes F to no):")))
question_2=question_2.upper()
test_2= 1 if question_2=="T" else 0
question_3=((input("Do you live near the victim?(type T for yes F to no):")))
question_3=question_3.upper()
test_3= 1 if question_3=="T" else 0
question_4=((input("Did it owe the victim?(type T for yes F to no):")))
question_4=question_4.upper()
test_4= 1 if question_4=="T" else 0
question_5=((input("Have you ever worked with the victim?(type T for yes F to no):")))
question_5=question_5.upper()
test_5= 1 if question_5=="T" else 0
tests= test_1+test_2+test_3+test_4+test_5
if tests==2:
    print("Suspect")
elif tests ==3 or tests==4:
    print("Accomplice")
elif tests==5:
    print("Killer")
else:
    print("Innocent")
    

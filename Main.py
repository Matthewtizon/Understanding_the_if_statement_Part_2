#define who is the richest person in the 3
person_1 = input("What is your name: ")
value_of_person_1 = input("How much money do you have: ")


person_2 = input("What is your name: ")
value_of_person_2 = input("How much money do you have: ")


person_3 = input("What is your name: ")
value_of_person_3 = input("How much money do you have: ")




if float(value_of_person_1) > float(value_of_person_2) and float(value_of_person_1) > float(value_of_person_3):
    print(f"then {person_1} is the richest among the 3")
elif float(value_of_person_2) > float(value_of_person_1) and float(value_of_person_2) > float(value_of_person_3):
    print(f"then {person_2} is the richest among the 3")
elif float(value_of_person_3) > float(value_of_person_1) and float(value_of_person_3) > float(value_of_person_2):
    print(f"then {person_3} is the richest among the 3")








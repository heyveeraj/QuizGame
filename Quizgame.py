print("Welcome to the Science Quiz Game!")
print("Test your knowledge of science by answering the following questions.")
x = input("Type yes to start! ")

if x.lower() == "yes":
    print("lets start")
    score = 0
else:
    print("invalid responce")
    quit()

answer = input(
    "\n1] What is the chemical symbol for the element gold? \nOptions:\nA) Au  B) Ag  C) Fe  D) Hg \n(enter the letter corresponding to your choice): ")
if answer == "a".lower():
    print("correct!")
    score += 1
else:
    print("Sorry, that's incorrect. The correct answer is A) Au ")

answer = input(
    "\n2] Who is known as the father of modern physics?\nOptions: \nA) Isaac Newton B) Galileo Galilei C) Albert EinsteinD) Stephen Hawking \n(enter the letter corresponding to your choice): ")
correct_answer = 'c'
if answer.lower() == correct_answer:
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect. The correct answer is C) Albert Einstein  ")

answer = input(
    "\n3] What is the largest planet in our solar system?\nOptions: \nA) Earth  B) Mars  C) Jupiter  D) Saturn \n(enter the letter corresponding to your choice):")
correct_answer = 'c'
if answer.lower() == correct_answer:
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect. The correct answer is C) Jupiter")

answer = input(
    "\n4] Which gas do plants absorb from the atmosphere during photosynthesis? \nOptions:\nA) Oxygen B) Nitrogen C) Carbondioxide D) Hydrogen \n(enter the letter corresponding to your choice):  ")
correct_answer = 'c'
if answer.lower() == correct_answer:
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect. The correct answer is C Carbon dioxide")

answer = input(
    "\n5] What is the chemical formula for water?\nOptions:\nA) H2O B) CO2 C) O2 D) CH4 \n(enter the letter corresponding to your choice):")
correct_answer = 'a'
if answer.lower() == correct_answer:
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect. The correct answer is A H2O")

answer = input(
    "\n6] What is the process by which plants make their own food using sunlight? \nOptions: \nA) Respiration B) Photosynthesis C) Transpiration D) Germination \n(enter the letter corresponding to your choice):")
correct_answer = 'b'
if answer.lower() == correct_answer:
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect. The correct answer is B Photosynthesis")

answer = input(
    "\n7] What is the process by which an unstable atomic nucleus emits radiation? \nOptions: \nA) Fusion B) Fission C) Decay D) Synthesis \n(enter the letter corresponding to your choice):")
correct_answer9 = 'c'
if answer.lower() == correct_answer9:
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect. The correct answer is C) Decay")

answer = input(
    "\n8] What is the term for the bending of light as it passes from one medium to another, such as from air to water?\nOptions: \nA) Reflection B) Dispersion C) Diffraction D) Refraction \n(enter the letter corresponding to your choice):")
correct_answer10 = 'd'
if answer.lower() == correct_answer10:
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect. The correct answer is D) Refraction")

answer = input(
    "\n9] What is the smallest particle of an element that retains all the properties of that element?\nOptions: \nA) Atom B) Molecule C) Compound D) Isotope \n(enter the letter corresponding to your choice):")
correct_answer11 = 'a'
if answer.lower() == correct_answer11:
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect. The correct answer is A) Atom")

answer = input(
    "\n10] What is the name of the process by which plants convert atmospheric nitrogen into a form that can be used by them?\nOptions: \nA) Nitrification B) Nitrogen Fixation C) Denitrification D) Ammonification \n(enter the letter corresponding to your choice):")
correct_answer12 = 'b'
if answer.lower() == correct_answer12:
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect. The correct answer is B) Nitrogen Fixation")

print("\nThank you for participating in the science quiz!")
print("You have completed the quiz.")
print("\nyou got " + str(score) + " questions corrrect out of 10 questions!")

if score <= 2:
    print("\nYou could do better. Keep practicing!")

elif score <= 4:
    print("\nNot bad, but there's room for improvement!")

elif score <= 6:
    print("\nNice job! You're on the right track!")

else:
    print("\nGreat work! ")

quiz = [
    {
        "question" : """What is the recommended minimum supply of drinking water
        per person per day in an emergency kit?""",
        "options" : ["A) one quart", "B) one gallon", "C) two litres"],
        "answer" : "B"
    },
    {
        "question" : """What is the best way to secure your home windows against
        strong hurrican winds?""",
        "options" : ["A) use masking tape to from 'X'",
                     "B) nail plywood or deploy permanent shutters", "C) open all windows"],
        "answer" : "B"
    },
    {
        "question" : """If authorities issue an evacuation order, where is the ideal designated
        meeting spot for your family""",
        "options" : ["A) pre planned meeting area outside of the neighborhood",
                     "B) inside the safest room in the house", "C) the nearest gas station"],
        "answer" : "A"
    },
    {
        "question" : "If the power goes out, what is the safest way to provide light?",
        "options" : ["A) candles and matches", "B) portable generator running inside the garage",
                     "C) battery powered flashlights/lanterns"],
        "answer" : "C"
    },
    {
        "question" : "How many days' worth of non-perishable food should your home emergency kit contain?",
        "options" : ["A) At least 1 day", "B) At least 3 days", "C) at least 7 days"],
        "answer" : "B"
    },
    {
        "question" : """After a hurricane, what is the first thing you should do if you suspect utility
        line damage (gas smell, flood risk)?""",
        "options" : ["A) call a plumber",
                     "B) turn off natural gas and main circuit breaker", "C) go outside to inspect lines"],
        "answer" : "B"
    },
    {
        "question" : """True or False: Storing important documents (insurance policies,
        identification) in a waterproof container is an essential preparedness step.""",
        "options" : ["A) true",
                     "B) false", "C) only if you plan to evacuate"],
        "answer" : "A"
    },
    {
        "question" : """What should you do with loose items in your yard (patio furniture, trash cans)
        before the storm hits?""",
        "options" : ["A) cover them with a tarm and tie them down",
                     "B) bring them indoors or secure them tightly",
                     "C) leave them where they are; they are too heavy to be moved by wind"],
        "answer" : "B"
    }]

score = 0

for q in quiz:
    print("\n" + q["question"])  # show question
    for option in q["options"]:
        print(option)            # show choices

    answer = input("Your answer: ").upper()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

print("\n------- RESULTS -------")
print(f"You got {score} out of {len(quiz)} questions right.")

# Survival logic
if score >= 5:
    print("You have a high chance of surviving the hurricane!")
else:
    print("Your chances of survival are low. Prepare better!")
input("\n Press Enter to exit...")

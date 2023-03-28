questions = ("What will you do if you are feeling low?",
             "What will you do if you are overthinking?",
             "How wil you manage your stress?")


options = (("A.Keep complaining about it ", "B.follow your hobby ", "C.Sleep and cry " ),
           ("A.write your thoughts down ", "B.sleep ", "C.stop thinking " ),
           ("A.watch TV ", "B.use phone ", "C.read a book " ))

answers = ("B", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------")
    print(question)
    for option in options[question_num]:
        print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct ans")
        question_num += 1

print("-------------------------")
print("         Results         ")
print("-------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) + 100)
print(f"Your score is: {score}%")


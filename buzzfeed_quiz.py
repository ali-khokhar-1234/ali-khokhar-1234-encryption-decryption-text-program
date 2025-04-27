questions = ["Pick a book you would read on a rainy day in: ",
             "What is your ideal vacation spot?: ",
             "If a genie gave you 3 wishes, what would be the first thing you wish for?: ",
             "Pick a Saturday night activity.: ",
             "Finally, pick a colour.: "]

options = [("A. Lord of the Rings ", "B. Harry Potter ", "C. The Chronicles of Narnia ", "D. Percy Jackson "),
           ("A. The countryside ", "B. DUBAI HABIBI YEAH!", "C. Anywhere with a beach, like Hawaii", "D. New York"),
           ("A. Peace and quiet whenever I want", "B. A trillion dollars and a yacht",
            "C. To eat whatever + however much I want and never get fat ", "D. The ability to fly"),
           ("A. Baking and Netflix", "B. Restaurant hopping", "C. YEMENI COFFEE", "D. Board Game night"),
           ("A. Blue ", "B. Green", "C. Pink", "D. Black")]

c1 = 0
c2 = 0
c3 = 0
c4 = 0
question_num = 0

for question in questions:
    print("-------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    answer = str(input("Enter (A, B, C, D): ").upper())

    question_num += 1

    if answer.upper() == "A":
        c1 += 1
    elif answer.upper() == "B":
        c2 += 1
    elif answer.upper() == "C":
        c3 += 1
    elif answer.upper() == "D":
        c4 += 1

print("---------------------------")
print("         RESULTS           ")
print("---------------------------")

if c1 > c2 and c1 > c3 and c1 > c4:
    print("You are [unknown character 1]")
elif c2 > c1 and c2 > c3 and c2 > c4:
    print("You are [unknown character 2]")
elif c3 > c1 and c3 > c2 and c3 > c4:
    print("You are [unknown character 3]")
elif c4 > c1 and c4 > c2 and c4 > c3:
    print("You are [unknown character 4]")
else:
    print("You are [unknown character 5]")

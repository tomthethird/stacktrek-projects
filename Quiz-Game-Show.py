from random import choice
from datetime import timedelta
from time import sleep

quizname = "Bawas Kamangmangan"
grandprize = 20000

print(f"\nWelcome to {quizname.upper()} QUIZ SHOW")
print("\nLet's all welcome our brave contestant for today!")

playername = input("\nWhat is your name, player?\n>>")

text = input("\nType 'START' to play\n\n>>")

while text.lower() != "start":
    print("\nInvalid input.")
    text = input("\nType 'START'>>")

delay = 3
while delay > 0:
    timer = timedelta(seconds = delay)
    print(".")
    sleep(1)
    delay -= 1

prize = 0

play = True
while play:
    lives = 5 # change this for number of attempts
    while lives!=0:
        print(f"\nWelcome, {playername}, to the {quizname.upper()} QUIZ SHOW.")
        print("\nYou will have a question each round and will be given choices to choose from.")
        print("Get it right and you will take the cash prize for that round.")
        print(f"\nYou will have {lives} lives to answer all questions.")
        print(f"\nAnswer all questions correctly and you take home {grandprize}.")

        text = input("\nType 'READY' to start\n\n>>")

        while text.lower() != "ready":
            print("\nInvalid input.")
            text = input("\nType 'READY'>>")

        # ---------------------------------------------------------------------

        print("\nLet's start with your first question.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print("\nQuestion 01")
        print("\n'In Python, which value type does input() return?'")
        ans1 = ["Boolean", "String", "Int", "Float"]

        correct_ans = "string"
        a = choice(ans1)
        a_pos = ans1.index(a)
        del ans1[a_pos]
        b = choice(ans1)
        b_pos = ans1.index(b)
        del ans1[b_pos]
        c = choice(ans1)
        c_pos = ans1.index(c)
        del ans1[c_pos]
        d = choice(ans1)
        d_pos = ans1.index(d)
        del ans1[d_pos]

        print(f"\nGet this correctly, and you take P{grandprize//10}.")
        print("\nHere are your choices.")
        print(f"\n* * * * * * * * * *\n{a}\n* * * * * * * * * *\n{b}\n* * * * * * * * * *\n{c}\n* * * * * * * * * *\n{d}\n* * * * * * * * * *")
        print("\nNote: Please type the answer with its correct spell and spacing.")
        answer = input("Type your answer here : ")

        a = a.lower()
        b = b.lower()
        c = c.lower()
        d = d.lower()
        answer = answer.lower()

        answer_valid = True
        while answer_valid:
            if answer == correct_ans:
                print("\nYOU GOT IT RIGHT!")
                print(f"\nYou win P{grandprize//10}. Congratulations!")
                prize += grandprize//10
                answer_valid = False
            elif (answer == a) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == b) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == c) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == d) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            else:
                print("\nInvalid input.")
                answer = input(">>")

        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print(f"\nYour current prize pot : P{prize}")
        if lives == 0:
            print("\nSorry, You lose all your lives.")
            break
        elif lives == 1:
            print(f"You have {lives} life left.")
        else:
            print(f"You have {lives} lives left.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        #---------------------------------------------------------------------

        print("\nYour second question.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print("\nQuestion 02")
        print("\n'In Python, which symbol is used to check whether two variables are the same?'")
        ans1 = ["-", "==", "=", "|"]
        correct_ans = "=="
        a = choice(ans1)
        a_pos = ans1.index(a)
        del ans1[a_pos]
        b = choice(ans1)
        b_pos = ans1.index(b)
        del ans1[b_pos]
        c = choice(ans1)
        c_pos = ans1.index(c)
        del ans1[c_pos]
        d = choice(ans1)
        d_pos = ans1.index(d)
        del ans1[d_pos]

        print(f"\nGet this correctly, and you take P{grandprize//10}.")
        print("\nHere are your choices.")
        print(f"\n* * * * * * * * * *\n{a}\n* * * * * * * * * *\n{b}\n* * * * * * * * * *\n{c}\n* * * * * * * * * *\n{d}\n* * * * * * * * * *")
        print("\nNote: Please type the answer with its correct spell and spacing.")
        answer = input("Type your answer here : ")

        a = a.lower()
        b = b.lower()
        c = c.lower()
        d = d.lower()
        answer = answer.lower()

        answer_valid = True
        while answer_valid:
            if answer == correct_ans:
                print("\nYOU GOT IT RIGHT!")
                print(f"\nYou win P{grandprize//10}. Congratulations!")
                prize += grandprize//10
                answer_valid = False
            elif (answer == a) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == b) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == c) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == d) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            else:
                print("\nInvalid input.")
                answer = input(">>")

        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print(f"\nYour current prize pot : P{prize}")
        if lives == 0:
            print("\nSorry, You lose all your lives.")
            break
        elif lives == 1:
            print(f"You have {lives} life left.")
        else:
            print(f"You have {lives} lives left.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        #---------------------------------------------------------------------

        print("\nYour third question.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print("\nQuestion 03")
        print("\n'True or False: A variable is a placeholder for data.'")
        ans1 = ["True", "False"]
        correct_ans = "true"
        a = choice(ans1)
        a_pos = ans1.index(a)
        del ans1[a_pos]
        b = choice(ans1)
        b_pos = ans1.index(b)
        del ans1[b_pos]

        print(f"\nGet this correctly, and you take P{grandprize//10}.")
        print("\nHere are your choices.")
        print(f"\n* * * * * * * * * *\n{a}\n* * * * * * * * * *\n{b}\n* * * * * * * * * *")
        print("\nNote: Please type the answer with its correct spell and spacing.")
        answer = input("Type your answer here : ")

        a = a.lower()
        b = b.lower()
        answer = answer.lower()

        answer_valid = True
        while answer_valid:
            if answer == correct_ans:
                print("\nYOU GOT IT RIGHT!")
                print(f"\nYou win P{grandprize//10}. Congratulations!")
                prize += grandprize//10
                answer_valid = False
            elif (answer == a) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == b) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            else:
                print("\nInvalid input.")
                answer = input(">>")

        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print(f"\nYour current prize pot : P{prize}")
        if lives == 0:
            print("\nSorry, You lose all your lives.")
            break
        elif lives == 1:
            print(f"You have {lives} life left.")
        else:
            print(f"You have {lives} lives left.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        #---------------------------------------------------------------------

        print("\nYour fourth question.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print("\nQuestion 04")
        print("\n'In Python, what is one function to output content to the console?'")
        ans1 = ["Echo", "Output", "Print", "Console.log"]
        correct_ans = "print"
        a = choice(ans1)
        a_pos = ans1.index(a)
        del ans1[a_pos]
        b = choice(ans1)
        b_pos = ans1.index(b)
        del ans1[b_pos]
        c = choice(ans1)
        c_pos = ans1.index(c)
        del ans1[c_pos]
        d = choice(ans1)
        d_pos = ans1.index(d)
        del ans1[d_pos]

        print(f"\nGet this correctly, and you take P{grandprize//10}.")
        print("\nHere are your choices.")
        print(f"\n* * * * * * * * * *\n{a}\n* * * * * * * * * *\n{b}\n* * * * * * * * * *\n{c}\n* * * * * * * * * *\n{d}\n* * * * * * * * * *")
        print("\nNote: Please type the answer with its correct spell and spacing.")
        answer = input("Type your answer here : ")

        a = a.lower()
        b = b.lower()
        c = c.lower()
        d = d.lower()
        answer = answer.lower()

        answer_valid = True
        while answer_valid:
            if answer == correct_ans:
                print("\nYOU GOT IT RIGHT!")
                print(f"\nYou win P{grandprize//10}. Congratulations!")
                prize += grandprize//10
                answer_valid = False
            elif (answer == a) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == b) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == c) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == d) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            else:
                print("\nInvalid input.")
                answer = input(">>")

        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print(f"\nYour current prize pot : P{prize}")
        if lives == 0:
            print("\nSorry, You lose all your lives.")
            break
        elif lives == 1:
            print(f"You have {lives} life left.")
        else:
            print(f"You have {lives} lives left.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1
        #--------------------------------------------------------------

        print("\nYour fifth question.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print("\nQuestion 05")
        print("\n'Which operator can be used on numeric values in Python?'")
        ans1 = ["+", "#", "@", "$"]
        correct_ans = "+"
        a = choice(ans1)
        a_pos = ans1.index(a)
        del ans1[a_pos]
        b = choice(ans1)
        b_pos = ans1.index(b)
        del ans1[b_pos]
        c = choice(ans1)
        c_pos = ans1.index(c)
        del ans1[c_pos]
        d = choice(ans1)
        d_pos = ans1.index(d)
        del ans1[d_pos]

        print(f"\nGet this correctly, and you take P{grandprize//10}.")
        print("\nHere are your choices.")
        print(f"\n* * * * * * * * * *\n{a}\n* * * * * * * * * *\n{b}\n* * * * * * * * * *\n{c}\n* * * * * * * * * *\n{d}\n* * * * * * * * * *")
        print("\nNote: Please type the answer with its correct spell and spacing.")
        answer = input("Type your answer here : ")

        a = a.lower()
        b = b.lower()
        c = c.lower()
        d = d.lower()
        answer = answer.lower()

        answer_valid = True
        while answer_valid:
            if answer == correct_ans:
                print("\nYOU GOT IT RIGHT!")
                print(f"\nYou win P{grandprize//10}. Congratulations!")
                prize += grandprize//10
                answer_valid = False
            elif (answer == a) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == b) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == c) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == d) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            else:
                print("\nInvalid input.")
                answer = input(">>")

        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print(f"\nYour current prize pot : P{prize}")
        if lives == 0:
            print("\nSorry, You lose all your lives.")
            break
        elif lives == 1:
            print(f"You have {lives} life left.")
        else:
            print(f"You have {lives} lives left.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        #---------------------------------------------------------

        print("\nWe are now on the second half of the our quiz.")

        print("\nHere is your sixth question.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print("\nQuestion 06")
        print("\n'A software life cycle model which builds a throwaway version.'")
        ans1 = ["Both answers are correct", "Prototyping Model", "Linear Sequential Model", "None of the above"]
        correct_ans = "prototyping model"
        a = choice(ans1)
        a_pos = ans1.index(a)
        del ans1[a_pos]
        b = choice(ans1)
        b_pos = ans1.index(b)
        del ans1[b_pos]
        c = choice(ans1)
        c_pos = ans1.index(c)
        del ans1[c_pos]
        d = choice(ans1)
        d_pos = ans1.index(d)
        del ans1[d_pos]

        print(f"\nGet this correctly, and you take P{grandprize//10}.")
        print("\nHere are your choices.")
        print(f"\n* * * * * * * * * *\n{a}\n* * * * * * * * * *\n{b}\n* * * * * * * * * *\n{c}\n* * * * * * * * * *\n{d}\n* * * * * * * * * *")
        print("\nNote: Please type the answer with its correct spell and spacing.")
        answer = input("Type your answer here : ")

        a = a.lower()
        b = b.lower()
        c = c.lower()
        d = d.lower()
        answer = answer.lower()

        answer_valid = True
        while answer_valid:
            if answer == correct_ans:
                print("\nYOU GOT IT RIGHT!")
                print(f"\nYou win P{grandprize//10}. Congratulations!")
                prize += grandprize//10
                answer_valid = False
            elif (answer == a) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == b) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == c) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == d) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            else:
                print("\nInvalid input.")
                answer = input(">>")

        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print(f"\nYour current prize pot : P{prize}")
        if lives == 0:
            print("\nSorry, You lose all your lives.")
            break
        elif lives == 1:
            print(f"You have {lives} life left.")
        else:
            print(f"You have {lives} lives left.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        #---------------------------------------------------------

        print("\nYour seventh question.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print("\nQuestion 07")
        print("\n'Which deliverable document describes the order of tasks and estimates of time and effort necessary?'")
        ans1 = ["Software test plan", "Project schedule", "Source code", "None of the above"]
        correct_ans = "project schedule"
        a = choice(ans1)
        a_pos = ans1.index(a)
        del ans1[a_pos]
        b = choice(ans1)
        b_pos = ans1.index(b)
        del ans1[b_pos]
        c = choice(ans1)
        c_pos = ans1.index(c)
        del ans1[c_pos]
        d = choice(ans1)
        d_pos = ans1.index(d)
        del ans1[d_pos]

        print(f"\nGet this correctly, and you take P{grandprize//10}.")
        print("\nHere are your choices.")
        print(f"\n* * * * * * * * * *\n{a}\n* * * * * * * * * *\n{b}\n* * * * * * * * * *\n{c}\n* * * * * * * * * *\n{d}\n* * * * * * * * * *")
        print("\nNote: Please type the answer with its correct spell and spacing.")
        answer = input("Type your answer here : ")

        a = a.lower()
        b = b.lower()
        c = c.lower()
        d = d.lower()
        answer = answer.lower()

        answer_valid = True
        while answer_valid:
            if answer == correct_ans:
                print("\nYOU GOT IT RIGHT!")
                print(f"\nYou win P{grandprize//10}. Congratulations!")
                prize += grandprize//10
                answer_valid = False
            elif (answer == a) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == b) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == c) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == d) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            else:
                print("\nInvalid input.")
                answer = input(">>")

        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print(f"\nYour current prize pot : P{prize}")
        if lives == 0:
            print("\nSorry, You lose all your lives.")
            break
        elif lives == 1:
            print(f"You have {lives} life left.")
        else:
            print(f"You have {lives} lives left.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        # ---------------------------------------------------------------------

        print("\nNow, here is your eight question.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print("\nQuestion 08")
        print("\n'The person who has complete responsibility for the success of the project and have accountability to the Stakeholders and Sponsors.'")
        ans1 = ["Systems Analyst", "Project Manager", "End-User", "Project Leader"]
        correct_ans = "project manager"
        a = choice(ans1)
        a_pos = ans1.index(a)
        del ans1[a_pos]
        b = choice(ans1)
        b_pos = ans1.index(b)
        del ans1[b_pos]
        c = choice(ans1)
        c_pos = ans1.index(c)
        del ans1[c_pos]
        d = choice(ans1)
        d_pos = ans1.index(d)
        del ans1[d_pos]

        print(f"\nGet this correctly, and you take P{grandprize//10}.")
        print("\nHere are your choices.")
        print(f"\n* * * * * * * * * *\n{a}\n* * * * * * * * * *\n{b}\n* * * * * * * * * *\n{c}\n* * * * * * * * * *\n{d}\n* * * * * * * * * *")
        print("\nNote: Please type the answer with its correct spell and spacing.")
        answer = input("Type your answer here : ")

        a = a.lower()
        b = b.lower()
        c = c.lower()
        d = d.lower()
        answer = answer.lower()

        answer_valid = True
        while answer_valid:
            if answer == correct_ans:
                print("\nYOU GOT IT RIGHT!")
                print(f"\nYou win P{grandprize//10}. Congratulations!")
                prize += grandprize//10
                answer_valid = False
            elif (answer == a) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == b) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == c) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == d) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            else:
                print("\nInvalid input.")
                answer = input(">>")

        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print(f"\nYour current prize pot : P{prize}")
        if lives == 0:
            print("\nSorry, You lose all your lives.")
            break
        elif lives == 1:
            print(f"You have {lives} life left.")
        else:
            print(f"You have {lives} lives left.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        # ---------------------------------------------------------------------

        print("\nWe are now in the last 2 question of the game.\n\nHere is your ninth question.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print("\nQuestion 09")
        print("\n'A type of Software Life Cycle Activity that involves building the software and converting the design into code.'")
        ans1 = ["Detailed design", "Interface design", "Architectural design", "Implementation"]
        correct_ans = "implementation"
        a = choice(ans1)
        a_pos = ans1.index(a)
        del ans1[a_pos]
        b = choice(ans1)
        b_pos = ans1.index(b)
        del ans1[b_pos]
        c = choice(ans1)
        c_pos = ans1.index(c)
        del ans1[c_pos]
        d = choice(ans1)
        d_pos = ans1.index(d)
        del ans1[d_pos]

        print(f"\nGet this correctly, and you take P{grandprize//10}.")
        print("\nHere are your choices.")
        print(f"\n* * * * * * * * * *\n{a}\n* * * * * * * * * *\n{b}\n* * * * * * * * * *\n{c}\n* * * * * * * * * *\n{d}\n* * * * * * * * * *")
        print("\nNote: Please type the answer with its correct spell and spacing.")
        answer = input("Type your answer here : ")

        a = a.lower()
        b = b.lower()
        c = c.lower()
        d = d.lower()
        answer = answer.lower()

        answer_valid = True
        while answer_valid:
            if answer == correct_ans:
                print("\nYOU GOT IT RIGHT!")
                print(f"\nYou win {grandprize//10}. Congratulations!")
                prize += grandprize//10
                answer_valid = False
            elif (answer == a) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == b) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == c) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == d) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            else:
                print("\nInvalid input.")
                answer = input(">>")

        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print(f"\nYour current prize pot : P{prize}")

        if lives == 0:
            print("\nSorry, You lose all your lives.")
            break
        elif lives == 1:
            print(f"You have {lives} life left.")
        else:
            print(f"You have {lives} lives left.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        # ---------------------------------------------------------------------

        print("\nCongratulations! You reached this level.\n\nHere is your final and last question.")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print("\nQuestion 10")
        print("\n'A type of Software Life Cycle Activity that involves building the software and converting the design into code.'")
        ans1 = ["Detailed design", "Interface design", "Architectural design", "Implementation"]
        correct_ans = "implementation"
        a = choice(ans1)
        a_pos = ans1.index(a)
        del ans1[a_pos]
        b = choice(ans1)
        b_pos = ans1.index(b)
        del ans1[b_pos]
        c = choice(ans1)
        c_pos = ans1.index(c)
        del ans1[c_pos]
        d = choice(ans1)
        d_pos = ans1.index(d)
        del ans1[d_pos]

        print(f"\nGet this correctly, and you take P{grandprize//10}.")
        print("\nHere are your choices.")
        print(f"\n* * * * * * * * * *\n{a}\n* * * * * * * * * *\n{b}\n* * * * * * * * * *\n{c}\n* * * * * * * * * *\n{d}\n* * * * * * * * * *")
        print("\nNote: Please type the answer with its correct spell and spacing.")
        answer = input("Type your answer here : ")

        a = a.lower()
        b = b.lower()
        c = c.lower()
        d = d.lower()
        answer = answer.lower()

        answer_valid = True
        while answer_valid:
            if answer == correct_ans:
                print("\nYOU GOT IT RIGHT!")
                print(f"\nYou win P{grandprize//10}. Congratulations!")
                prize += grandprize//10
                answer_valid = False
            elif (answer == a) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == b) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == c) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            elif (answer == d) and (answer != correct_ans):
                print("\nSorry, that is wrong.")
                lives -= 1
                answer_valid = False
            else:
                print("\nInvalid input.")
                answer = input(">>")

        delay = 2
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

        print(f"\nYour grand prize pot : P{prize}")
        print(f"\nCONGRATULATIONS!")

        delay = 3
        while delay > 0:
            timer = timedelta(seconds = delay)
            print(".")
            sleep(1)
            delay -= 1

    print("\nWould like to try again?")
    text = input("\nType 'RESTART' to restart.\nType 'END' to exit.\n>>")
    while text.lower() != "restart":
        if text.lower() == "end":
            play = False
            text = "restart"
        else:
            print("\nInvalid input.")
            text = input("Type 'RESTART' / 'END'>>")

print(f"\nThank you for playing, {quizname}.\n")

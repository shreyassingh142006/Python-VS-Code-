# KBC
print("KINDLY WRITE YOUR ANSWERS IN CAPITAL LETTERS\n")

q1 = ["Which city is known as pink city?", "ALWAR", "JAIPUR", "PUNE", "GWALIOR"]
q2 = ["What are the largest lizard species found on earth?", "MONITOR LIZARD", "KOMODO DRAGON", "GREEN IGUANA", "GREEN ANOLE"]
q3 = ["Who wrote the National Anthem of India?", "CHETAN BHAGAT", "RABINDRANATH TAGORE", "BANKIM CHNADRA CHATERJEE", "PREMCHAND"]
q4 = ["Which of the following is not a state in India ?", "GOA", "VRINDAVAN", "MEGHALAYA", "SIKKIM"]
q5 = ["Which country is the largest by land area ?", "RUSSIA", "CANADA", "UNITED STATES", "BRAZIL"]
prize = [100, 200, 300, 400, 500]

print("question 1. ", q1[0])
print("a. ", q1[1])
print("b. ", q1[2])
print("c. ", q1[3])
print("d. ", q1[4])
x = input(str("Enter your answer here: "))
if x == "JAIPUR":
    print("Your answer is correct.\n You've won the cash prize of Rs.100\n\n")

    print("question 2. ", q2[0])
    print("a. ", q2[1])
    print("b. ", q2[2])
    print("c. ", q2[3])
    print("d. ", q2[4])
    y = input(str("Enter your answer here: "))
    if y == "KOMODO DRAGON":
        print("Your answer is correct.\n You've won the cash prize of Rs.200\n\n")

        print("question 3. ", q3[0])
        print("a. ", q3[1])
        print("b. ", q3[2])
        print("c. ", q3[3])
        print("d. ", q3[4])
        a = input(str("Enter your answer here: "))
        if a == "RABINDRANATH TAGORE":
            print("Your answer is correct.\n You've won the cash prize of Rs.300\n\n")
                
            print("question 4. ", q4[0])
            print("a. ", q4[1])
            print("b. ", q4[2])
            print("c. ", q4[3])
            print("d. ", q4[4])
            b = input(str("Enter your answer here: "))
            if b == "VRINDAVAN":
                print("Your answer is correct.\n You've won the cash prize of Rs.400\n\n")
                
                print("question 5. ", q5[0])
                print("a. ", q5[1])
                print("b. ", q5[2])
                print("c. ", q5[3])
                print("d. ", q5[4])
                c = input(str("Enter your answer here: "))
                if c == "RUSSIA":
                    print("Your answer is correct.\n You've won the cash prize of Rs.500\n\n")

                    print("CONGRATULATIONS!!! You've passed all the questions.")
                    print("The cash prizes you've won are as follows:\n Question 1: Rs.100\n Question 2: Rs.200\n Question 3: Rs.300\n Question 4: Rs.400\n Question 5: Rs.500\n")
                    sum = sum(prize)
                    print("Total amount won is...\n", "Rs.", sum)
                else:
                    print("Your answer is wrong.\n Better luck next time.\n Total cash prize won by you is... ", "Rs.", sum(prize[0:3]))
            else:
                print("Your answer is wrong.\n Better luck next time.\n Total cash prize won by you is... ", "Rs.", sum(prize[0:2]))
        else:
            print("Your answer is wrong.\n Better luck next time.\n Total cash prize won by you is... ", "Rs.", sum(prize[0:1]))
    else:
        print("Your answer is wrong.\n Better luck next time.\n Total cash prize won by you is... ", "Rs.", sum(prize[0:0]))
else:
    print("Your answer is wrong.\n Better luck next time.\n Total cash prize won by you is... \n", "Rs.0")
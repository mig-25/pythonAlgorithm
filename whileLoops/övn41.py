""" Insert a series of numbers, add the sum after each prompt,
terminate the loop with the string quit
show the grand total
Example output:
Nr is: 3
Total is: 3
Nr is: 3
Total is: 6
Nr is: 5
Total is: 11
The sum of the numbers you entered is 11
 """


def sumTotal():
    total = 0

    userInput = input("Mata in en siffra: ")

    while userInput != "quit":
        total = total + int(userInput)
        print(f"Siffran du matade in är: {userInput}\n")
        print(f"Totalen är: {total}")

        userInput = input("Mata in en siffra: ")
    print(f"Summan av alla talen du matade in är: {total}")


sumTotal()

def main():
    userIn = input("enter your input: ")
    print(convert(userIn))

def convert(userInput):
    if ":)" in userInput:
        userInput = userInput.replace(":)", "🙂")
    if ":(" in userInput:
        userInput = userInput.replace(":(", "🙁")
    return userInput

main()

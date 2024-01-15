print("Welcome to my Elite 101 Chatbot!")
name = input("Please input your name: ")
print("Hallo! Pleased to meet you, " + name + "!" + " How old are you?")
age = int(input())


def myAge(age1):
  if age1 < 15:
    print("To be young is a good thing! How can I help you today? ")
  elif age1 >= 15 and age1 < 18:
    print("This is the best time to learn things! How can I help you today? ")
  elif age1 >= 18 and age1 < 55:
    print("Oh to be " + str(age) +
          " must be interesting. How can I help you today? ")
  elif age1 >= 55 and age1 < 120:
    print("You must be immortal. How can I help you today? ")
  else:
    print("You must be an alien! How can I help you today? ")


myAge(age)

print("\nPlease choose from the menu options: ")
print(
    "1.Placeholder Option 1\n2.Placeholder Option 2\n3.Placeholder Option 3\n4.Quit"
)
menuChoice = int(input("Enter the number of your choice: "))


def menu(choice):
  if choice == 4:
    print("\nGoodbye " + name + "!")
    exit()


menu(menuChoice)  #call to function menu

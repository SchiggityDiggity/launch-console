name = input("What's your name? ")
print(f"Welcome to Launch Console, {name}!")
Start = True
while Start:
    print('1) About Me\n2) My Goals\n3) Favorite Project\n4) Exit')
    choice = input("Choose 1-4")
    if choice == '1':
        print('I am a builder taking the c2c program, currently taking Elite 101')
    elif choice == "2":
        print('My goal is to get good understanding of the internship experience.')
    elif choice == "3":
        print('My favorite project was my personal project of making game called, "Rent Game" with AI as an instructor/guide.')
    elif choice == "4":
        print("Goodbye!")
        Start = False
    else:
        print('Invalid choice, choose 1-4')
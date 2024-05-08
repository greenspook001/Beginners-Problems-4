for attempt in range(3):
    password = input("Enter Password: ")
    if password == "Kobus":
        print("Correct Password")
        break
else:
    print("Locked")

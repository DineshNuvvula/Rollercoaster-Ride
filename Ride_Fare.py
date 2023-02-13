print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
photo = input("Do you need a photo ? y or n. ")

if height >= 120:
    print("You can ride the rollercoaster!!")
    if age < 12:
        bill = 5
        if photo == "y":
            bill += 3
            print(f"Your ticket costs ${bill}.")
        else:
            print(f"Your ticket costs ${bill}.")
    elif age < 45 or age > 55:
        bill = 12
        if photo == "y":
            bill += 3
            print(f"Your ticket costs ${bill}.")
        else:
            print(f"Your ticket costs ${bill}.")
    elif age >= 45 & age <= 55:
        bill = 0
        if photo == "y":
            bill += 3
            print(f"Your ticket costs ${bill}.")
        else:
            print(f"Your ticket costs ${bill}.")
    else:
        bill = 7
        if photo == "y":
            bill += 3
            print(f"Your ticket costs ${bill}.")
        else:
            print(f"Your ticket costs ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

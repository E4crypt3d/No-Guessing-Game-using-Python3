import random
import time
print("Welcome to The NUMBER GUESSING GAME")
print('''1: Easy
2: Medium
3: Hard
4: Extreme''')
diff_lvl = input("Choose the diffulty level: ")
if diff_lvl == '1':
    print('Difficulty Level = EASY')
    a = 1
    b = 10
    trys = 4
elif diff_lvl == '2':
    print('Difficulty Level = MEDIUM')
    a= 1
    b = 20
    trys = 4
elif diff_lvl == '3':
    print('Difficulty Level = HARD')
    a =1
    b =30
    trys = 5
elif diff_lvl == '4':
    print('Difficulty Level = EXTREME')
    a = 1
    b = 50
    trys = 6
else:
    print("Invalid option")
    exit()
n_range = random.randrange(a,b)
time.sleep(2)
user_i = int(input(f"Guess between {a} to {b} [You have {trys+1} attempts Only] \nEnter your guess: "))
while n_range != user_i and trys != 0:
    if user_i < n_range:
        print("Guess Higher")
        print(f'You have only {trys} guesses left')
        user_i = int(input("Try Again: "))
        trys-=1
    elif user_i > n_range:
        print("Guess Lower")
        print(f'You have only {trys} guess left')
        user_i = int(input("Try Again: "))
        trys-=1
if user_i == n_range:
    print("**** Correct Guess WELL DONE ****")
else:
    print('You have 0 attempts left\nGood Luck Next Time')

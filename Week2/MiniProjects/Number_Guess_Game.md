```python
import random
top_of_range=input("Type a number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range <=0:
        print('print type larger then zero!')
        quit()
else:
    print('print type number next time!')
    quit()
random_number=random.randint(0,top_of_range)
guesses=0
while True:
    guesses+=1
    user_guess = input('Enter guess ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('print type number next time!')
        continue
    if user_guess==random_number:
        print("You Got correctly")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")
print("You got it in "+str(guesses)+' Guesses')
```

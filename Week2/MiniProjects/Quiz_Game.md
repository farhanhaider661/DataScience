```python
print("***Welcome to Quiz Game***")
playing=input('Do you Want To Play? ')
if playing.lower()!='yes':
    quit()
print("Okay! Let's Play")
score=0
answer=input("What does CPU stands for? ").lower()
if answer=='central processing unit':
    print('Correct!')
    score+=1
else:
    print('Wrong')
answer=input("What does GPU stands for? ").lower()
if answer=='graphic processing unit':
    print('Correct!')
    score += 1
else:
    print('Wrong')
answer=input("What does GUI stands for? ").lower()
if answer=='graphical user interface':
    print('Correct!')
    score += 1
else:
    print('Wrong')
answer=input("What does RAM stands for? ").lower()
if answer=='random access memory':
    print('Correct!')
    score += 1
else:
    print('Wrong')
answer=input("What does AI stands for? ").lower()
if answer=='artificial intelligence':
    print('Correct!')
    score += 1
else:
    print('Wrong')
print("TOTAL MARKS YOU GOT: "+str(score))
```

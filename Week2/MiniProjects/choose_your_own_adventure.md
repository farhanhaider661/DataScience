```python
name=input("type your name: ")
print("welcome",name,"to this adventure")
answer=input('you are on a direct road, it has come to end and you can go left or right. Which way would you like to go? ').lower()
if answer=='left':
    answer=input("you come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across:  ").lower()
    if answer=="swim":
        print('you swam across & were eaten by an alligator')
    elif answer=="walk":
        print('you want many miles,ran out of water and you lost the game')
    else:
        print("Not a Valid option. You lose")
elif answer=='right':
    answer=input("you come to a bridge, it looks wobbly,do you want to cross it or head back (cross/back) ?").lower()
    if answer == "back":
        print('you go back & lose')
    elif answer == "cross":
       answer=input('You cross the bridge and met a stranger. Do you talk to them (Yes/No) ').lower()
       if answer=='yes':
           print('you talk to stranger and they give you gold. you Win!')
       elif answer=='no':
           print('you ignore the stranger and you lose!')
       else:
           print("Not a Valid option. You lose")
    else:
        print("Not a Valid option. You lose")
else:
    print("Not a Valid option. You lose")
print("Thank You ",name)
```

# Code
```python

class Pokemon:
    def __init__(self,name,primary_type,max_hp):
        self.name=name
        self.primary_type=primary_type
        self.hp=max_hp
        self.max_hp=max_hp
    def __str__(self):
        return f"{self.name}({self.primary_type} :{self.hp}/{self.max_hp})"
    def feed(self):
        if self.hp < self.max_hp:
           self.hp+=1
           print(f"{self.name} has now {self.hp} HP")   
        else:
            print(f"{self.name} is full.")  
    @staticmethod
    def typewheel(type1,type2):
        result_map={0: 'lose', 1:'win',-1:'tie'}
        game_map={'water':0,'fire':1,'grass':2}
        rps_table=[
            #water
            [-1,1,0],
             #fire
            [0,-1,1],
           #grass
            [1,0,-1]
        ]          
        result=rps_table[game_map[type1]][game_map[type2]]
        return result_map[result]      
    def battle(self,other):
        result=self.typewheel(self.primary_type,other.primary_type)
        if result=='lose':
            self.hp=0
            print(f"{self.name} fainted")
        elif result=='tie':
            self.hp-=10
            other.hp-=10
            print(f"{self.name} and {other.name} battled hard. It's tie")
        elif result=='win':
            other.hp=0
            print(f"{self.name} Won!!!")           
if __name__=='__main__':
 a=Pokemon("bulbasaur","water",100)
 b=Pokemon("charmandar","fire",150)
 a.battle(b)
 print(Pokemon("bulbasaur","water",100))

```
# Output
![image](https://user-images.githubusercontent.com/111038642/190197769-e28b9ddc-d717-4eba-94c8-fd5706e3562d.png)

![image](https://user-images.githubusercontent.com/111038642/190199823-79c3d563-2b78-4bcc-b589-1837533ebf0f.png)



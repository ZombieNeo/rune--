
#import shit
from random import *
#import shit

#skills
woodcutting = 0
fishing = 0
strength = 0


# formula for skills = level / 0.75 = the chance of something working EG. doing damage
#skills



#MAKE FUNCTIONS
randamage = randint(1,2)
damage = woodcutting/0.75+ randamage
def locationforest():
    if location== "forest":
        print("you arrive at the forest" )
        print("woodcutting level = "+str(woodcutting))
        axe = input("what do you want to do? (cut tree, collect wood) ")
        axe.lower()
        if axe == "cut tree":
            print("you swing your axe")
            tree_health = 5 
            tree_health - damage = tree_damage
            print(tree_health)
            
            
            

def locationlake():
    if location == "lake":
        print("you arrive at the lake")
        pass
def locationarena():
    if location == "arena":
        print("you arrive at the arena")
        pass
    
#def woodcutting_skill_chance():
    
#make functions ^




















name = input("enter your name ")#only show if no save file
print("In this game you train skills in various locations. where would you like to go (type GO TO X) ")
 







print("---------")
f = open("locations.txt","r")
file_contents = f.read()
print(file_contents)
print("---------")
location= input(" where do you want to go:")
location.lower()#makes users input lower case POG
locationlake()#if they say "lake" this function is called 
locationforest()
locationarena()
    
        
    

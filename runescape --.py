
#import shit
from random import *
#import shit

#skills
woodcutting = 1
woodcuttingexp = 1
fishing = 1
fishingexp = 1
strength = 1
strengthexp = 1


# formula for skills = level / 0.75 = the chance of something working EG. doing damage

#100 xp to level up + 10% per level


#skills



#MAKE FUNCTIONS
def location_select():
    location= input(" where do you want to go:")
    location.lower()#makes users input lower case POG
    locationlake()#if they say "lake" this function is called 
    locationforest()
    locationarena()    

def wood_level_up():
    if woodcuttingexp == 100:
        woodcutting = woodcutting + 1
        

def locationforest():
    if location== "forest":
        print("you arrive at the forest" )
        print("woodcutting level = "+str(woodcutting))
        axe = input("what do you want to do? (cut tree, collect wood) ")
        axe.lower()
        if axe == "cut tree":
            tree_health = 5 
            while tree_health >0:
                randamage = randint(0,1)
                damage = woodcutting * 0.75 + randamage                
                print("you swing your axe")
                tree_health = tree_health - damage
                print("you did :"+str(damage)+" damage")
            else:
                print("Tree cut down!")
                
                woodcutting_exp_random = randint(1,30)
                global woodcuttingexp 
                woodcuttingexp = woodcuttingexp + woodcutting_exp_random
                print(str(woodcutting_exp_random)+" XP earned")
                print("total level: "+str(woodcutting))
                keep = input("keep training? (n/y) ")
                if keep == "y":
                    locationforest()
                else:
                    location_select()
            
                
                
            
            
            

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
    
        
    

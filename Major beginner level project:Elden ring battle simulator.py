# Elden Ring Battle Simulator
# Built by Renegade | Age 16
# Status: In Progress
# Known bugs: Being fixed
# Started: 2026
# Day:2
# project:4
#project difficulty: mediocre

# game intro#

import random
import time
print("===ELDEN_RING_SIMULATOR==")
time.sleep(2)

AI=input(" press enter to start:")
choice=input(" Type initiate to start :")
if choice=="initiate":
        for every in range (4):
            print("loading resources... ")
            time.sleep(1)
else:
  print("action terminated")
  
print("=_ELDEN_REALM=")
time.sleep(1)
print(".chapter one ")
time.sleep(1)
player_name=input(" Input your name:")
for every in range (2):
    print( " exracting game assets..... " )
    time.sleep(1)

print(" Ultimate elden god-level boss appeared..! ")
time.sleep(1)

print(player_name  + "Oh no,! he caught me in his domain, i can't escape!, guess i have to go all out today!")
time.sleep(1)

#player and boss stats
#HPs:
player_hp=80000
boss_hp=100000
boss_name= "Eldenboss"

# Attacks
player_atk = random.randint(500,600)
boss_atk = random.randint(400,1000)
 #Artifacts
Dragon_blood= 300
Dragon_scale=1000
Heng_blade=1004
dragon_god_claws=19999
flame_katana=1000
#defensive artifacts
next_gen_flood_dragon_amour=40*500
Void_ancient_amour=30000
print("Initializing Forced battle")
time.sleep(1)

while player_hp > 0 and boss_hp > 0:
    print("...================...")
    print(player_name + " has "+ str(player_hp) + " hp")
    print(boss_name + " has "+ str(boss_hp) + " hp ")
    time.sleep(3)
    #attack phases
    player_atk=random.randint(599,600)
    boss_hp= boss_hp- player_atk
    if player_atk== 600:
        print(" 600 atk points activates " + player_name + "hidden bloodline effect : dragon god claws ")
        print(player_name + " attacks for " + str(player_atk) + " with an edittion of " + str(dragon_god_claws) +" on " + boss_name)
        time.sleep(1)
        boss_hp=boss_hp + player_atk
    elif player_atk==500:
        print(" hidden passive activated ! : Dragon_scales: it grands " + player_name + " an atk boost of 1000 ! ")
        print( player_name +" attacks for :"+ str(player_atk) +  str(Dragon_scale) + " on " + boss_name)
        time.sleep(1)
        boss_hp=boss_hp - player_atk
    else:
        print(player_name + " attacks for ! :" + str(player_atk) + " on " + boss_name)
    boss_hp=boss_hp - player_atk
#standby phase
if boss_hp< 1000:
    boss_hp=boss_hp + void_ancient_amour
    print(boss_name+ " has activated his innert clan talent : Void_Ancient_amour and gained a significant portion of his health! ")
    print(boss_name + " now has :" + str(boss_hp) +" left! be careful!! ")
else:
    print(boss_name + " has now "+str(boss_hp)+"left to slaughter you !")
  
#To be finished;🎯
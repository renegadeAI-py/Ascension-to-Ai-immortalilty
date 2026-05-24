import math
import random
import time
import sys

#Initiation phase#

print("#RENAGADE_IMMORTAL_RPG#")
time.sleep(1)
print("=Welcome to the culivation world=")
print("=#Roles#=")
print("sect_master")
print("supreme_eleder")
print("supreme_emperor")
print("Young_Master")
print("Sovereign")
print("Lord")
print("king")
role=input("choose your role from above :")
choice=input(" Enter play to continue: ")
time.sleep(1)
if choice=="play":
    for every in range(1):
        print("Analyzing game resources..")
        time.sleep(1)
    for every in range(1):
        print("Analysis complete...")
        time.sleep(1)
        print("loading game resources....")
        time.sleep(1)
else:
    print(" Input invalid! ")
    print(" Action Terminated! ")
    sys.exit()
#roles phase#
name=input("pick a name:")
sect=input("Name your sect :")

Player_info={"name":name,
"realm":"mortal",
"Diu_qi":100,
"sect":"Jade_cloud"}
enermies=["Dread_feng","Huang_tian",
"Gui_shen"]
artifacts={"spring_dagger":5,
                    "loong_tian_claw":10,
                    "heavenly_flame":15,
                    "phoneix_bow":10,
                    "phoneix_wing":9,
                    "chaos_dagger":25}
passives={"heavenly_demon_palm":25,
               "bhuddhas_blessing":10,
               "nine_neither_phantom_blade":30}
HP_talismen={"reincarnation_pill":400,
                            "Dragon_scales":500,}
player_HP=200
boss_HP=250
Player_atk=random.choice(50,60,80)
boss_atk=random.choice(50,75,100)
with open("player_stats.txt","w") as file:
    file.write(str(Player_info))
    file.write("\n" +HP_talismen)
    file.write("\n"+passives)
    file.write("\n"+artifacts)
    boss=random.choice(enermies)
    print(name + " vs " + boss)
    time.sleep(1.5)
    print("Reason : " + name + " stole " + boss + "e's" + " women ")
    time.sleep(1.5)
     
    for every in range(1):
        print("Alert..!")
        print("initiating_battle !....")
        print("prepare your self !")
        time.sleep(2)
  
while player_HP>=0 and boss_HP>0:
    player_atk=random.choice(50,60,80)
    if player_atk==50:
        print("passive: bhuddhas_blessing acivated..!")
        print(name + " atk increased by" + str(passives["bhuddhas_blessing"]))
        player_atk=player_atk+passives["bhuddhas_blessing"]
    elif player_atk==80:
            print("passive: nine_neither_phantom_blade.. acivated !")
            print(name + "atk increased by " + str(passives["nine_neither_phantom_blade"]))
            player_atk=player_atk+passives["nine_neither_phantom_blade"]
    elif player_atk==60:
        print("passive: heavenly_demon_palm.. activated")
        print("player_atk increased by " + str(passives["heavenly_demon_palm"]))
        player_atk=player_atk+passives["heavenly_demon_palm"]
else:
    player_atk=player_atk
    boss_atk=random.choice(50,75,100)
    if boss_atk == 50:
        print(boss + " uses the : chaos dagger ")
        print(boss + " atk increased by " + str(artifacts["chaos_dagger"]))
        boss_atk = boss_atk + artifacts["chaos_dagger"]
    elif boss_atk == 100:
        boss_atk = boss_atk + artifacts["spring_dagger"]
        print(boss + "uses the : spring_dagger")
        print(boss + " atk increases by " + str(artifacts["spring_dagger"]))
    elif boss_atk == 75:
        boss_atk = boss_atk + artifacts["phoneix_wing"] + artifacts["phoneix_bow"]
        
        print(boss + "activates his phoenix_wing , uses phoenix_bow and increases his atk by " + str(artifacts["phoenix_wing"] + ["phoneix_bow"]))
    print(boss + "- You are just an Ant..! ,you could have just killed Yourself , the moment you decided to steal my women..!")
    print(name + " -Oh , such a big talk, it  seems you are confident in your skills ")
    print(name +" hahaha " +"This "+ role + " would like to see if you actually have the ability to crush an Ant like me...!?")
    boss_HP=boss_HP - player_atk
    player_HP=player_HP - boss_atk
  
 
    print(name + " attacks for "+ str(player_atk) + " on "+ boss)
    print(boss + " strikes back for " +str(boss_atk))
    time.sleep(1.5)
    print(name +" HP: " + str(player_HP))
    print(boss +" HP: " + str(boss_HP))

#name: Renegade
#project#:6
#project status: In progress 
#project type: Lesson 1-10 graduation test
#bugs:manyknown : to be fixed
#age:16
#project expected to be finished?:🤔 maybe tomorrow
#Year:2026
#Day:3
#projected difficulty:hard"well for someone who learned basics 3 days ago"
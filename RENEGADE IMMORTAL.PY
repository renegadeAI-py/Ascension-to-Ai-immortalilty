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
"Dou_qi":100,
"sect":sect}
enermies=["Dread_feng","Huang_tian",
"Gui_shen"]
artifacts={"spring_dagger":5,
                    "loong_tian_claw":10,
                    "heavenly_flame":15,
                    "phoneix_bow":10,
                    "phoneix_wing":9,
                    "chaos_dagger":25}
passives={"heavenly_demon_palm":25,
               "bhudhas_blessing":10,
               "nine_neither_phantom_blade":30}
HP_talismen={"reincarnation_pill":400,
                            "Dragon_scales":500,}
player_HP=500
boss_HP=250
Player_atk=random.choice([50,80,100])
boss_atk=random.choice([50, 75,100])
with open("player_stats.txt","w") as file:
    file.write(str(Player_info))
    file.write("\n" +str(HP_talismen))
    file.write("\n"+str(passives))
    file.write("\n"+str(artifacts))
    boss=random.choice(enermies)
    print(name + " vs " + boss)
    time.sleep(1.5)
    print("Reason : " + name + " stole " + boss + "es" + " women ")
    time.sleep(1.5)
     
    for every in range(1):
        print("Alert..!")
        print("initiating_battle !....")
        print("prepare your self !")
        time.sleep(2)
  
while player_HP>0 and boss_HP>0:
    player_atk=random.choice([50,80,100])
    boss_atk=random.choice([50,75,40,100])
    if player_atk==100:
        player_atk=player_atk+passives["bhudhas_blessing"]
        print(name +" passive: bhuddhas_blessing acivated..!")
        time.sleep(1)
        print(name + " atk increased by" + str(passives["bhudhas_blessing"]))
        time.sleep(1)
        print(name + " old ugly die! " )
        time.sleep(2)
        print(name  + " attacks for " + str(player_atk))
        time.sleep(2)
        boss_HP=boss_HP - player_atk
        print(boss +" HP: " + str(boss_HP))
        time.sleep(3) 
    elif player_atk==80:
            player_atk=player_atk+passives["nine_neither_phantom_blade"]  
            print(name +": passive: nine_neither_phantom_blade.. acivated !")
            print(name + " atk increased by " + str(passives["nine_neither_phantom_blade"]))
            print(name + " attacks for " + str(player_atk))
            time.sleep(2)
            boss_HP=boss_HP - player_atk
            print(boss +" HP: " + str(boss_HP))
            time.sleep(3)
    elif player_atk==60:
        player_atk=player_atk+passives["heavenly_demon_palm"]
        print(name +" :passive: heavenly_demon_palm.. activated")
        time.sleep(2)
        print(name +" atk increased by " + str(passives["heavenly_demon_palm"]))
        time.sleep(2)
        print(name + " attacks for " + str(player_atk))
        time.sleep(2)
        boss_HP=boss_HP - player_atk
        print(boss +" HP: " + str(boss_HP))
        time.sleep(3)
       
    if boss_atk == 50:
        boss_atk = boss_atk + artifacts["chaos_dagger"] 
        print(boss + ": uses the  chaos dagger ")
        time.sleep(2)
        print(boss + " atk increased by " + str(artifacts["chaos_dagger"]))
        time.sleep(2)
        print(boss + " strikes  for " +str(boss_atk))
        time.sleep(2)
        player_HP=player_HP - boss_atk
        print(name +" HP: " + str(player_HP))
        time.sleep(3)
    elif boss_atk == 100:
        boss_atk = boss_atk + artifacts["spring_dagger"]
        print(boss + ": uses the  spring_dagger")
        time.sleep(1)
        print(boss + " atk increases by " + str(artifacts["spring_dagger"]))
        time.sleep(2)
        print(boss + " attacks for " + str(boss_atk))
        time.sleep(2)
        player_HP=player_HP - boss_atk
        print(name +" HP: " + str(player_HP))
        time.sleep(3)
    elif boss_atk == 75:
        boss_atk = boss_atk + artifacts["phoneix_wing"] + artifacts["phoneix_bow"]
       
        print(boss + " activates his phoneix_wing , uses phoneix_bow and increases his atk by " + str(float(artifacts["phoneix_wing"])) +str(float(artifacts["phoneix_bow"])))
        time.sleep(2)
         
        print(boss + " strikes for " +str(boss_atk))
        time.sleep(2)
        print(boss + "- You are just an Ant..! ,you could have just killed Yourself , the moment you decided to steal my women..!")
        time.sleep(3)
        print(name + " -Oh , such a big talk, it  seems you are confident in your skills ")
        time.sleep(2)
        print(name +" hahaha " +" This "+ role + " would like to see if you actually have the ability to crush an Ant like me...!?")
        time.sleep(3)
        player_HP=player_HP - boss_atk
        time.sleep(1.5)
        print(name + "HP :" + str(player_HP))
    
if boss_HP<=0:
    print(name + "- hmp " + " The dignified ruthless " + boss +" is nothing jus so-so" + " infront of the " + role +" of the " + sect + "_SECT" )
    time.sleep(2)
    print("You win")
    
    Player_info["Dou_qi"]=Player_info["Dou_qi"] + 1000
    player_atk=player_atk+math.sqrt(1000)
    
    
elif player_HP<=0:
      print(boss + " little thing in your next life forget about being a " + role + " or else you will die miserably !!! ")
      print("You lost miserably ")
      print("work harder next time")
      time.sleep(2)

with open("player_stats.txt","r") as file:
    stats=file.read()
    print(stats)
    sys.exit()
#project updated
#known bugs:few and being fixed
#project status: fully functional
#peoject type: RPG game
#Days to finish:(1)
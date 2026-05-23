import time
sect_name="Sky_dread_feng"
sect={"sect_leader": "Di tian",
            "vice_leader": "Bai_dong",
            "Bai_dong": "8 diciples"}
sect["elders"]="4"
sect["supreme_elder"]="Dong tian"
try:
    print("#Order of power in :" + sect_name)
    time.sleep(1.5)
    print("#Supreme_elder")
    time.sleep(1.5)
    print("#sect_leader")
    time.sleep(1.5)
    print("#vice_leader")
    time.sleep(1.5)
    print("#elders")
    time.sleep(1.5)
    print("disciple")
    
    print(" Qidian_Sect_has the following: ")
    time.sleep(1.5)
    print(sect["sect_leader"] + " is the sect leader ")
    time.sleep(1.5)
    print(sect["vice_leader"] +" is the vice leader ")
    time.sleep(1.5)
    print(sect["Bai_dong"] + " are " + sect["vice_leader"] + " lackeys ")
    time.sleep(1.5)
    choice=input(" choose your role from above: ")
    time.sleep(1.5)
  
    if choice=="sect_leader":
        print(" You are not worth the tittle.. ")
    elif choice=="supreme_elder":
        print(" You are now " + sect["supreme_elder"] + " the Transcentant supreme anchor of" +  sect_name )
        print("You now have access to all the " + sect_name + " resources and beauties ")
    elif choice=="elders":
        print("You are one of the " + sect["elders"] + " elders of the " + sect_name)
        print("you now have complete dominance " + " on all " + sect["Bai_dong"] + " of " + sect_name + "ancient sect !")
        
except:
    print("error detected !")
    print("action invalid")
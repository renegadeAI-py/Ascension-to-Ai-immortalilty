points=0
q1= input("what is btth?  ")
if q1== "battle through the heavens":
    points=points+10
    print("correct + "+ str(10))
else:
    print("ultra wrong + "+str(0))
q2=input("MC of btth is ? ")
if q2=="xiao yan":
    points=points + 20
    print("correct + "+str(20))
else:
    print("all wrong ! , final points = " + str(0))
q3=input("how many did xiao yan defeat? ")
if q3=="3":
        points=points + 30/2
        print("correct +" + str(30/2))
else:
    print("incorrect! " + str(0))
    
print("final score is "+ str(points))

hero_name=input("gimme a hero name : ")
enermy=input (" gimme an enermy name: ")
donghua=input(" gimme a donghua name: ")
women=input( " gimme a beaty :")

print(hero_name + " is a baddass ")
print("he killed " + enermy)
print(" in the donghua "+ donghua + " and claimed " + women + " and earned ! :" + str(points))
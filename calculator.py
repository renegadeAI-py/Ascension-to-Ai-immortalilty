
#This is a calculator build by renegadeAi
#Age 16
#goal = global tech giant in 2040
#side goal= souls game ai NPC developer in 2040


num1= input("choose your number")
num2=input("choose number")
choice=input("add,multipy,divide,subtract:")
num1=float(num1)
num2=float(num2)
if choice=="add":
    answer=num1 + num2
elif choice=="multiply":
    answer= num1 * num2
elif choice =="divide":
    answer=num1 / num2
elif choice=="subtract":
    answer= num1 - num2
else:
    answer ="invalid"
print("answer is "+str(answer))
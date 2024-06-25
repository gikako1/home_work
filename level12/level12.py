#for loops
for i in range(10):
    print(i+1)
for i in range(3):
    print("წინადადება")
#while loops
num=1
while num <6:
    print(num)
    num=num+1

num1=0
while num1<3:
    print("ჰელო")
    num1=num1+1

#easy 1
age=input()
if int(age)<18:
    print("you are too young")
elif int(age)>=18:
    print('welcome')

#easy 2
number=10
answer=input()
if int(answer)==number:
    print('you are correct')
elif int(answer)!=number:
    print('you stupid')

#hard
print("what is your age?")
age=input()
if int(age)>0 and int(age)<10:
    print('you are a child')
elif int(age)>=10:
    print('you are older than a child')

#extreme
print('make a valid triangle')
side1=(input())
side2=(input())
side3=(input())
if int(side1)+int(side2)>int(side3):
    print("triangle valid")
elif int(side1)+int(side2)<=int(side3):
    print('triangle invalid')
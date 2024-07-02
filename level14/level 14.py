# მათე დოლიძის დავალება
#for loop

# დავალება 1

for i in range(21):
    print(i)

#დავალება 2
for i in range(10):
    print(i+1)

#დავალება 3

#ლუწი
for i in range(51):
    print(i+i)

#კენტი
for i in range(50):
    print(i+i+1)

#დავალება 4
sum = 0
for i in range(1,int(input())+2):
    print(sum)
    sum=sum+i

#დავალება 5
for i in range(1,11):
    print(i*5)

#While loop

#დავალება 1

num=0
while num<=20:
    print(num)
    num=num+2

#დავალება 2 ვერ გავიგე

#დავალება 3
print("pick a number between 1 and 10 and i'll tell you the correct one")
num=int(0)
while int(num) <10:
    num=int(input())
    if num==int(7):
        print('you are correct')
        break
    elif num!=int(7):
        print("wrong")
    
    
#დავალება 4

print("pick a number and we'll make a list of numbers doubling till 1000")
num=int(input())
while num<1000:
    print(num)
    num=num+num

#დავალება 5


password='password123'
while password==password:
    
    print('enter password please')
    password=str(input())
    
    if password!="password123":
        print('wrong')  

    elif password=="password123":
        print('you are correct')
        break

#if-else

#დავალება 1
print('please enter time')
time=int(input())
if time<=12 and time>0:
    print('good morning')
elif time>12 and time<24:
    print('good afternoon')
else: print('thats not possible')

#დავალება 2 ვერ ვაკეთებ

#დავალება 3

print("how's the weather today?")
degrees=int(input())
if degrees<30:
    print("it's not that hot outside")
elif degrees>30:
    print("it's hot outside")

#დავალება 4

print('how old are you?')
age=int(input())

if age>=13 and age<20:
    print("you are a teenager")
else :print('you are not a teenager.')




    
    
        
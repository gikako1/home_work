#შექმენით ფუნქცია რომელსაც პარამეტრად გადაეცემა string-ების სია, საბოლოოდ კი აბრუნებს ყველაზე გრძელ სიტყვას სიიდან
stringlist=["a","aa","aaa","aaaaa","aaaa"]
def lensort(stringlist):
    if len(stringlist[3])>len(stringlist[4]):
        stringlist.append(stringlist[3])
        stringlist.pop(3)
    return print(stringlist)
lensort(stringlist)

# შექმენით ფუნქცია რომელიც მიიღებს მთელი რიცხვების სიას, ლუწ რიცხვებს გაამრავლებს თავის თავზე,
#  კენტებს კი 2-ზე შემდეგ ჩაამატებს ახალ სიაში, საბოლოოდ კი დააბრუნებს ახალ სიას.

numbers=[1,2,3,4,5,6]
def numsort():
    #0
    if numbers[0]/2==int:#ლუწი 
        numbers.insert(0,numbers[0]*numbers[0])
        numbers.pop(1)
    elif numbers[0]/2!=int:#კენტი
        numbers.insert(0,numbers[0]*2)
        numbers.pop(1)
    #1
    if numbers[1]/2==int:#ლუწი 
        numbers.insert(1,numbers[1]*numbers[1])
        numbers.pop(2)
    elif numbers[1]/2!=int:#კენტი
        numbers.insert(1,numbers[1]*2)
        numbers.pop(2)
     #2
    if numbers[2]/2==int:#ლუწი 
        numbers.insert(2,numbers[2]*numbers[2])
        numbers.pop(3)
    elif numbers[2]/2!=int:#კენტი
        numbers.insert(2,numbers[2]*2)
        numbers.pop(3)
    #3
    if numbers[3]/2==int:#ლუწი 
        numbers.insert(3,numbers[3]*numbers[3])
        numbers.pop(4)
    elif numbers[3]/2!=int:#კენტი
        numbers.insert(3,numbers[3]*2)
        numbers.pop(4)
    #4
    if numbers[4]/2==int:#ლუწი 
        numbers.insert(4,numbers[4]*numbers[4])
        numbers.pop(5)
    elif numbers[4]/2!=int:#კენტი
        numbers.insert(4,numbers[4]*2)
        numbers.pop(5)
    #5
    if numbers[5]/2==int:#ლუწი 
        numbers.insert(5,numbers[5]*numbers[5])
        numbers.pop(6)
    elif numbers[5]/2!=int:#კენტი
        numbers.insert(5,numbers[5]*2)
        numbers.pop(6)
        
        return print(numbers)
numsort()



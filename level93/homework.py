#1 lambda function-ის დახამრებით შექმენით ფუნქცია რომელიც ესალმება მომხმარებელს, 
# მაგალიტად თუ მომხარებელმა შემოიტანა მნიშვნელობა Name, დაპრინტეთ Hello Name!

def hello(name):
    x = lambda name : 'hello'+' '+ name
    return print(x(name))

hello('gurt')

#2 Map-ის გამოყენებით list-ში მოცემულ ყველა მნიშვნელობას დაუმატეთ თავისი თავი 
# (გაამრავლეთ ორზე) და გამოიტანეთ მიღებული მნიშვნელობები list-ის სახით

def times2(num):
    return num+num

x = map(times2,[1,2,3,4,5])
print(list(x))

#3 Filter-ის გამოყენებით list-ში შეინახეთ მხოლოდ ისეთი მნიშველობები მოცემული 
# list-იდან რომელიც უნაშთოდ იყოფა 5-ზე (5-ის ჯერადია):
listn = [1,3,5,6,7,10,15,21,25.5,30,101,105]
def five(num):
    if num % 5:
        return False
    else:
        return True

x = filter(five,listn)
for num in x:
    print(num)
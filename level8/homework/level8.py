num = 5

# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False 

# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False

print("----------- AND -----------")
#and-ის შემთხვევაში, თუ ერთი უტოლობა არასწორია, მაშინ მთლიანად არასწორია
print(num >= 1 and num <= 10) # True
print(num >= 1 and num <= 4) # False
print(num > 5 and num <= 10) # False
print(num > 5 and num > 10) # False

print("----------- OR -----------")
#or-ის შემთხვევაში, თუ ერთი მაინც სწორია, მაშინ მთლიანად სწორია
print(num >= 1 or num <= 10) # True
print(num >= 1 or num <= 4) # True
print(num > 5 or num <= 10) # True
print(num > 5 or num > 10) # False

#სამუშაო
#or
print(num>=5 or num <=9)
print(num<5 or num==5)
print(num==0 or num<=5)
print(num<10 or num>4)
print(num-1<5 or num+1>5)
#and
print(num>=5 and num <=9)
print(num<5 and num==5)
print(num==0 and num<=5)
print(num<10 and num>4)
print(num-1<5 and num+1>5)

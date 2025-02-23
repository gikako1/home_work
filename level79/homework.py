# 1) დაადგინეთ შემოსული წელი ნაკიანია თუ არა. ნაკიანია წელიწადი თუ:
# ის არის 4-ის ჯერადი, მაგრამ არა 100-ის ჯერადი
# თუ ის არის 400-ის ჯერადი.

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return print("this is a leap year")
    else:
        return print("this it not a leap year")

leap_year(2004) 
leap_year(2005) 
leap_year(2100) 

# 2) შემოდის სამნიშნა რიცხვი. დათვალეთ მისი ციფრთა ჯამი.

def sum_of_digits(number):
    digit_sum = 0
    for i in range(3):
        digit_sum += number % 10
        number //= 10
    return print(digit_sum)
sum_of_digits(199)
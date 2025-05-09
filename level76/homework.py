
#! DAY 76
# /დავალება:
#!/ ქვემოთ მოცემული კოდი უნდა აბრუნებდეს რიცხვის ციფრთა ჯამს, მაგრამ შეცდომაა.
#!/ წაიკითხე კოდი.*
#!/ იპოვე შეცდომა(ები).
#!/ გაასწორე და სწორად დაწერე.
#! def sum_digits(n):
#!     result = 0
#!     while n > 0:
#!         result += n % 10
#!         n // 10
#!     return result
#! print(sum_digits(123))  # მოსალოდნელი შედეგი: 6 (1 + 2 + 3)
#! print(sum_digits(405))  # მოსალოდნელი შედეგი: 9 (4 + 0 + 5)
# დამატებითი კითხვები:
#✅ კოდის გაშვების გარეშე შეგიძლია იპოვო შეცდომა?
# ✅ როგორ შეიძლება კოდი ისე შეცვალო, რომ უარყოფითი რიცხვებიც იმუშაოს სწორად?
#* პრობლემა იმაშია რომ n//10 შედეგს არ ინახავს და უბრალოდ გაატარებს.
#* უნდა ეწეროს n //= 10
#/ დავალება 2: ქვემოთ მოცემულია Python კოდი, რომელიც უნდა აბრუნებდეს ორი უდიდესი განსხვავებული რიცხვის ჯამს სიაში, მაგრამ კოდი არასწორად მუშაობს.

#/ წაიკითხე კოდი ყურადღებით.
#/ იპოვე შეცდომა(ები). (აქაც გაშვების გარეშე)
#/ შესწორებული კოდი დაწერე.
#! def sum_two_largest(lst):
#!     if len(lst) < 2:
#!         return None

#!     max1 = max(lst)
#!     max2 = max(lst)

#!     return max1 + max2

#! print(sum_two_largest([3, 7, 2, 9, 5]))  # მოსალოდნელი შედეგი: 16 (9 + 7)
#! print(sum_two_largest([10, 10, 5, 3]))   # მოსალოდნელი შედეგი: 20 (10 + 10)
# დამატებითი კითხვა:
# ✅ კოდის შეცვლის გარეშე შეგიძლია იპოვო რა არასწორად მუშაობს?
# * პრობლემა იმაშია რომ max1 და max2 ერთმანეთს უდრის და ეს ორ განსხვავებულ უდიდეს რიცხვთა ჯამს კი არ ამოაგდებს,
# * არამედ array-ს უდიდეს რიცხვს ფაქტობრივად გაამრავლებს ორზე.
# * მე აქ შემიძლია გამოვიყენო bubble sort ტექნიკა და ბოლოს რა სიაც დამრჩება იმის ბოლო ორ რიცხვს ავიღებ
# * და ერთმანეთს მივუმატებ:
def sum_two_largest(arr):
    sorted=False
    while not sorted:
        sorted=True
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted=False
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return print(arr[-1]+arr[-2])

sum_two_largest([1,6,3,5,7,9,15,3])
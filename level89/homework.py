#1 Python-ში slicing-ის დახმარებით შექმენით პროგრამა, რომელიც ამოჭრის მომხმარებლის
#მიერ შემოტანილ სტრინგს იმ ინდექსიდან-ბოლომდე, რომელსაც ასევე მომხმარებელი შემოიტანს.
def slicing(string,num):
    return print(string[num:])
slicing('kombosto123',2)

#2 გაიმეორეთ slicing Js-შიც (გადავიმეორე)

#3 ახსენით რას აკეთებს ყოველი გადაცემული არგუმენტი slicing-ში:
str = "Hello World"

# print(str[x:y:z])
# პირველი არგუმენტი "x" არის დასაწყისი, "y" არის დასასრული, "x" არის რამდენი ნაბიჯი უნდა გადადგა

#4 შექმენით პროგრამა, რომელიც მიიღებს input-ად წინადადებას და დააბრუნებს 
# მასში არსებულ სიტყვებს შემოტრიალებულად, მაგრამ იგივე თანმიმდევრობით.
sentence = 'I put the fries in the bag.'


def reverse(string):
    newstr = []
    strspl = string.split(' ')
    for i in range(len(strspl)):
        newstr.append(strspl[i][::-1])
        continue
    return print(" ".join(newstr))

reverse('kaci shedis saxinkleshi')
reverse('da ukvetavs 100 xinkals')
    